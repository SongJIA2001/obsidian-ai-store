# -*- coding: utf-8 -*-
"""upgrade19 多语言译文：葡萄牙语（pt，巴西葡语）与俄语（ru）。
由 i18n.merge_extra() 按变量名约定合并：STRINGS_X / PRODUCTS_X /
BLOBS_X / WARRANTY_X / CAT_X / ANN_X / LEVEL_X（后缀 = 语言代码大写）。
"""

STRINGS_PT = {
    "nav.home": "Início", "nav.order": "Pedir agora",
    "nav.my_orders": "Meus pedidos", "nav.wallet": "Minha carteira",
    "nav.support": "Atendimento", "nav.guide": "Guia de uso",
    "nav.admin": "Painel do vendedor", "nav.logout": "Sair",
    "nav.login": "Entrar", "nav.register": "Cadastrar",
    "nav.track": "Rastrear pedido",
    "footer.tag": "Apenas serviços digitais, sem envio físico",
    "footer.privacy": "Política de Privacidade",
    "footer.terms": "Termos de Uso",
    "footer.cookies": "Política de Cookies",
    "home.search_ph": "Buscar produtos",
    "home.all": "Todos",
    "home.buy": "Comprar agora →", "home.soldout": "Esgotado",
    "home.sold_n": "{n} vendidos",
    "home.stock_n": "{n} em estoque",
    "home.stock_low": "🔥 Restam apenas {n}",
    "home.stock_plenty": "Em estoque",
    "home.no_match": "Nenhum produto encontrado",
    "common.yuan": "¥",
    "status.unpaid": "Aguardando pagamento",
    "status.paid": "Pago / Aguardando entrega",
    "status.completed": "Concluído (entregue)",
    "status.failed": "Falhou",
    "status.refunded": "Reembolsado",
    "status.cancelled": "Cancelado",
    "home.title": "Todos os produtos",
    "track.err_notfound": "Número do pedido ou contato incorreto — verifique e tente novamente",
    "track.result_title": "Resultado da consulta",
    "track.more": "Consultar outro",
    "chat.me": "Eu", "chat.seller": "Vendedor", "chat.customer": "Cliente",
    "chat.empty": "Ainda não há mensagens. Deixe uma mensagem abaixo e o vendedor responderá assim que a vir.",
    "lock.msg": "Muitas tentativas — tente novamente em {m} min",
    "guide.contact": "Falar com o vendedor",
    "guide.contact_hint": "O vendedor costuma estar disponível no horário comercial. Inclua o número do pedido nas mensagens para um atendimento mais rápido.",
    "legal.privacy_title": "Política de Privacidade",
    "legal.terms_title": "Termos de Uso",
    "legal.cookies_title": "Política de Cookies",
    "legal.updated": "Última atualização: 2026-11-08 · Aplicável a muse798.com (OBSIDIAN AI)",
    "legal.contact_pre": "Contato: ",
    "legal.contact_post": " ou o vendedor no QQ {qq}.",
    "rpay.result_title": "Resultado da recarga",
    "rpay.credited": "Creditado",
    "rpay.confirming": "Confirmando",
    "rpay.tip_credited": "Sua recarga foi creditada — confira o saldo em Minha carteira.",
    "rpay.tip_confirming": "Seu pagamento ainda está sendo confirmado — atualize Minha carteira em instantes.",
    "pay.title": "Pagar pedido",
    "pay.order_no": "Nº do pedido: ",
    "pay.product": "Produto: ",
    "pay.amount": "Valor a pagar: ",
    "pay.balance_btn": "Pagar com saldo (saldo de ¥{b})",
    "pay.balance_low_pre": "Seu saldo é de ¥{b}, insuficiente para este pedido. Você pode ",
    "pay.goto_recharge": "recarregar primeiro",
    "pay.balance_low_post": ".",
    "pay.balance_zero_pre": "Seu saldo é de ¥0,00. Você pode ",
    "pay.recharge_word": "recarregar",
    "pay.balance_zero_post": " e depois pagar diretamente com o saldo.",
    "pay.epay_btn": "Pagar com Alipay",
    "pay.note": "Após o pagamento, o pedido muda automaticamente para \"Pago / Aguardando entrega\" e o vendedor o processará na ordem. Até o pagamento ser concluído, o pedido permanece não pago e nada é cobrado.",
    "pay.status_title": "Status do pedido",
    "pay.status_amount": "Valor: ",
    "pay.status_now": "Status: ",
    "pay.tip_paid": "Pagamento confirmado. O vendedor processará seu pedido na ordem.",
    "pay.tip_unpaid": "O resultado do pagamento ainda está sendo confirmado (vale a notificação assíncrona da plataforma de pagamento). Atualize Meus pedidos em instantes. Se o pagamento não foi concluído, o pedido permanece não pago e nada é cobrado.",
    "pay.tip_other": "O status do pedido está acima. Dúvidas? Fale com o vendedor.",
    "pay.view_detail": "Ver detalhes do pedido",
    "wallet.title": "Minha carteira",
    "wallet.balance_label": "Saldo atual",
    "wallet.custom_label": "Ou informe um valor personalizado (CNY)",
    "wallet.custom_ph": "ex.: 30",
    "wallet.recharge_btn": "Recarregar com Alipay",
    "wallet.note": "Recarregue via Alipay; após o crédito, você pode pagar pedidos diretamente com o saldo. Recarga única de ¥1 a ¥5000. O saldo não pode ser sacado; reembolsos de pedidos pagos com saldo retornam automaticamente ao saldo.",
    "wallet.bonus_banner": "🎁 <b>Oferta de primeira recarga</b>: primeira recarga de ¥10 ou mais credita <b>¥12</b>; de ¥15 ou mais credita <b>¥20</b>. O bônus chega automaticamente junto com o valor principal. Uma vez por pessoa.",
    "wallet.paid_badge": "Creditado",
    "wallet.unpaid_link": "Não pago · Pagar agora",
    "wallet.bonus_incl": "Inclui bônus de primeira recarga de ¥{b}; ¥{t} creditados no total",
    "wallet.no_recharges": "Ainda não há registros de recarga",
    "wallet.no_logs": "Ainda não há movimentações",
    "wallet.records": "Histórico de recargas",
    "wallet.rc_no": "Nº da recarga",
    "wallet.amount": "Valor",
    "wallet.status": "Status",
    "wallet.time": "Hora",
    "wallet.logs": "Movimentações",
    "wallet.type": "Tipo",
    "wallet.change": "Variação",
    "wallet.balance": "Saldo",
    "wallet.note_col": "Observação",
    "wallet.member_title": "👑 Nível de membro",
    "wallet.member_now": "Nível atual: <b>{name}</b> ({n} níveis no total; os descontos são aplicados automaticamente ao pedir)",
    "wallet.lv_current": "Atual",
    "wallet.lv_next": "Próximo",
    "wallet.lv_member": "Membro",
    "wallet.lv_disc_all": "{label} em todo o site",
    "wallet.lv_disc_default": "Nível padrão",
    "wallet.lv_req": "Upgrade automático ao gastar ¥{s} ou recarregar ¥{r}",
    "wallet.lv_manual": "Seu nível foi definido manualmente pelo vendedor 🎁 (progresso automático: ¥{s} gastos · ¥{r} recarregados)",
    "wallet.lv_progress": "Total gasto ¥{s} · total recarregado ¥{r}; para {name}: faltam ¥{ds} em compras ou ¥{dr} em recargas",
    "wallet.lv_max": "Total gasto ¥{s} · total recarregado ¥{r}; você está no nível máximo 🎉",
    "wallet.err_amount": "Valor de recarga inválido: informe um valor entre ¥1 e ¥5000.",
    "wallet.err_expired": "Esta página expirou — atualize e tente novamente.",
    "kind.recharge": "Recarga online",
    "kind.bonus": "Bônus de primeira recarga",
    "kind.pay": "Pagamento com saldo",
    "kind.refund": "Reembolso",
    "kind.admin": "Ajuste do vendedor",
    "rpay.title": "Pagamento de recarga",
    "rpay.no": "Nº da recarga: ",
    "rpay.amount": "Valor da recarga: ",
    "rpay.bonus_hint": "🎁 Esta é a sua primeira recarga: um bônus extra de <b>¥{b}</b> será creditado, <b>¥{t}</b> no total.",
    "rpay.note": "Após o pagamento, seu saldo é creditado automaticamente — confira em Minha carteira. Se houver um pequeno atraso, o site consulta a plataforma de pagamento a cada minuto.",
    "rpay.not_found": "Recarga não encontrada",
    "forgot.title": "Esqueci a senha",
    "forgot.p1": "A recuperação por e-mail ainda não está disponível. Se você esqueceu a senha, fale com o vendedor para confirmar sua identidade e redefini-la:",
    "forgot.li1": "Envie uma mensagem pelo Atendimento no topo da página ou adicione o vendedor no QQ <b>{qq}</b> e informe seu <b>e-mail cadastrado</b>;",
    "forgot.li2": "Após a confirmação, o vendedor redefinirá sua senha no painel e enviará a nova senha a você;",
    "forgot.li3_pre": "Ao receber a nova senha, ",
    "forgot.li3_post": " o quanto antes para confirmar que funciona.",
    "forgot.hint": "Observação: o vendedor nunca pedirá a senha da sua conta Google. A redefinição de senha é feita apenas dessa forma — desconfie de outros canais.",
    "forgot.back": "Voltar ao login",
    "qq.title": "A recarga precisa da ajuda do vendedor",
    "qq.copy": "Copiar QQ",
    "qq.note": "Informe o número do seu pedido ao adicionar. O vendedor ajudará você a concluir a recarga. Observação: o vendedor nunca pedirá a senha da sua conta Google.",
    "qq.pre": "Adicione o vendedor no QQ",
    "nf.title": "Página não encontrada",
    "nf.body": "A página que você acessou pode ter sido movida ou o endereço foi digitado incorretamente.",
    "nf.home": "Voltar ao início",
    "nf.guide": "Ler o guia de uso",
    "support.title": "Atendimento",
    "support.intro": "O vendedor responde pessoalmente (não é um robô), geralmente em poucos minutos. Você também pode adicionar o vendedor no QQ {qq}. Para dúvidas sobre pedidos, inclua o número do pedido.",
    "support.ph": "Digite uma mensagem, ex.: Pedido GM... ainda não creditado",
    "support.send": "Enviar",
    "support.err_expired": "Esta página expirou — atualize e tente novamente.",
    "orders.title": "Meus pedidos",
    "orders.empty": "Ainda não há pedidos.",
    "orders.go_order": "Fazer um pedido",
    "orders.no": "Nº do pedido",
    "orders.product": "Produto",
    "orders.status": "Status",
    "orders.detail": "Detalhes",
    "orders.pay": "Pagar agora",
    "orders.cancel": "Cancelar pedido",
    "orders.cancel_confirm": "Cancelar este pedido?",
    "orders.cancel_confirm2": "Cancelar este pedido? Isso não pode ser desfeito.",
    "orders.delivery_title": "📦 Entrega (dados da conta)",
    "common.copy": "Copiar",
    "orders.gemini_qq_pre": "QQ de ajuda para recarga:",
    "orders.gemini_qq_note": "(informe o número do pedido ao adicionar)",
    "detail.title": "Detalhes do pedido",
    "detail.not_found": "Pedido não encontrado",
    "detail.order_no": "Nº do pedido",
    "detail.product": "Produto: ",
    "detail.amount": "Valor: ",
    "detail.created": "Pedido feito em: ",
    "detail.paid_at": "Pago em: ",
    "detail.status": "Status: ",
    "detail.usage": "Como usar",
    "detail.delivery": "Entrega",
    "detail.delivery_keep": "Guarde o conteúdo da entrega em segurança — não o encaminhe a ninguém.",
    "detail.delivery_account": "📦 Dados da conta",
    "detail.copy_all": "Copiar tudo",
    "detail.download_all": "Baixar conteúdo da entrega",
    "detail.view_orders": "Ver pedidos",
    "detail.continue": "Continuar comprando",
    "detail.file_suffix": "entrega",
    "hero.completed": "Pedido concluído",
    "hero.paid": "Pago — vendedor processando",
    "hero.unpaid": "Aguardando pagamento",
    "hero.failed": "Pedido falhou",
    "hero.refunded": "Pedido reembolsado",
    "hero.cancelled": "Pedido cancelado",
    "tip.completed": "O vendedor concluiu este pedido; a entrega está abaixo (se houver).",
    "tip.paid": "Pagamento confirmado. O vendedor processa os pedidos na ordem; a entrega aparecerá nesta página quando estiver pronta.",
    "tip.unpaid": "O vendedor só começa a processar após a conclusão do pagamento.",
    "tip.failed": "O processamento deste pedido falhou. Para pós-venda, fale com o vendedor no QQ informando o número do pedido.",
    "tip.refunded": "Este pedido foi reembolsado. Dúvidas? Fale com o vendedor.",
    "tip.cancelled": "Este pedido foi cancelado e não será processado. Faça um novo pedido se ainda quiser o produto.",
    "track.title": "Rastrear pedido",
    "track.intro": "Sem cadastro nem login: informe o <b>número do pedido</b> recebido após a compra e o <b>contato</b> utilizado (deve ser exatamente igual) para ver o status e a entrega do pedido.",
    "track.order_no": "Número do pedido",
    "track.order_no_ph": "O número do pedido exibido após a compra",
    "track.contact": "Contato",
    "track.contact_ph": "O contato que você usou na compra",
    "track.submit": "Consultar pedido",
    "track.alt_pre": "Usuários cadastrados também podem ",
    "track.alt_login": "entrar",
    "track.alt_mid": " e verificar em Meus pedidos. Ainda não encontrou? Adicione o vendedor no QQ ",
    "track.alt_post": " informando o número do pedido.",
    "order.title": "Pedido",
    "order.soldout_title": "Esgotado",
    "order.soldout_body": "😔 Este produto acabou de esgotar. Ele voltará quando o vendedor reabastecer o estoque.",
    "order.soldout_hint": "Com pressa? Adicione o vendedor no QQ {qq} ou veja outros produtos primeiro.",
    "order.back_home": "← Voltar ao início e ver outros produtos",
    "order.stock_hint": "🔥 Restam apenas {n} — um fica reservado para você assim que o pagamento for concluído.",
    "order.required": "*obrigatório",
    "order.aux_label": "E-mail reserva",
    "order.aux_hint": "Usado se for necessária verificação durante a recarga. Obrigatório e deve estar em formato válido.",
    "order.contact_label": "Contato",
    "order.contact_ph": "WeChat / telefone / QQ, para o vendedor falar com você",
    "order.submit": "Enviar pedido e pagar",
    "order.after_sale_pre": "Pós-venda: reembolso total antes da entrega; se uma conta entregue não conseguir entrar, fale com o vendedor imediatamente. Regras completas no ",
    "order.after_sale_post": ".",
    "order.one_time": "pagamento único",
    "order.member_line": "👑 Benefício {name}: {label}, você economiza ¥{off} neste pedido",
    "order.err_expired": "Esta página expirou — atualize e tente novamente",
    "order.err_soldout": "Este produto está esgotado",
    "order.err_aux_required": "O e-mail reserva é obrigatório e não pode ficar vazio",
    "order.err_aux_format": "Formato do e-mail reserva incorreto",
    "order.err_contact_required": "O contato é obrigatório",
    "trust.sold": "{n} pedidos vendidos",
    "trust.avg_min": "Entrega média ≈ {n} min",
    "trust.avg_hour": "Entrega média ≈ {n} h",
    "trust.nopass": "Nunca pedimos a senha da sua conta",
    "auth.register": "Cadastrar",
    "auth.register_sub": "Crie uma conta e comece a pedir agora mesmo",
    "auth.email": "E-mail",
    "auth.password_rule": "Senha (mínimo de 8 caracteres)",
    "auth.password_set_ph": "Defina uma senha",
    "auth.have_account": "Já tem uma conta?",
    "auth.go_login": "Entrar",
    "auth.login": "Entrar",
    "auth.login_sub": "Entre para pedir e acompanhar seus pedidos a qualquer momento",
    "auth.password": "Senha",
    "auth.password_ph": "Digite sua senha",
    "auth.no_account": "Ainda não tem conta?",
    "auth.register_now": "Cadastre-se agora",
    "auth.forgot": "Esqueci a senha",
    "auth.track_hint": "Pediu sem se cadastrar? Use o número do pedido + contato para",
    "auth.track_link": "consulta de pedido como visitante",
    "auth.err_email": "Formato de e-mail inválido",
    "auth.err_pw_short": "A senha deve ter pelo menos 8 caracteres",
    "auth.err_email_taken": "Este e-mail já está cadastrado — faça login",
    "auth.err_login": "E-mail ou senha incorretos",
}

