#!/usr/bin/env python3
"""给 store.db 做一致性备份快照（用 sqlite3 backup API，备份时网站可照常运行）。

用法：python3 backup_db.py [数据库路径]
- 数据库路径缺省取环境变量 GEMINI_DB，再缺省为本文件同目录的 store.db；
- 快照写到数据库同目录的 backups/ 子目录，文件名
  store-YYYYMMDD-HHMM.db（同分钟重跑自动加 -2、-3 后缀）；
- 清理规则：按时间从新到旧保留最近 14 份；14 份以外的，仅当
  文件已超过 7 天才删除（即高频手动备份不会挤掉 7 天内的历史）。

部署时配合 gemini-store-backup.service / .timer 每天自动跑一次。
"""
import os
import sqlite3
import sys
import time
from datetime import datetime

KEEP_MAX = 14          # 至少保留的最新份数
KEEP_DAYS = 7          # 超出份数上限时，未满 7 天的也保留
SECONDS_PER_DAY = 24 * 3600


def snapshot(src_path, dest_dir):
    """把 src_path 快照到 dest_dir，返回新文件路径。"""
    os.makedirs(dest_dir, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M")
    dest = os.path.join(dest_dir, f"store-{stamp}.db")
    n = 2
    while os.path.exists(dest):
        dest = os.path.join(dest_dir, f"store-{stamp}-{n}.db")
        n += 1
    src = sqlite3.connect(f"file:{src_path}?mode=ro", uri=True)
    try:
        dst = sqlite3.connect(dest)
        try:
            src.backup(dst)
        finally:
            dst.close()
    finally:
        src.close()
    return dest


def prune(dest_dir, now=None):
    """按保留规则清理旧快照，返回删除的文件名列表。"""
    now = time.time() if now is None else now
    files = []
    for name in os.listdir(dest_dir):
        if name.startswith("store-") and name.endswith(".db"):
            path = os.path.join(dest_dir, name)
            files.append((os.path.getmtime(path), path))
    files.sort(reverse=True)  # 新 → 旧
    removed = []
    for idx, (mtime, path) in enumerate(files):
        if idx < KEEP_MAX:
            continue
        if now - mtime <= KEEP_DAYS * SECONDS_PER_DAY:
            continue
        os.remove(path)
        removed.append(os.path.basename(path))
    return removed


def main(argv):
    src = (argv[1] if len(argv) > 1
           else os.environ.get("GEMINI_DB")
           or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "store.db"))
    if not os.path.exists(src):
        print(f"[backup] 源数据库不存在：{src}", file=sys.stderr)
        return 1
    dest_dir = os.path.join(os.path.dirname(os.path.abspath(src)),
                            "backups")
    dest = snapshot(src, dest_dir)
    removed = prune(dest_dir)
    print(f"[backup] 已备份 {src} -> {dest}"
          f"（{os.path.getsize(dest)} 字节）"
          + (f"；清理旧备份 {len(removed)} 份" if removed else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
