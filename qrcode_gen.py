"""Minimal QR Code generator (byte mode, ECC level M, versions 1-6).

Used to render WeChat Pay Native `code_url` as a scannable QR code without
any third-party dependency. Produces a boolean module matrix that callers
can render as SVG/HTML.

Implementation follows ISO/IEC 18004: data encoding -> Reed-Solomon error
correction over GF(256) -> block interleaving -> matrix placement ->
mask evaluation (all 8 masks scored with the standard penalty rules) ->
format information via BCH(15,5).
"""

# (ecc_codewords_per_block, [(num_blocks, data_codewords_per_block), ...])
_ECC_TABLE_M = {
    1: (10, [(1, 16)]),
    2: (16, [(1, 28)]),
    3: (26, [(1, 44)]),
    4: (18, [(2, 32)]),
    5: (24, [(2, 43)]),
    6: (16, [(4, 27)]),
}

_ALIGNMENT_CENTERS = {
    1: [],
    2: [6, 18],
    3: [6, 22],
    4: [6, 26],
    5: [6, 30],
    6: [6, 34],
}

# GF(256) tables, primitive polynomial 0x11D, generator 2.
_GF_EXP = [0] * 512
_GF_LOG = [0] * 256
_x = 1
for _i in range(255):
    _GF_EXP[_i] = _x
    _GF_LOG[_x] = _i
    _x <<= 1
    if _x & 0x100:
        _x ^= 0x11D
for _i in range(255, 512):
    _GF_EXP[_i] = _GF_EXP[_i - 255]


def _gf_mul(a, b):
    if a == 0 or b == 0:
        return 0
    return _GF_EXP[_GF_LOG[a] + _GF_LOG[b]]


def _rs_generator(degree):
    poly = [1]
    for i in range(degree):
        poly = _poly_mul(poly, [1, _GF_EXP[i]])
    return poly


def _poly_mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] ^= _gf_mul(a, b)
    return out


def _rs_encode(data, gen):
    ecc = [0] * (len(gen) - 1)
    for byte in data:
        factor = byte ^ ecc[0]
        ecc = ecc[1:] + [0]
        for j in range(len(ecc)):
            ecc[j] ^= _gf_mul(gen[j + 1], factor)
    return ecc


def _encode_data(data_bytes, version):
    ecc_per_block, groups = _ECC_TABLE_M[version]
    total_data = sum(n * d for n, d in groups)
    capacity_bits = total_data * 8
    bits = []

    def push(value, length):
        for i in range(length - 1, -1, -1):
            bits.append((value >> i) & 1)

    push(0b0100, 4)  # byte mode
    push(len(data_bytes), 8)  # byte mode length is 8 bits for versions 1-9
    for b in data_bytes:
        push(b, 8)
    # terminator + byte alignment + pad bytes
    bits += [0] * min(4, capacity_bits - len(bits))
    while len(bits) % 8:
        bits.append(0)
    codewords = []
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i + 8]:
            byte = (byte << 1) | bit
        codewords.append(byte)
    pad = 0xEC
    while len(codewords) < total_data:
        codewords.append(pad)
        pad = 0x11 if pad == 0xEC else 0xEC

    # split into blocks, compute ECC
    blocks = []
    pos = 0
    gen = _rs_generator(ecc_per_block)
    for num, per in groups:
        for _ in range(num):
            block = codewords[pos:pos + per]
            pos += per
            blocks.append((block, _rs_encode(block, gen)))
    # interleave data then ECC
    result = []
    for i in range(max(len(b[0]) for b in blocks)):
        for data, _ in blocks:
            if i < len(data):
                result.append(data[i])
    for i in range(ecc_per_block):
        for _, ecc in blocks:
            result.append(ecc[i])
    return result


def _format_bits(mask):
    # ECC level M indicator bits = 00
    data = (0b00 << 3) | mask
    rem = data
    for _ in range(10):
        rem = (rem << 1) ^ (0x537 if (rem >> 9) & 1 else 0)
    return (((data << 10) | rem) ^ 0x5412) & 0x7FFF


def _function_matrix(version):
    """Matrix with function patterns filled, data cells None."""
    size = 17 + 4 * version
    m = [[None] * size for _ in range(size)]

    def finder(top, left):
        for dr in range(-1, 8):
            for dc in range(-1, 8):
                r, c = top + dr, left + dc
                if not (0 <= r < size and 0 <= c < size):
                    continue
                m[r][c] = (0 <= dr <= 6 and dc in (0, 6)) or \
                          (0 <= dc <= 6 and dr in (0, 6)) or \
                          (2 <= dr <= 4 and 2 <= dc <= 4)

    finder(0, 0)
    finder(0, size - 7)
    finder(size - 7, 0)
    for i in range(8, size - 8):
        m[6][i] = (i % 2 == 0)
        m[i][6] = (i % 2 == 0)
    centers = _ALIGNMENT_CENTERS[version]
    for r in centers:
        for c in centers:
            if m[r][c] is not None:
                continue
            for dr in range(-2, 3):
                for dc in range(-2, 3):
                    m[r + dr][c + dc] = (max(abs(dr), abs(dc)) != 1)
    m[size - 8][8] = True  # dark module
    # reserve format info cells
    for i in range(9):
        if m[8][i] is None:
            m[8][i] = False
        if m[i][8] is None:
            m[i][8] = False
    for i in range(8):
        if m[8][size - 1 - i] is None:
            m[8][size - 1 - i] = False
        if m[size - 1 - i][8] is None:
            m[size - 1 - i][8] = False
    return m