STRINGS_RU = {
    "nav.home": "Главная", "nav.order": "Заказать",
    "nav.my_orders": "Мои заказы", "nav.wallet": "Мой кошелёк",
    "nav.support": "Поддержка", "nav.guide": "Инструкция",
    "nav.admin": "Панель продавца", "nav.logout": "Выйти",
    "nav.login": "Войти", "nav.register": "Регистрация",
    "nav.track": "Отследить заказ",
    "footer.tag": "Только цифровые услуги, без физической доставки",
    "footer.privacy": "Политика конфиденциальности",
    "footer.terms": "Условия использования",
    "footer.cookies": "Политика cookies",
    "home.search_ph": "Поиск товаров",
    "home.all": "Все",
    "home.buy": "Купить →", "home.soldout": "Нет в наличии",
    "home.sold_n": "Продано: {n}",
    "home.stock_n": "В наличии: {n}",
    "home.stock_low": "🔥 Осталось всего {n}",
    "home.stock_plenty": "В наличии",
    "home.no_match": "Подходящих товаров нет",
    "common.yuan": "¥",
    "status.unpaid": "Ожидает оплаты",
    "status.paid": "Оплачено / Ожидает доставки",
    "status.completed": "Выполнено (доставлено)",
    "status.failed": "Не удалось",
    "status.refunded": "Возвращено",
    "status.cancelled": "Отменено",
    "home.title": "Все товары",
    "track.err_notfound": "Номер заказа или контактные данные указаны неверно — проверьте и попробуйте снова",
    "track.result_title": "Результат поиска заказа",
    "track.more": "Искать ещё",
    "chat.me": "Я", "chat.seller": "Продавец", "chat.customer": "Клиент",
    "chat.empty": "Сообщений пока нет. Оставьте сообщение ниже — продавец ответит, как только увидит его.",
    "lock.msg": "Слишком много попыток — попробуйте снова через {m} мин",
    "guide.contact": "Связаться с продавцом",
    "guide.contact_hint": "Продавец обычно на связи в рабочее время. Указывайте номер заказа в сообщениях — так обработка будет быстрее.",
    "legal.privacy_title": "Политика конфиденциальности",
    "legal.terms_title": "Условия использования",
    "legal.cookies_title": "Политика cookies",
    "legal.updated": "Обновлено: 2026-11-08 · Действует для muse798.com (OBSIDIAN AI)",
    "legal.contact_pre": "Контакт: ",
    "legal.contact_post": " или продавец в QQ {qq}.",
    "rpay.result_title": "Результат пополнения",
    "rpay.credited": "Зачислено",
    "rpay.confirming": "Подтверждается",
    "rpay.tip_credited": "Пополнение зачислено — проверьте баланс в разделе «Мой кошелёк».",
    "rpay.tip_confirming": "Платёж ещё подтверждается — обновите «Мой кошелёк» чуть позже.",
    "pay.title": "Оплата заказа",
    "pay.order_no": "Номер заказа: ",
    "pay.product": "Товар: ",
    "pay.amount": "Сумма к оплате: ",
    "pay.balance_btn": "Оплатить с баланса (баланс ¥{b})",
    "pay.balance_low_pre": "Ваш баланс — ¥{b}, этого недостаточно для заказа. Вы можете ",
    "pay.goto_recharge": "сначала пополнить",
    "pay.balance_low_post": ".",
    "pay.balance_zero_pre": "Ваш баланс — ¥0,00. Вы можете ",
    "pay.recharge_word": "пополнить",
    "pay.balance_zero_post": " и затем оплатить напрямую с баланса.",
    "pay.epay_btn": "Оплатить через Alipay",
    "pay.note": "После оплаты статус заказа автоматически изменится на «Оплачено / Ожидает доставки», и продавец обработает его в порядке очереди. Пока оплата не завершена, заказ остаётся неоплаченным и средства не списываются.",
    "pay.status_title": "Статус заказа",
    "pay.status_amount": "Сумма: ",
    "pay.status_now": "Статус: ",
    "pay.tip_paid": "Оплата подтверждена. Продавец обработает ваш заказ в порядке очереди.",
    "pay.tip_unpaid": "Результат оплаты ещё подтверждается (окончательным является асинхронное уведомление платёжной платформы). Обновите «Мои заказы» чуть позже. Если оплата не была завершена, заказ останется неоплаченным и средства не спишутся.",
    "pay.tip_other": "Статус заказа показан выше. Есть вопросы? Свяжитесь с продавцом.",
    "pay.view_detail": "Детали заказа",
    "wallet.title": "Мой кошелёк",
    "wallet.balance_label": "Текущий баланс",
    "wallet.custom_label": "Или укажите свою сумму (CNY)",
    "wallet.custom_ph": "например, 30",
    "wallet.recharge_btn": "Пополнить через Alipay",
    "wallet.note": "Пополняйте через Alipay; после зачисления вы сможете оплачивать заказы напрямую с баланса. Разовое пополнение — от ¥1 до ¥5000. Вывод баланса не поддерживается; возврат за заказы, оплаченные с баланса, автоматически возвращается на баланс.",
    "wallet.bonus_banner": "🎁 <b>Бонус за первое пополнение</b>: при первом пополнении от ¥10 зачисляется <b>¥12</b>, от ¥15 — <b>¥20</b>. Бонус поступает автоматически вместе с основной суммой. Один раз на человека.",
    "wallet.paid_badge": "Зачислено",
    "wallet.unpaid_link": "Не оплачено · Оплатить",
    "wallet.bonus_incl": "Включая бонус за первое пополнение ¥{b}; всего зачислено ¥{t}",
    "wallet.no_recharges": "Записей о пополнениях пока нет",
    "wallet.no_logs": "Операций пока нет",
    "wallet.records": "История пополнений",
    "wallet.rc_no": "Номер пополнения",
    "wallet.amount": "Сумма",
    "wallet.status": "Статус",
    "wallet.time": "Время",
    "wallet.logs": "Операции",
    "wallet.type": "Тип",
    "wallet.change": "Изменение",
    "wallet.balance": "Баланс",
    "wallet.note_col": "Примечание",
    "wallet.member_title": "👑 Уровень участника",
    "wallet.member_now": "Текущий уровень: <b>{name}</b> (всего уровней: {n}; скидки применяются автоматически при заказе)",
    "wallet.lv_current": "Текущий",
    "wallet.lv_next": "Следующий",
    "wallet.lv_member": "Участник",
    "wallet.lv_disc_all": "{label} на весь сайт",
    "wallet.lv_disc_default": "Уровень по умолчанию",
    "wallet.lv_req": "Автоповышение при тратах ¥{s} или пополнениях ¥{r}",
    "wallet.lv_manual": "Ваш уровень установлен продавцом вручную 🎁 (автопрогресс: потрачено ¥{s} · пополнено ¥{r})",
    "wallet.lv_progress": "Всего потрачено ¥{s} · всего пополнено ¥{r}; до уровня {name}: ещё ¥{ds} в покупках или ¥{dr} в пополнениях",
    "wallet.lv_max": "Всего потрачено ¥{s} · всего пополнено ¥{r}; у вас максимальный уровень 🎉",
    "wallet.err_amount": "Неверная сумма пополнения: укажите сумму от ¥1 до ¥5000.",
    "wallet.err_expired": "Страница устарела — обновите её и попробуйте снова.",
    "kind.recharge": "Онлайн-пополнение",
    "kind.bonus": "Бонус за первое пополнение",
    "kind.pay": "Оплата с баланса",
    "kind.refund": "Возврат",
    "kind.admin": "Корректировка продавца",
    "rpay.title": "Оплата пополнения",
    "rpay.no": "Номер пополнения: ",
    "rpay.amount": "Сумма пополнения: ",
    "rpay.bonus_hint": "🎁 Это ваше первое пополнение: дополнительно будет зачислен бонус <b>¥{b}</b>, всего <b>¥{t}</b>.",
    "rpay.note": "После успешной оплаты баланс зачисляется автоматически — проверьте в «Моём кошельке». При небольшой задержке сайт каждую минуту запрашивает подтверждение у платёжной платформы.",
    "rpay.not_found": "Пополнение не найдено",
    "forgot.title": "Забыли пароль",
    "forgot.p1": "Самостоятельное восстановление по e-mail пока недоступно. Если вы забыли пароль, свяжитесь с продавцом, чтобы подтвердить личность и сбросить пароль:",
    "forgot.li1": "Напишите через «Поддержку» вверху страницы или добавьте продавца в QQ <b>{qq}</b> и укажите ваш <b>зарегистрированный e-mail</b>;",
    "forgot.li2": "После проверки продавец сбросит ваш пароль в панели и отправит вам новый;",
    "forgot.li3_pre": "Получив новый пароль, пожалуйста, ",
    "forgot.li3_post": " как можно скорее, чтобы убедиться, что он работает.",
    "forgot.hint": "Обратите внимание: продавец никогда не попросит пароль от вашего аккаунта Google. Сброс пароля выполняется только этим способом — остерегайтесь других каналов.",
    "forgot.back": "Назад ко входу",
    "qq.title": "Для пополнения нужна помощь продавца",
    "qq.copy": "Копировать QQ",
    "qq.note": "При добавлении укажите номер вашего заказа. Продавец поможет вам завершить пополнение. Обратите внимание: продавец никогда не попросит пароль от вашего аккаунта Google.",
    "qq.pre": "Добавьте продавца в QQ",
    "nf.title": "Страница не найдена",
    "nf.body": "Страница, которую вы открыли, возможно, была перемещена, или адрес введён неверно.",
    "nf.home": "На главную",
    "nf.guide": "Читать инструкцию",
    "support.title": "Поддержка",
    "support.intro": "Продавец отвечает лично (не бот), обычно в течение нескольких минут. Вы также можете добавить продавца в QQ {qq}. По вопросам о заказе указывайте его номер.",
    "support.ph": "Введите сообщение, например: Заказ GM... ещё не зачислен",
    "support.send": "Отправить",
    "support.err_expired": "Страница устарела — обновите её и попробуйте снова.",
    "orders.title": "Мои заказы",
    "orders.empty": "Заказов пока нет.",
    "orders.go_order": "Сделать заказ",
    "orders.no": "Номер заказа",
    "orders.product": "Товар",
    "orders.status": "Статус",
    "orders.detail": "Детали",
    "orders.pay": "Оплатить",
    "orders.cancel": "Отменить заказ",
    "orders.cancel_confirm": "Отменить этот заказ?",
    "orders.cancel_confirm2": "Отменить этот заказ? Это действие нельзя отменить.",
    "orders.delivery_title": "📦 Доставка (данные аккаунта)",
    "common.copy": "Копировать",
    "orders.gemini_qq_pre": "QQ для помощи с пополнением:",
    "orders.gemini_qq_note": "(при добавлении укажите номер заказа)",
    "detail.title": "Детали заказа",
    "detail.not_found": "Заказ не найден",
    "detail.order_no": "Номер заказа",
    "detail.product": "Товар: ",
    "detail.amount": "Сумма: ",
    "detail.created": "Дата заказа: ",
    "detail.paid_at": "Дата оплаты: ",
    "detail.status": "Статус: ",
    "detail.usage": "Как пользоваться",
    "detail.delivery": "Доставка",
    "detail.delivery_keep": "Храните данные доставки в безопасности — не пересылайте их другим.",
    "detail.delivery_account": "📦 Данные аккаунта",
    "detail.copy_all": "Копировать всё",
    "detail.download_all": "Скачать данные доставки",
    "detail.view_orders": "Мои заказы",
    "detail.continue": "Продолжить покупки",
    "detail.file_suffix": "доставка",
    "hero.completed": "Заказ выполнен",
    "hero.paid": "Оплачено — продавец обрабатывает",
    "hero.unpaid": "Ожидает оплаты",
    "hero.failed": "Заказ не выполнен",
    "hero.refunded": "Заказ возвращён",
    "hero.cancelled": "Заказ отменён",
    "tip.completed": "Продавец выполнил этот заказ; данные доставки — ниже (если есть).",
    "tip.paid": "Оплата подтверждена. Продавец обрабатывает заказы в порядке очереди; данные доставки появятся на этой странице по готовности.",
    "tip.unpaid": "Продавец начнёт обработку только после завершения оплаты.",
    "tip.failed": "Обработать этот заказ не удалось. По послепродажным вопросам свяжитесь с продавцом в QQ, указав номер заказа.",
    "tip.refunded": "По этому заказу выполнен возврат. Есть вопросы? Свяжитесь с продавцом.",
    "tip.cancelled": "Этот заказ отменён и не будет обработан. Если товар всё ещё нужен, оформите новый заказ.",
    "track.title": "Отследить заказ",
    "track.intro": "Регистрация и вход не нужны: введите <b>номер заказа</b>, полученный после оформления, и <b>контактные данные</b>, которые вы указывали (должны совпадать в точности), чтобы увидеть статус и доставку заказа.",
    "track.order_no": "Номер заказа",
    "track.order_no_ph": "Номер заказа, показанный после оформления",
    "track.contact": "Контактные данные",
    "track.contact_ph": "Контактные данные, указанные при заказе",
    "track.submit": "Найти заказ",
    "track.alt_pre": "Зарегистрированные пользователи также могут ",
    "track.alt_login": "войти",
    "track.alt_mid": " и проверить раздел «Мои заказы». Всё равно не находится? Добавьте продавца в QQ ",
    "track.alt_post": ", указав номер заказа.",
    "order.title": "Заказ",
    "order.soldout_title": "Нет в наличии",
    "order.soldout_body": "😔 Этот товар только что закончился. Он вернётся, как только продавец пополнит запас.",
    "order.soldout_hint": "Нужно срочно? Добавьте продавца в QQ {qq} или сначала посмотрите другие товары.",
    "order.back_home": "← На главную к другим товарам",
    "order.stock_hint": "🔥 Осталось всего {n} — один экземпляр будет зарезервирован за вами сразу после оплаты.",
    "order.required": "*обязательно",
    "order.aux_label": "Резервный e-mail",
    "order.aux_hint": "Нужен, если при пополнении потребуется подтверждение. Обязателен и должен быть в верном формате.",
    "order.contact_label": "Контактные данные",
    "order.contact_ph": "WeChat / телефон / QQ, чтобы продавец мог с вами связаться",
    "order.submit": "Оформить заказ и оплатить",
    "order.after_sale_pre": "Послепродажное обслуживание: полный возврат до доставки; если доставленный аккаунт не входит, сразу свяжитесь с продавцом. Полные правила — в ",
    "order.after_sale_post": ".",
    "order.one_time": "разовый платёж",
    "order.member_line": "👑 Привилегия уровня {name}: {label}, вы экономите ¥{off} на этом заказе",
    "order.err_expired": "Страница устарела — обновите её и попробуйте снова",
    "order.err_soldout": "Этот товар закончился",
    "order.err_aux_required": "Резервный e-mail обязателен и не может быть пустым",
    "order.err_aux_format": "Неверный формат резервного e-mail",
    "order.err_contact_required": "Контактные данные обязательны",
    "trust.sold": "Продано заказов: {n}",
    "trust.avg_min": "Средняя доставка ≈ {n} мин",
    "trust.avg_hour": "Средняя доставка ≈ {n} ч",
    "trust.nopass": "Мы никогда не просим пароль от вашего аккаунта",
    "auth.register": "Регистрация",
    "auth.register_sub": "Создайте аккаунт и сразу начните заказывать",
    "auth.email": "E-mail",
    "auth.password_rule": "Пароль (не менее 8 символов)",
    "auth.password_set_ph": "Придумайте пароль",
    "auth.have_account": "Уже есть аккаунт?",
    "auth.go_login": "Войти",
    "auth.login": "Вход",
    "auth.login_sub": "Войдите, чтобы заказывать и отслеживать заказы в любое время",
    "auth.password": "Пароль",
    "auth.password_ph": "Введите пароль",
    "auth.no_account": "Ещё нет аккаунта?",
    "auth.register_now": "Зарегистрироваться",
    "auth.forgot": "Забыли пароль",
    "auth.track_hint": "Заказывали без регистрации? Используйте номер заказа + контактные данные для",
    "auth.track_link": "гостевого отслеживания заказа",
    "auth.err_email": "Неверный формат e-mail",
    "auth.err_pw_short": "Пароль должен содержать не менее 8 символов",
    "auth.err_email_taken": "Этот e-mail уже зарегистрирован — просто войдите",
    "auth.err_login": "Неверный e-mail или пароль",
}

PRODUCTS_PT = {
    "gemini-pro-24m": {
        "name": "Recarga Gemini Pro por 24 meses",
        "points": [
            "Recarga feita na sua própria conta Google, com 24 meses de assinatura",
            "Não é preciso informar a senha da conta — apenas o e-mail de recarga e um e-mail reserva",
            "Aceita Alipay",
            "Recarga manual após o pagamento; acompanhe o andamento em Meus pedidos",
        ],
        "desc": "Serviço de recarga da assinatura Gemini Pro, por 24 meses. Após o pagamento, o vendedor faz a recarga manualmente na conta Google que você informar — a senha da conta nunca é solicitada.",
        "first_label": "E-mail da conta Google a recarregar",
        "password_hint": "Nunca pediremos a senha da sua conta Google em nenhuma etapa.",
        "first_err": "O e-mail da conta Google a recarregar não está em um formato de e-mail válido",
    },
    "muse-account-1b": {
        "name": "Conta pronta Muse · 1 bilhão de tokens",
        "points": [
            "Conta pronta para uso com 1 bilhão de tokens de utilização",
            "Em linguagem simples: tokens ≈ a quantidade de texto que a IA lê e escreve; 1 bilhão de tokens equivale aproximadamente a centenas de milhões de caracteres — o bastante para conversas e escrita do dia a dia por muito tempo (estimativa; o uso real depende do tamanho das conversas)",
            "Entrega manual pelo vendedor através do contato informado após o pagamento",
            "Aceita Alipay",
            "Acompanhe o andamento da entrega em Meus pedidos",
        ],
        "desc": "Conta pronta Muse com 1 bilhão de tokens. Entrega manual pelo vendedor através do contato informado.",
        "first_label": "E-mail para receber a conta",
        "password_hint": "Após o pagamento, o vendedor entrega a conta pelo contato informado — confira se ele está correto.",
        "first_err": "O formato do e-mail para receber a conta está incorreto",
    },
    "muse-2b": {
        "name": "Muse · 2 bilhões de tokens",
        "points": [
            "Conta Muse com 2 bilhões de tokens",
            "Em linguagem simples: tokens ≈ a quantidade de texto que a IA lê e escreve; 2 bilhões é o dobro de 1 bilhão e aguenta bem até o uso diário intenso (estimativa; o uso real depende do tamanho das conversas)",
            "Processado manualmente pelo vendedor após o pagamento e entregue pelo contato informado",
            "Aceita Alipay",
            "Acompanhe o andamento em Meus pedidos",
        ],
        "desc": "Muse, 2 bilhões de tokens. Processado manualmente pelo vendedor após o pagamento e entregue pelo contato informado.",
        "first_label": "E-mail de recebimento",
        "password_hint": "Após o pagamento, o vendedor faz a entrega pelo contato informado — confira se ele está correto.",
        "first_err": "O formato do e-mail de recebimento está incorreto",
    },
    "muse3-1b": {
        "name": "Muse · 31 bilhões de tokens",
        "points": [
            "Conta Muse com 31 bilhões de tokens",
            "Em linguagem simples: tokens ≈ a quantidade de texto que a IA lê e escreve; 31 bilhões é cerca de 31× o plano de 1 bilhão, feito para uso intenso e prolongado (estimativa; o uso real depende do tamanho das conversas)",
            "Processado manualmente pelo vendedor após o pagamento e entregue pelo contato informado",
            "Aceita Alipay",
            "Acompanhe o andamento em Meus pedidos",
        ],
        "desc": "Muse, 31 bilhões de tokens. Processado manualmente pelo vendedor após o pagamento e entregue pelo contato informado.",
        "first_label": "E-mail de recebimento",
        "password_hint": "Após o pagamento, o vendedor faz a entrega pelo contato informado — confira se ele está correto.",
        "first_err": "O formato do e-mail de recebimento está incorreto",
    },
    "chatgpt-go-3m": {
        "name": "ChatGPT Go 3 meses",
        "points": [
            "Conta pronta, 3 meses de assinatura ChatGPT Go",
            "Formato de entrega: e-mail | senha | chave 2FA",
            "Garantia de 3 dias",
            "Códigos 2FA: abra https://2fa.fun/ , insira a chave 2FA e clique em Obter código — os códigos são atualizados a cada 30 segundos",
            "Entrega manual pelo vendedor através do contato informado após o pagamento",
            "Aceita Alipay",
            "Acompanhe o andamento da entrega em Meus pedidos",
        ],
        "desc": "Conta pronta ChatGPT Go, 3 meses, ativada via Apple Pay. Entrega manual pelo vendedor através do contato informado.",
        "first_label": "E-mail para receber a conta",
        "password_hint": "Após o pagamento, o vendedor entrega a conta pelo contato informado — confira se ele está correto.",
        "first_err": "O formato do e-mail para receber a conta está incorreto",
    },
    "chatgpt-plus-1m-applepay": {
        "name": "ChatGPT Plus 1 mês (Apple Pay)",
        "points": [
            "Conta pronta, 1 mês de ChatGPT Plus, ativado via Apple Pay",
            "Formato de entrega: e-mail / senha / chave 2FA",
            "Garantia: cobre apenas o primeiro acesso dentro de 1 hora (garantia de primeiro acesso de 1H) — entre e verifique assim que receber",
            "Entrega manual pelo vendedor através do contato informado após o pagamento",
            "Aceita Alipay",
            "Acompanhe o andamento da entrega em Meus pedidos",
        ],
        "desc": "Conta pronta ChatGPT Plus, 1 mês, ativada via Apple Pay. Entrega manual pelo vendedor através do contato informado.",
        "first_label": "E-mail para receber a conta",
        "password_hint": "Após o pagamento, o vendedor entrega a conta pelo contato informado — confira se ele está correto.",
        "first_err": "O formato do e-mail para receber a conta está incorreto",
    },
    "grok-plus-1m": {
        "name": "Grok Plus 1 mês",
        "points": [
            "Conta pronta, 1 mês de assinatura Grok Plus",
            "Pool compartilhado de uso de IA, incluindo chat, voz, Imagine e Build do Grok",
            "Inclui acesso à API do Grok; use em grok.com",
            "Formato de entrega: e-mail + senha (ambos podem ser alterados)",
            "Não desvincule a conta do X, ou o uso pode ser afetado",
            "Este produto não tem garantia; serviços de verificação de login não são cobertos",
            "Entrega manual pelo vendedor através do contato informado após o pagamento",
            "Aceita Alipay",
            "Acompanhe o andamento da entrega em Meus pedidos",
        ],
        "desc": "Conta pronta Grok Plus, 1 mês. Entrega manual pelo vendedor através do contato informado.",
        "first_label": "E-mail para receber a conta",
        "password_hint": "Após o pagamento, o vendedor entrega a conta pelo contato informado — confira se ele está correto.",
        "first_err": "O formato do e-mail para receber a conta está incorreto",
    },
    "grok-plus-7d": {
        "name": "Grok Plus 7 dias",
        "points": [
            "Conta pronta, 7 dias de assinatura Grok Plus",
            "Garantia de 1 dia",
            "Pool compartilhado de uso de IA, incluindo chat, voz, Imagine e Build do Grok",
            "Inclui acesso à API do Grok; use em grok.com",
            "Formato de entrega: e-mail + senha (ambos podem ser alterados)",
            "Não desvincule a conta do X, ou o uso pode ser afetado",
            "Serviços de verificação de login não são cobertos pela garantia",
            "Entrega manual pelo vendedor através do contato informado após o pagamento",
            "Aceita Alipay",
            "Acompanhe o andamento da entrega em Meus pedidos",
        ],
        "desc": "Conta pronta Grok Plus, 7 dias. Entrega manual pelo vendedor através do contato informado.",
        "first_label": "E-mail para receber a conta",
        "password_hint": "Após o pagamento, o vendedor entrega a conta pelo contato informado — confira se ele está correto.",
        "first_err": "O formato do e-mail para receber a conta está incorreto",
    },
    "gmail-old-account": {
        "name": "Conta Gmail antiga (2010–2022), região aleatória",
        "points": [
            "Conta Gmail antiga, registrada entre 2010 e 2022, região atribuída aleatoriamente",
            "Formato de entrega: conta de e-mail + senha de acesso + e-mail reserva + 2FA",
            "Garantia de primeiro acesso de 24H: cobre apenas o primeiro acesso dentro de 24 horas — entre e verifique assim que receber",
            "O acesso pode exigir verificação por telefone; providencie seu próprio método de recebimento de SMS",
            "Recomenda-se uma rede estável e confiável para o acesso",
            "Entrega manual pelo vendedor através do contato informado após o pagamento",
            "Aceita Alipay",
            "Acompanhe o andamento da entrega em Meus pedidos",
        ],
        "desc": "Conta Gmail antiga, registrada entre 2010 e 2022, região aleatória. Entrega manual pelo vendedor através do contato informado.",
        "first_label": "E-mail para receber a conta",
        "password_hint": "Após o pagamento, o vendedor entrega a conta pelo contato informado — confira se ele está correto.",
        "first_err": "O formato do e-mail para receber a conta está incorreto",
    },
}