def _place_format(m, mask):
    size = len(m)
    fmt = _format_bits(mask)
    bits = [(fmt >> i) & 1 == 1 for i in range(15)]  # bits[0] = LSB
    # positions per spec: first copy around top-left finder
    coords1 = [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 7),
               (8, 8), (7, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8)]
    for (r, c), bit in zip(coords1, reversed(bits)):
        m[r][c] = bit
    coords2 = [(size - 1, 8), (size - 2, 8), (size - 3, 8), (size - 4, 8),
               (size - 5, 8), (size - 6, 8), (size - 7, 8),
               (8, size - 8), (8, size - 7), (8, size - 6), (8, size - 5),
               (8, size - 4), (8, size - 3), (8, size - 2), (8, size - 1)]
    for (r, c), bit in zip(coords2, reversed(bits)):
        m[r][c] = bit
    m[size - 8][8] = True  # dark module stays dark


_MASKS = [
    lambda r, c: (r + c) % 2 == 0,
    lambda r, c: r % 2 == 0,
    lambda r, c: c % 3 == 0,
    lambda r, c: (r + c) % 3 == 0,
    lambda r, c: (r // 2 + c // 3) % 2 == 0,
    lambda r, c: (r * c) % 2 + (r * c) % 3 == 0,
    lambda r, c: ((r * c) % 2 + (r * c) % 3) % 2 == 0,
    lambda r, c: ((r + c) % 2 + (r * c) % 3) % 2 == 0,
]


def _penalty(m):
    size = len(m)
    score = 0
    # rule 1: runs of >=5 same-color modules in rows/columns
    for is_col in (False, True):
        for i in range(size):
            line = [m[j][i] if is_col else m[i][j] for j in range(size)]
            run_color, run_len = line[0], 1
            for v in line[1:]:
                if v == run_color:
                    run_len += 1
                else:
                    if run_len >= 5:
                        score += 3 + (run_len - 5)
                    run_color, run_len = v, 1
            if run_len >= 5:
                score += 3 + (run_len - 5)
    # rule 2: 2x2 blocks
    for r in range(size - 1):
        for c in range(size - 1):
            if m[r][c] == m[r][c + 1] == m[r + 1][c] == m[r + 1][c + 1]:
                score += 3
    # rule 3: finder-like patterns 1011101 with 4-module quiet zone
    pattern = [True, False, True, True, True, False, True]
    for is_col in (False, True):
        for i in range(size):
            line = [m[j][i] if is_col else m[i][j] for j in range(size)]
            for j in range(size - 6):
                if line[j:j + 7] == pattern:
                    before = j >= 4 and not any(line[j - 4:j])
                    after = j + 11 <= size and not any(line[j + 7:j + 11])
                    if before or after:
                        score += 40
    # rule 4: dark module proportion
    dark = sum(sum(1 for v in row if v) for row in m)
    total = size * size
    k = int(abs(dark * 20 - total * 10) / total)
    score += k * 10
    return score


def generate(text):
    """Return (size, matrix) for the given text, best mask chosen by penalty."""
    data = text.encode("utf-8")
    version = None
    for v in range(1, 7):
        _, groups = _ECC_TABLE_M[v]
        if len(data) <= sum(n * d for n, d in groups) - 2:
            version = v
            break
    if version is None:
        raise ValueError("内容太长，超出二维码容量")
    codewords = _encode_data(data, version)
    bits = []
    for cw in codewords:
        for i in range(7, -1, -1):
            bits.append((cw >> i) & 1)
    bits += [0] * {1: 0, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7}[version]

    size = 17 + 4 * version
    best = None
    for mask in range(8):
        m = _function_matrix(version)
        # data placement
        idx = 0
        upward = True
        col = size - 1
        data_cells = []
        while col > 0:
            if col == 6:
                col -= 1
            rows = range(size - 1, -1, -1) if upward else range(size)
            for r in rows:
                for c in (col, col - 1):
                    if m[r][c] is None:
                        data_cells.append((r, c))
            upward = not upward
            col -= 2
        for i, (r, c) in enumerate(data_cells):
            bit = bool(bits[i]) if i < len(bits) else False
            if _MASKS[mask](r, c):
                bit = not bit
            m[r][c] = bit
        _place_format(m, mask)
        score = _penalty(m)
        if best is None or score < best[0]:
            best = (score, m)
    return size, best[1]


def to_svg(text, scale=6, border=4):
    """Render the QR code for `text` as a standalone SVG string."""
    size, m = generate(text)
    total = (size + border * 2) * scale
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{total}" '
             f'height="{total}" viewBox="0 0 {total} {total}">',
             f'<rect width="{total}" height="{total}" fill="#ffffff"/>']
    for r in range(size):
        for c in range(size):
            if m[r][c]:
                x = (c + border) * scale
                y = (r + border) * scale
                parts.append(f'<rect x="{x}" y="{y}" width="{scale}" '
                             f'height="{scale}" fill="#000000"/>')
    parts.append('</svg>')
    return ''.join(parts)