PRODUCTS_RU = {
    "gemini-pro-24m": {
        "name": "Пополнение Gemini Pro на 24 месяца",
        "points": [
            "Пополнение на ваш собственный аккаунт Google, подписка на 24 месяца",
            "Пароль от аккаунта не нужен — только e-mail для пополнения и резервный e-mail",
            "Принимается Alipay",
            "Ручное пополнение после оплаты; отслеживайте ход в «Моих заказах»",
        ],
        "desc": "Услуга пополнения подписки Gemini Pro на 24 месяца. После оплаты продавец вручную пополняет указанный вами аккаунт Google — пароль от аккаунта никогда не требуется.",
        "first_label": "E-mail аккаунта Google для пополнения",
        "password_hint": "Мы ни на одном этапе не попросим пароль от вашего аккаунта Google.",
        "first_err": "E-mail аккаунта Google для пополнения указан в неверном формате",
    },
    "muse-account-1b": {
        "name": "Готовый аккаунт Muse · 1 млрд токенов",
        "points": [
            "Готовый к использованию аккаунт с 1 млрд токенов",
            "Простыми словами: токены ≈ объём текста, который ИИ читает и пишет; 1 млрд токенов — это примерно сотни миллионов знаков, чего надолго хватит для повседневных бесед и текстов (оценка; фактический расход зависит от длины диалогов)",
            "Продавец вручную доставляет аккаунт по указанным вами контактным данным после оплаты",
            "Принимается Alipay",
            "Отслеживайте ход доставки в «Моих заказах»",
        ],
        "desc": "Готовый аккаунт Muse с 1 млрд токенов. Продавец вручную доставляет его по указанным вами контактным данным.",
        "first_label": "E-mail для получения аккаунта",
        "password_hint": "После оплаты продавец доставит аккаунт по указанным вами контактным данным — пожалуйста, убедитесь, что они верны.",
        "first_err": "Неверный формат e-mail для получения аккаунта",
    },
    "muse-2b": {
        "name": "Muse · 2 млрд токенов",
        "points": [
            "Аккаунт Muse с 2 млрд токенов",
            "Простыми словами: токены ≈ объём текста, который ИИ читает и пишет; 2 млрд — вдвое больше, чем 1 млрд, и выдерживает даже интенсивное ежедневное использование (оценка; фактический расход зависит от длины диалогов)",
            "Продавец вручную обрабатывает заказ после оплаты и доставляет по указанным вами контактным данным",
            "Принимается Alipay",
            "Отслеживайте ход в «Моих заказах»",
        ],
        "desc": "Muse, 2 млрд токенов. Продавец вручную обрабатывает заказ после оплаты и доставляет по указанным вами контактным данным.",
        "first_label": "E-mail для получения",
        "password_hint": "После оплаты продавец доставит заказ по указанным вами контактным данным — пожалуйста, убедитесь, что они верны.",
        "first_err": "Неверный формат e-mail для получения",
    },
    "muse3-1b": {
        "name": "Muse · 31 млрд токенов",
        "points": [
            "Аккаунт Muse с 31 млрд токенов",
            "Простыми словами: токены ≈ объём текста, который ИИ читает и пишет; 31 млрд — примерно в 31 раз больше плана на 1 млрд, рассчитан на длительное интенсивное использование (оценка; фактический расход зависит от длины диалогов)",
            "Продавец вручную обрабатывает заказ после оплаты и доставляет по указанным вами контактным данным",
            "Принимается Alipay",
            "Отслеживайте ход в «Моих заказах»",
        ],
        "desc": "Muse, 31 млрд токенов. Продавец вручную обрабатывает заказ после оплаты и доставляет по указанным вами контактным данным.",
        "first_label": "E-mail для получения",
        "password_hint": "После оплаты продавец доставит заказ по указанным вами контактным данным — пожалуйста, убедитесь, что они верны.",
        "first_err": "Неверный формат e-mail для получения",
    },
    "chatgpt-go-3m": {
        "name": "ChatGPT Go на 3 месяца",
        "points": [
            "Готовый аккаунт, подписка ChatGPT Go на 3 месяца",
            "Формат доставки: e-mail | пароль | секрет 2FA",
            "Гарантия 3 дня",
            "Коды 2FA: откройте https://2fa.fun/ , введите секрет 2FA и нажмите «Получить код» — коды обновляются каждые 30 секунд",
            "Продавец вручную доставляет аккаунт по указанным вами контактным данным после оплаты",
            "Принимается Alipay",
            "Отслеживайте ход доставки в «Моих заказах»",
        ],
        "desc": "Готовый аккаунт ChatGPT Go, 3 месяца, активирован через Apple Pay. Продавец вручную доставляет его по указанным вами контактным данным.",
        "first_label": "E-mail для получения аккаунта",
        "password_hint": "После оплаты продавец доставит аккаунт по указанным вами контактным данным — пожалуйста, убедитесь, что они верны.",
        "first_err": "Неверный формат e-mail для получения аккаунта",
    },
    "chatgpt-plus-1m-applepay": {
        "name": "ChatGPT Plus на 1 месяц (Apple Pay)",
        "points": [
            "Готовый аккаунт, подписка ChatGPT Plus на 1 месяц, активирована через Apple Pay",
            "Формат доставки: e-mail / пароль / секрет 2FA",
            "Гарантия: покрывает только первый вход в течение 1 часа (гарантия первого входа 1H) — войдите и проверьте сразу после получения",
            "Продавец вручную доставляет аккаунт по указанным вами контактным данным после оплаты",
            "Принимается Alipay",
            "Отслеживайте ход доставки в «Моих заказах»",
        ],
        "desc": "Готовый аккаунт ChatGPT Plus, 1 месяц, активирован через Apple Pay. Продавец вручную доставляет его по указанным вами контактным данным.",
        "first_label": "E-mail для получения аккаунта",
        "password_hint": "После оплаты продавец доставит аккаунт по указанным вами контактным данным — пожалуйста, убедитесь, что они верны.",
        "first_err": "Неверный формат e-mail для получения аккаунта",
    },
    "grok-plus-1m": {
        "name": "Grok Plus на 1 месяц",
        "points": [
            "Готовый аккаунт, подписка Grok Plus на 1 месяц",
            "Общий пул использования ИИ, включая чат, голос, Imagine и Build в Grok",
            "Включает доступ к API Grok; используйте на grok.com",
            "Формат доставки: e-mail + пароль (и то, и другое можно изменить)",
            "Не отвязывайте аккаунт от X, иначе использование может быть затронуто",
            "На этот товар гарантии нет; услуги проверки входа не покрываются",
            "Продавец вручную доставляет аккаунт по указанным вами контактным данным после оплаты",
            "Принимается Alipay",
            "Отслеживайте ход доставки в «Моих заказах»",
        ],
        "desc": "Готовый аккаунт Grok Plus, 1 месяц. Продавец вручную доставляет его по указанным вами контактным данным.",
        "first_label": "E-mail для получения аккаунта",
        "password_hint": "После оплаты продавец доставит аккаунт по указанным вами контактным данным — пожалуйста, убедитесь, что они верны.",
        "first_err": "Неверный формат e-mail для получения аккаунта",
    },
    "grok-plus-7d": {
        "name": "Grok Plus на 7 дней",
        "points": [
            "Готовый аккаунт, подписка Grok Plus на 7 дней",
            "Гарантия 1 день",
            "Общий пул использования ИИ, включая чат, голос, Imagine и Build в Grok",
            "Включает доступ к API Grok; используйте на grok.com",
            "Формат доставки: e-mail + пароль (и то, и другое можно изменить)",
            "Не отвязывайте аккаунт от X, иначе использование может быть затронуто",
            "Услуги проверки входа гарантией не покрываются",
            "Продавец вручную доставляет аккаунт по указанным вами контактным данным после оплаты",
            "Принимается Alipay",
            "Отслеживайте ход доставки в «Моих заказах»",
        ],
        "desc": "Готовый аккаунт Grok Plus, 7 дней. Продавец вручную доставляет его по указанным вами контактным данным.",
        "first_label": "E-mail для получения аккаунта",
        "password_hint": "После оплаты продавец доставит аккаунт по указанным вами контактным данным — пожалуйста, убедитесь, что они верны.",
        "first_err": "Неверный формат e-mail для получения аккаунта",
    },
    "gmail-old-account": {
        "name": "Старый аккаунт Gmail (2010–2022), случайный регион",
        "points": [
            "Старый аккаунт Gmail, зарегистрирован в 2010–2022 гг., регион назначается случайно",
            "Формат доставки: аккаунт e-mail + пароль для входа + резервный e-mail + 2FA",
            "Гарантия первого входа 24H: покрывает только первый вход в течение 24 часов — войдите и проверьте сразу после получения",
            "При входе может потребоваться подтверждение по телефону; пожалуйста, предусмотрите свой способ приёма SMS",
            "Для входа рекомендуется стабильная и надёжная сеть",
            "Продавец вручную доставляет аккаунт по указанным вами контактным данным после оплаты",
            "Принимается Alipay",
            "Отслеживайте ход доставки в «Моих заказах»",
        ],
        "desc": "Старый аккаунт Gmail, зарегистрирован в 2010–2022 гг., случайный регион. Продавец вручную доставляет его по указанным вами контактным данным.",
        "first_label": "E-mail для получения аккаунта",
        "password_hint": "После оплаты продавец доставит аккаунт по указанным вами контактным данным — пожалуйста, убедитесь, что они верны.",
        "first_err": "Неверный формат e-mail для получения аккаунта",
    },
}

BLOBS_PT = {
    "usage_muse": """<ol>
          <li>Acesse muse.ai e entre com o <b>e-mail e a senha</b> da entrega.</li>
          <li>O formato de entrega costuma ser "e-mail - senha - link de código"; se for necessário um código de verificação, abra o link de código para obtê-lo.</li>
          <li>Se aparecer "você entrou na lista de espera", geralmente é uma restrição regional — mude para um nó de rede dos <b>EUA ou do Canadá</b> e entre novamente.</li>
          <li>Algumas contas podem exigir verificação por foto do rosto; a aprovação é decidida oficialmente pela Muse.</li>
          <li>Problemas com a conta ou precisa de ajuda? Fale com o vendedor no QQ 1006025461 (informe o número do pedido).</li>
        </ol>""",
    "usage_gemini": """<ol>
          <li>Confira se o e-mail Google e o e-mail reserva informados no checkout estão corretos.</li>
          <li>Adicione o vendedor no QQ 1006025461 informando o número do pedido e colabore para concluir a recarga.</li>
          <li>Depois, confirme na página de assinaturas da sua conta Google que o Gemini Pro está ativo (24 meses).</li>
          <li>Você nunca precisa informar a senha da sua conta Google — recuse qualquer pessoa que a peça.</li>
        </ol>""",
    "usage_grok": """<ol>
          <li>Acesse grok.com e entre com o <b>e-mail e a senha</b> da entrega.</li>
          <li>Tanto o e-mail quanto a senha podem ser alterados; <b>não desvincule a conta do X</b>, ou o uso pode ser afetado.</li>
          <li>O plano de 7 dias tem garantia de 1 dia; o plano de 1 mês não tem garantia; serviços de verificação de login não são cobertos.</li>
          <li>Problemas com a conta ou precisa de ajuda? Fale com o vendedor no QQ 1006025461 (informe o número do pedido).</li>
        </ol>""",
    "usage_gmail": """<ol>
          <li>Entre no Gmail com a <b>conta de e-mail e a senha</b> da entrega; use o e-mail reserva e o 2FA quando a verificação for solicitada.</li>
          <li>Este produto é coberto apenas para o <b>primeiro acesso dentro de 24 horas</b> — entre e verifique assim que receber.</li>
          <li>Pode ser necessária verificação por telefone no acesso; providencie seu próprio método de recebimento de SMS e use uma rede estável e confiável.</li>
          <li>Problemas com a conta ou precisa de ajuda? Fale com o vendedor no QQ 1006025461 (informe o número do pedido).</li>
        </ol>""",
    "usage_openai": """<ol>
          <li>Acesse chatgpt.com e entre com o <b>e-mail e a senha</b> da entrega.</li>
          <li>Se for necessário um código de verificação, abra https://2fa.fun/ , insira a <b>chave 2FA</b> da entrega e clique em "Obter código" — os códigos são atualizados a cada 30 segundos.</li>
          <li>O plano ChatGPT Plus de 1 mês cobre apenas o <b>primeiro acesso dentro de 1 hora</b> — entre e verifique assim que receber; o plano ChatGPT Go de 3 meses tem garantia de 3 dias.</li>
          <li>Problemas com a conta ou precisa de ajuda? Fale com o vendedor no QQ 1006025461 (informe o número do pedido).</li>
        </ol>""",
    "usage_default": """<ul>
          <li>Basta seguir o conteúdo da entrega acima.</li>
          <li>Alguma dúvida? Fale com o vendedor no QQ 1006025461 informando o número do pedido.</li>
        </ul>""",
    "legal_privacy": """
        <h2>O que coletamos</h2>
        <ul>
          <li><b>Dados da conta</b>: seu e-mail de cadastro e a senha de acesso (armazenada com salt e hash — não conseguimos vê-la em texto simples).</li>
          <li><b>Dados do pedido</b>: os produtos e valores que você comprou, além do e-mail de recarga, e-mail reserva, contato e conteúdo de entrega informados na compra.</li>
          <li><b>Registros de carteira e atendimento</b>: histórico de recargas/gastos e o conteúdo das suas conversas com o atendimento.</li>
          <li><b>Registros de segurança</b>: para evitar roubo de contas e fraudes em pedidos, o sistema registra informações de segurança, como a contagem de tentativas de login malsucedidas.</li>
        </ul>
        <h2>Para que são usados</h2>
        <ul>
          <li>Processar pedidos, concluir a entrega e prestar pós-venda;</li>
          <li>Manter contas e valores em segurança;</li>
          <li>Não vendemos nem alugamos suas informações pessoais e não as usamos para perfilamento de anúncios.</li>
        </ul>
        <h2>O que nunca faremos</h2>
        <ul>
          <li>Em nenhum momento este site <b>pedirá a senha da sua conta Google ou de qualquer outra conta de terceiros</b> — não a forneça a ninguém.</li>
          <li>Os pagamentos são concluídos por plataformas de pagamento de terceiros; este site nunca toca nem armazena os dados do seu cartão bancário ou senhas de pagamento.</li>
        </ul>
        <h2>Retenção e exclusão</h2>
        <p>Os registros de pedidos são mantidos por um período para pós-venda e conciliação. Para excluir sua conta e suas informações pessoais, fale conosco pelo Atendimento ou pelo QQ do vendedor, 1006025461; faremos o processamento após confirmar sua identidade.</p>""",
    "legal_terms": """
        <h2>Natureza do serviço</h2>
        <p>Este site vende produtos digitais (serviços de recarga de assinaturas e contas prontas), entregues manualmente pelo vendedor, sem envio físico.</p>
        <h2>Pedido e pagamento</h2>
        <ul>
          <li>Preços, estoque e garantia dos produtos são os exibidos nas páginas dos produtos.</li>
          <li>O sucesso de um pagamento é determinado pelo status do pedido; se o sistema de pagamento confirmar com atraso, fale com o vendedor com o comprovante de pagamento para verificação manual — você nunca precisará pagar duas vezes.</li>
          <li>Confira se o e-mail de recarga, o contato e os demais dados estão corretos ao pedir; prejuízos causados por informações incorretas fornecidas pelo comprador são de responsabilidade do comprador. Se perceber um erro, fale com o vendedor imediatamente.</li>
        </ul>
        <h2>Garantia e reembolsos</h2>
        <ul>
          <li>Pedidos ainda não entregues podem ser reembolsados integralmente a qualquer momento, bastando falar com o vendedor.</li>
          <li>O escopo e o prazo de garantia de cada produto são os exibidos nos selos dos cards dos produtos e nas <a href="/guide">regras de pós-venda do Guia</a>, que prevalecem.</li>
          <li>Pedidos entregues fora do escopo da garantia não são reembolsáveis.</li>
        </ul>
        <h2>Observações ao comprador</h2>
        <ul>
          <li>Após receber uma conta pronta, entre e verifique-a dentro do prazo de garantia;</li>
          <li>Banimentos ou invalidações causados por você trocar a senha, emprestar a conta ou usá-la indevidamente (incluindo violar as regras da plataforma de destino) não são cobertos pela garantia.</li>
        </ul>
        <h2>Alterações destes termos</h2>
        <p>Atualizações destes termos são publicadas nesta página; continuar usando este site significa aceitá-las. Dúvidas? Fale conosco pelo Atendimento ou pelo QQ do vendedor, 1006025461.</p>""",
    "legal_cookies": """
        <h2>Quais cookies este site usa</h2>
        <ul>
          <li><b>Cookie de sessão de login (essencial)</b>: mantém você conectado após o login e faz verificações de segurança de formulários; expira quando você sai ou após seu prazo de validade.</li>
          <li>A preferência de "fechado" do anúncio da página inicial é armazenada localmente no seu navegador (localStorage) e não é enviada ao servidor.</li>
        </ul>
        <h2>O que não fazemos</h2>
        <ul>
          <li>Sem cookies de publicidade, sem rastreamento entre sites;</li>
          <li>Sem serviços de análise de terceiros ou perfilamento de usuários.</li>
        </ul>
        <h2>Páginas de terceiros</h2>
        <p>Durante o pagamento, você é redirecionado para páginas de pagamento de terceiros, como o Alipay; os cookies usados por essas páginas são regidos pelas políticas dos próprios terceiros, não por este site.</p>
        <h2>Suas escolhas</h2>
        <p>Você pode limpar ou desativar os cookies no seu navegador, mas com os cookies desativados não é possível permanecer conectado e, portanto, não é possível fazer pedidos nem visualizar pedidos.</p>""",
    "guide": '<div class="card guide"><h1>Guia de uso</h1>\n        <h2>1. Como funciona a compra</h2>\n        <ol>\n          <li><b>Cadastrar / entrar</b>: crie uma conta com seu e-mail (necessário para pedir e acompanhar pedidos).</li>\n          <li><b>Escolha um produto e peça</b>: na página inicial, clique em "Comprar agora" em um produto, preencha os dados solicitados e envie.</li>\n          <li><b>Pague</b>: no momento aceitamos <b>Alipay</b>. Após o pagamento, o pedido muda automaticamente para "Pago / Aguardando entrega" em cerca de 1 minuto.</li>\n          <li><b>Aguarde o vendedor</b>: o vendedor processa os pedidos na ordem de pagamento; acompanhe o andamento a qualquer momento em Meus pedidos.</li>\n        </ol>\n        <h2>2. Recarga Gemini Pro (precisa da sua colaboração)</h2>\n        <ol>\n          <li>No checkout, informe o <b>e-mail Google a recarregar</b> e um <b>e-mail reserva</b> — ambos devem estar corretos.</li>\n          <li>Após o pagamento, <b>adicione o vendedor no QQ (veja abaixo)</b> e informe o número do pedido ao adicionar — a recarga exige colaboração em tempo real com o vendedor.</li>\n          <li>Ao concluir, a assinatura é creditada na sua própria conta Google, por 24 meses.</li>\n        </ol>\n        <p class="hint">⚠️ Importante: você <b>nunca precisa informar a senha da sua conta Google</b> em nenhum momento. O vendedor nunca pedirá sua senha; nunca a revele a quem pedir.</p>\n        <h2>3. Contas prontas Muse (é só aguardar a entrega)</h2>\n        <ol>\n          <li>No checkout, basta informar seu <b>contato</b> para o vendedor falar com você.</li>\n          <li>Após o pagamento, o vendedor envia a <b>conta e a senha para o seu pedido</b>: abra Meus pedidos e encontre-as na seção "Entrega" do pedido — um clique para copiar.</li>\n          <li>Ao receber, entre em muse.ai sem demora para confirmar que a conta funciona e guarde os dados em segurança.</li>\n          <li>"Tokens" ≈ a quantidade de texto que a IA lê e escreve: 100 milhões de tokens equivalem aproximadamente a dezenas de milhões de caracteres, e 1 bilhão de tokens dura muito tempo para conversas e escrita do dia a dia (estimativas; o uso real depende do tamanho das conversas).</li>\n        </ol>\n        <h2>4. Pagamento e pós-venda</h2>\n        <ul>\n          <li>Se o status do pedido não atualizar por muito tempo após o pagamento (mais de 10 minutos), fale com o vendedor no QQ informando o número do pedido.</li>\n          <li>Todos os status dos pedidos são os exibidos na página Meus pedidos.</li>\n        </ul>\n        <h2>Regras de pós-venda e reembolso (compre com confiança)</h2>\n        <ul>\n          <li><b>Reembolso antes da entrega</b>: a qualquer momento antes da entrega do pedido (marcado como "Concluído"), fale com o vendedor para cancelar e receber um <b>reembolso total</b>.</li>\n          <li><b>Como o reembolso chega</b>: para pedidos pagos com saldo, o reembolso retorna instantânea e automaticamente ao seu saldo no site; para pedidos pagos com Alipay, o vendedor reembolsa via Alipay pela via original de pagamento.</li>\n          <li><b>Recargas Gemini</b>: se a recarga falhar por motivos do vendedor, reembolso total; se um e-mail incorreto informado por você causar uma recarga em conta errada, fale com o vendedor imediatamente para verificar e resolver; assinaturas já creditadas com sucesso não são reembolsáveis sem motivo.</li>\n          <li><b>Contas prontas Muse</b>: primeiro login garantido — entre e verifique logo após a entrega; se o primeiro login falhar, fale com o vendedor imediatamente (com o número do pedido) — após a verificação, faremos a troca ou o reembolso; após o primeiro login bem-sucedido, problemas posteriores da conta (incluindo troca de senha feita por você ou mau uso) não são cobertos.</li>\n          <li>Todo o pós-venda é feito pelo <b>Atendimento</b> ou pelo QQ do vendedor (veja abaixo) — inclua o número do pedido.</li>\n        </ul>\n        <h2>5. Recargas de carteira e atendimento</h2>\n        <ul>\n          <li><b>Recarga</b>: em Minha carteira, você pode recarregar antecipadamente via Alipay; depois, os pedidos podem ser pagos diretamente com o saldo, sem redirecionamento ao Alipay a cada vez.</li>\n          <li><b>Atendimento</b>: o item "Atendimento" na navegação superior permite enviar mensagens diretamente ao vendedor; quando ele responder, um selo vermelho com número aparece na navegação.</li>\n          <li>Se um pedido pago com saldo for reembolsado, o valor retorna automaticamente ao seu saldo.</li>\n        </ul>\n        </div>',
}

BLOBS_RU = {
    "usage_muse": """<ol>
          <li>Перейдите на muse.ai и войдите, используя <b>e-mail и пароль</b> из доставки.</li>
          <li>Формат доставки обычно такой: «e-mail - пароль - ссылка для кода»; если потребуется код подтверждения, откройте ссылку для кода, чтобы получить его.</li>
          <li>Если вы видите сообщение «вы присоединились к списку ожидания», это обычно региональное ограничение — переключитесь на сетевой узел <b>США или Канады</b> и войдите снова.</li>
          <li>Для некоторых аккаунтов может потребоваться подтверждение по фотографии лица; решение о прохождении принимает официально Muse.</li>
          <li>Проблемы с аккаунтом или нужна помощь? Свяжитесь с продавцом в QQ 1006025461 (укажите номер заказа).</li>
        </ol>""",
    "usage_gemini": """<ol>
          <li>Убедитесь, что e-mail Google и резервный e-mail, указанные при оформлении, верны.</li>
          <li>Добавьте продавца в QQ 1006025461, укажите номер заказа и содействуйте завершению пополнения.</li>
          <li>После этого проверьте на странице подписок вашего аккаунта Google, что Gemini Pro активен (24 месяца).</li>
          <li>Вам никогда не нужно сообщать пароль от вашего аккаунта Google — отказывайте всем, кто его просит.</li>
        </ol>""",
    "usage_grok": """<ol>
          <li>Перейдите на grok.com и войдите, используя <b>e-mail и пароль</b> из доставки.</li>
          <li>И e-mail, и пароль можно изменить; <b>не отвязывайте аккаунт от X</b>, иначе использование может быть затронуто.</li>
          <li>У плана на 7 дней гарантия 1 день; у плана на 1 месяц гарантии нет; услуги проверки входа не покрываются.</li>
          <li>Проблемы с аккаунтом или нужна помощь? Свяжитесь с продавцом в QQ 1006025461 (укажите номер заказа).</li>
        </ol>""",
    "usage_gmail": """<ol>
          <li>Войдите в Gmail, используя <b>аккаунт e-mail и пароль</b> из доставки; при необходимости подтверждения используйте резервный e-mail и 2FA.</li>
          <li>Этот товар покрывается только для <b>первого входа в течение 24 часов</b> — войдите и проверьте сразу после получения.</li>
          <li>При входе может потребоваться подтверждение по телефону; пожалуйста, предусмотрите свой способ приёма SMS и используйте стабильную, надёжную сеть.</li>
          <li>Проблемы с аккаунтом или нужна помощь? Свяжитесь с продавцом в QQ 1006025461 (укажите номер заказа).</li>
        </ol>""",
    "usage_openai": """<ol>
          <li>Перейдите на chatgpt.com и войдите, используя <b>e-mail и пароль</b> из доставки.</li>
          <li>Если потребуется код подтверждения, откройте https://2fa.fun/ , введите <b>секрет 2FA</b> из доставки и нажмите «Получить код» — коды обновляются каждые 30 секунд.</li>
          <li>План ChatGPT Plus на 1 месяц покрывает только <b>первый вход в течение 1 часа</b> — войдите и проверьте сразу после получения; у плана ChatGPT Go на 3 месяца гарантия 3 дня.</li>
          <li>Проблемы с аккаунтом или нужна помощь? Свяжитесь с продавцом в QQ 1006025461 (укажите номер заказа).</li>
        </ol>""",
    "usage_default": """<ul>
          <li>Просто следуйте данным доставки выше.</li>
          <li>Есть вопросы? Свяжитесь с продавцом в QQ 1006025461, указав номер заказа.</li>
        </ul>""",
    "legal_privacy": """
        <h2>Что мы собираем</h2>
        <ul>
          <li><b>Данные аккаунта</b>: ваш зарегистрированный e-mail и пароль для входа (хранится с солью и в виде хэша — мы не видим его в открытом виде).</li>
          <li><b>Данные заказа</b>: купленные вами товары и суммы, а также e-mail для пополнения, резервный e-mail, контактные данные и данные доставки, указанные при заказе.</li>
          <li><b>Записи кошелька и поддержки</b>: история пополнений и трат, а также содержание ваших обращений в поддержку.</li>
          <li><b>Записи безопасности</b>: для предотвращения кражи аккаунтов и мошенничества с заказами система записывает сведения безопасности, например количество неудачных попыток входа.</li>
        </ul>
        <h2>Для чего это используется</h2>
        <ul>
          <li>Обработка заказов, завершение доставки и послепродажное обслуживание;</li>
          <li>Обеспечение безопасности аккаунтов и средств;</li>
          <li>Мы не продаём и не сдаём в аренду вашу личную информацию и не используем её для рекламного профилирования.</li>
        </ul>
        <h2>Чего мы никогда не делаем</h2>
        <ul>
          <li>Этот сайт ни при каких обстоятельствах не <b>попросит пароль от вашего аккаунта Google или любого другого стороннего аккаунта</b> — не сообщайте его никому.</li>
          <li>Платежи проводятся через сторонние платёжные платформы; этот сайт никогда не получает и не хранит данные вашей банковской карты или платёжные пароли.</li>
        </ul>
        <h2>Хранение и удаление</h2>
        <p>Записи заказов хранятся в течение некоторого времени для послепродажного обслуживания и сверок. Чтобы удалить ваш аккаунт и личную информацию, свяжитесь с нами через Поддержку или QQ продавца 1006025461; мы обработаем запрос после подтверждения вашей личности.</p>""",
    "legal_terms": """
        <h2>Характер услуги</h2>
        <p>Этот сайт продаёт цифровые товары (услуги пополнения подписок и готовые аккаунты), которые продавец доставляет вручную, без физической отправки.</p>
        <h2>Заказ и оплата</h2>
        <ul>
          <li>Цены, наличие и гарантия товаров указаны на страницах товаров.</li>
          <li>Успешность платежа определяется статусом заказа; если платёжная система подтвердит платёж с задержкой, свяжитесь с продавцом, предоставив подтверждение оплаты, для ручной проверки — вас никогда не попросят платить дважды.</li>
          <li>Пожалуйста, при заказе убедитесь, что e-mail для пополнения, контактные данные и прочие сведения верны; убытки, вызванные неверной информацией от покупателя, несёт покупатель. Если вы заметили ошибку, немедленно свяжитесь с продавцом.</li>
        </ul>
        <h2>Гарантия и возвраты</h2>
        <ul>
          <li>Заказы, ещё не доставленные, можно в любое время полностью вернуть, связавшись с продавцом.</li>
          <li>Объём и срок гарантии каждого товара указаны на значках карточек товаров и в <a href="/guide">правилах послепродажного обслуживания в Инструкции</a>, которые имеют преимущественную силу.</li>
          <li>Доставленные заказы вне объёма гарантии возврату не подлежат.</li>
        </ul>
        <h2>Примечания для покупателя</h2>
        <ul>
          <li>Получив готовый аккаунт, пожалуйста, войдите и проверьте его в течение гарантийного срока;</li>
          <li>Блокировки или потеря действительности, вызванные самостоятельной сменой пароля, передачей аккаунта другим или ненадлежащим использованием (включая нарушение правил целевой платформы), гарантией не покрываются.</li>
        </ul>
        <h2>Изменения этих условий</h2>
        <p>Обновления этих условий публикуются на этой странице; продолжение использования сайта означает согласие с ними. Есть вопросы? Свяжитесь с нами через Поддержку или QQ продавца 1006025461.</p>""",
    "legal_cookies": """
        <h2>Какие cookies использует этот сайт</h2>
        <ul>
          <li><b>Cookie сессии входа (обязательный)</b>: сохраняет ваш вход после авторизации и выполняет проверки безопасности форм; срок его действия истекает при выходе или по окончании времени жизни.</li>
          <li>Настройка «закрыто» для объявления на главной странице хранится локально в вашем браузере (localStorage) и не отправляется на сервер.</li>
        </ul>
        <h2>Чего мы не делаем</h2>
        <ul>
          <li>Никаких рекламных cookies и межсайтового отслеживания;</li>
          <li>Никаких сторонних сервисов аналитики или профилирования пользователей.</li>
        </ul>
        <h2>Сторонние страницы</h2>
        <p>Во время оплаты вы перенаправляетесь на сторонние платёжные страницы, например Alipay; cookies, используемые этими страницами, регулируются собственными политиками третьих сторон, а не этого сайта.</p>
        <h2>Ваш выбор</h2>
        <p>Вы можете очистить или отключить cookies в браузере, но при отключённых cookies вы не сможете оставаться в системе, а значит — не сможете оформлять заказы и просматривать их.</p>""",
    "guide": '<div class="card guide"><h1>Инструкция</h1>\n        <h2>1. Как проходит покупка</h2>\n        <ol>\n          <li><b>Регистрация / вход</b>: создайте аккаунт с вашим e-mail (нужен для оформления и отслеживания заказов).</li>\n          <li><b>Выберите товар и закажите</b>: на главной странице нажмите «Купить» у товара, заполните данные по подсказкам и отправьте.</li>\n          <li><b>Оплата</b>: сейчас мы принимаем <b>Alipay</b>. После успешной оплаты статус заказа примерно за 1 минуту автоматически изменится на «Оплачено / Ожидает доставки».</li>\n          <li><b>Ожидайте продавца</b>: продавец обрабатывает заказы в порядке оплаты; ход можно отслеживать в «Моих заказах» в любое время.</li>\n        </ol>\n        <h2>2. Пополнение Gemini Pro (нужно ваше участие)</h2>\n        <ol>\n          <li>При оформлении укажите <b>e-mail Google для пополнения</b> и <b>резервный e-mail</b> — оба должны быть верны.</li>\n          <li>После оплаты, пожалуйста, <b>добавьте продавца в QQ (см. ниже)</b> и при добавлении укажите номер заказа — пополнение требует взаимодействия с продавцом в реальном времени.</li>\n          <li>По завершении подписка будет зачислена на ваш собственный аккаунт Google сроком на 24 месяца.</li>\n        </ol>\n        <p class="hint">⚠️ Важно: вам <b>никогда не нужно сообщать пароль от вашего аккаунта Google</b>. Продавец никогда его не попросит; не сообщайте его никому, кто просит.</p>\n        <h2>3. Готовые аккаунты Muse (просто дождитесь доставки)</h2>\n        <ol>\n          <li>При оформлении достаточно указать ваши <b>контактные данные</b>, чтобы продавец мог с вами связаться.</li>\n          <li>После оплаты продавец отправит <b>аккаунт и пароль прямо в ваш заказ</b>: откройте «Мои заказы» и найдите их в разделе «Доставка» заказа — копирование в один клик.</li>\n          <li>Получив аккаунт, сразу войдите на muse.ai, чтобы убедиться, что он работает, и храните данные в безопасности.</li>\n          <li>«Токены» ≈ объём текста, который ИИ читает и пишет: 100 млн токенов — это примерно десятки миллионов знаков, а 1 млрд токенов надолго хватает для повседневных бесед и текстов (оценки; фактический расход зависит от длины диалогов).</li>\n        </ol>\n        <h2>4. Оплата и послепродажное обслуживание</h2>\n        <ul>\n          <li>Если статус заказа долго не обновляется после оплаты (более 10 минут), свяжитесь с продавцом в QQ, указав номер заказа.</li>\n          <li>Все статусы заказов указаны на странице «Мои заказы».</li>\n        </ul>\n        <h2>Правила послепродажного обслуживания и возврата (покупайте с уверенностью)</h2>\n        <ul>\n          <li><b>Возврат до доставки</b>: в любое время до доставки заказа (статус «Выполнено») свяжитесь с продавцом, чтобы отменить заказ и получить <b>полный возврат</b>.</li>\n          <li><b>Как поступает возврат</b>: для заказов, оплаченных с баланса, возврат мгновенно и автоматически возвращается на ваш баланс на сайте; для заказов, оплаченных через Alipay, продавец возвращает средства через Alipay по исходному маршруту платежа.</li>\n          <li><b>Пополнения Gemini</b>: если пополнение не удалось по причинам на стороне продавца — полный возврат; если указанный вами неверный e-mail привёл к пополнению не того аккаунта, немедленно свяжитесь с продавцом для проверки и решения; успешно зачисленные подписки возврату без оснований не подлежат.</li>\n          <li><b>Готовые аккаунты Muse</b>: гарантия первого входа — пожалуйста, выполните первый вход и проверьте аккаунт сразу после доставки; если первый вход не удаётся, немедленно свяжитесь с продавцом (указав номер заказа) — после проверки мы заменим аккаунт или вернём деньги; после успешного первого входа последующие проблемы с аккаунтом (включая самостоятельную смену пароля или ненадлежащее использование) гарантией не покрываются.</li>\n          <li>Всё послепродажное обслуживание ведётся через <b>Поддержку</b> или QQ продавца (см. ниже) — пожалуйста, указывайте номер заказа.</li>\n        </ul>\n        <h2>5. Пополнение кошелька и поддержка</h2>\n        <ul>\n          <li><b>Пополнение</b>: в «Моём кошельке» вы можете заранее пополнить баланс через Alipay; затем заказы можно будет оплачивать напрямую с баланса, без перехода в Alipay каждый раз.</li>\n          <li><b>Поддержка</b>: пункт «Поддержка» в верхней навигации позволяет писать продавцу напрямую; после его ответа в навигации появится красный значок с числом.</li>\n          <li>Если по заказу, оплаченному с баланса, выполнен возврат, сумма автоматически возвращается на ваш баланс.</li>\n        </ul>\n        </div>',
}

WARRANTY_PT = {
    "gemini-pro-24m": "🛡 Reembolso total se a recarga falhar",
    "muse-account-1b": "🛡 Primeiro login garantido",
    "muse-2b": "🛡 Primeiro login garantido",
    "muse3-1b": "🛡 Primeiro login garantido",
    "chatgpt-go-3m": "🛡 Garantia de 3 dias",
    "chatgpt-plus-1m-applepay": "🛡 Garantia de 1 hora · primeiro acesso",
    "grok-plus-1m": None,
    "grok-plus-7d": "🛡 Garantia de 1 dia",
    "gmail-old-account": "🛡 Garantia de 24 horas · primeiro acesso",
}
WARRANTY_RU = {
    "gemini-pro-24m": "🛡 Полный возврат, если пополнение не удастся",
    "muse-account-1b": "🛡 Гарантия первого входа",
    "muse-2b": "🛡 Гарантия первого входа",
    "muse3-1b": "🛡 Гарантия первого входа",
    "chatgpt-go-3m": "🛡 Гарантия 3 дня",
    "chatgpt-plus-1m-applepay": "🛡 Гарантия 1 час · первый вход",
    "grok-plus-1m": None,
    "grok-plus-7d": "🛡 Гарантия 1 день",
    "gmail-old-account": "🛡 Гарантия 24 часа · первый вход",
}

CAT_PT = {"gemini": "Gemini", "muse": "Muse", "openai": "OpenAI",
          "grok": "Grok", "gmail": "Gmail"}
CAT_RU = {"gemini": "Gemini", "muse": "Muse", "openai": "OpenAI",
          "grok": "Grok", "gmail": "Gmail"}

ANN_PT = [
    ("🎉 Bônus de primeira recarga: primeira recarga da carteira de ¥10 ou mais ganha ¥2 grátis; de ¥15 ou mais, ¥5 grátis — veja Minha carteira →", "/wallet"),
    ("🛡 Proteção ao comprador: reembolso total antes da entrega; veja o selo de garantia de cada produto e o Guia →", "/guide"),
    ("💬 Entrega manual: o vendedor processa os pedidos manualmente após o pagamento; acompanhe em Meus pedidos ou fale com o Atendimento →", "/support"),
]
ANN_RU = [
    ("🎉 Бонус за первое пополнение: при первом пополнении кошелька от ¥10 — ¥2 в подарок, от ¥15 — ¥5 в подарок. Подробнее в «Моём кошельке» →", "/wallet"),
    ("🛡 Защита покупателя: полный возврат до доставки; см. значок гарантии у каждого товара и Инструкцию →", "/guide"),
    ("💬 Ручная доставка: продавец обрабатывает заказы вручную после оплаты; отслеживайте ход в «Моих заказах» или обратитесь в Поддержку →", "/support"),
]

LEVEL_PT = [("Padrão", ""), ("Prata", "2% de desconto"),
            ("Ouro", "5% de desconto"), ("Platina", "8% de desconto"),
            ("Ouro Negro", "12% de desconto")]
LEVEL_RU = [("Обычный", ""), ("Серебряный", "скидка 2%"),
            ("Золотой", "скидка 5%"), ("Платиновый", "скидка 8%"),
            ("Чёрное золото", "скидка 12%")]

STRINGS_PT.update({
    "hero.tagline": "As principais assinaturas de IA em um só lugar — recargas e contas prontas",
    "hero.cta": "Ver produtos",
})
STRINGS_RU.update({
    "hero.tagline": "Главные ИИ-подписки в одном месте — пополнение и готовые аккаунты",
    "hero.cta": "Смотреть товары",
})
