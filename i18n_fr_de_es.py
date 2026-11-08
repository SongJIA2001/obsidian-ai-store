# -*- coding: utf-8 -*-
"""muse798.com 多语言译文（upgrade19）：法语 fr / 德语 de / 西班牙语 es。

由 i18n.merge_extra() 合并：变量后缀 = 语言代码大写。
简体中文为源语言，英文为参考；本文件按英文参考逐项翻译，
语气为礼貌形（fr vous / de Sie / es usted）。
"""

STRINGS_FR = {
    "nav.home": "Accueil", "nav.order": "Commander",
    "nav.my_orders": "Mes commandes", "nav.wallet": "Mon portefeuille",
    "nav.support": "Service client", "nav.guide": "Guide d'utilisation",
    "nav.admin": "Administration vendeur", "nav.logout": "Se déconnecter",
    "nav.login": "Se connecter", "nav.register": "S'inscrire",
    "nav.track": "Suivi de commande",
    "footer.tag": "Services numériques uniquement, aucun envoi physique",
    "footer.privacy": "Politique de confidentialité",
    "footer.terms": "Conditions d'utilisation",
    "footer.cookies": "Politique relative aux cookies",
    "home.search_ph": "Rechercher un produit",
    "home.all": "Tous",
    "home.buy": "Acheter →", "home.soldout": "Épuisé",
    "home.sold_n": "{n} vendus",
    "home.stock_n": "{n} en stock",
    "home.stock_low": "🔥 Plus que {n} en stock",
    "home.stock_plenty": "En stock",
    "home.no_match": "Aucun produit correspondant",
    "common.yuan": "¥",
    "status.unpaid": "En attente de paiement",
    "status.paid": "Payé / En attente de livraison",
    "status.completed": "Terminé (livré)",
    "status.failed": "Échoué",
    "status.refunded": "Remboursé",
    "status.cancelled": "Annulé",
    "home.title": "Tous les produits",
    "track.err_notfound": "Numéro de commande ou coordonnées incorrects — veuillez vérifier et réessayer",
    "track.result_title": "Résultat de la recherche de commande",
    "track.more": "Nouvelle recherche",
    "chat.me": "Moi",
    "chat.seller": "Vendeur",
    "chat.customer": "Client",
    "chat.empty": "Aucun message pour le moment. Laissez un message ci-dessous, le vendeur vous répondra dès qu'il le verra.",
    "lock.msg": "Trop de tentatives — veuillez réessayer dans {m} min",
    "guide.contact": "Contacter le vendeur",
    "guide.contact_hint": "Le vendeur est généralement disponible pendant les heures de travail. Indiquez votre numéro de commande dans vos messages pour un traitement plus rapide.",
    "legal.privacy_title": "Politique de confidentialité",
    "legal.terms_title": "Conditions d'utilisation",
    "legal.cookies_title": "Politique relative aux cookies",
    "legal.updated": "Dernière mise à jour : 08/11/2026 · S'applique à muse798.com (OBSIDIAN AI)",
    "legal.contact_pre": "Contact : ",
    "legal.contact_post": " ou le vendeur sur QQ {qq}.",
    "rpay.result_title": "Résultat de la recharge",
    "rpay.credited": "Crédité",
    "rpay.confirming": "En cours de confirmation",
    "rpay.tip_credited": "Votre recharge a été créditée — vérifiez votre solde dans Mon portefeuille.",
    "rpay.tip_confirming": "Votre paiement est encore en cours de confirmation — veuillez actualiser Mon portefeuille dans un instant.",
    "pay.title": "Payer la commande",
    "pay.order_no": "N° de commande : ",
    "pay.product": "Produit : ",
    "pay.amount": "Montant dû : ",
    "pay.balance_btn": "Payer avec le solde (solde ¥{b})",
    "pay.balance_low_pre": "Votre solde est de ¥{b}, ce qui ne suffit pas pour cette commande. Vous pouvez ",
    "pay.goto_recharge": "recharger d'abord",
    "pay.balance_low_post": ".",
    "pay.balance_zero_pre": "Votre solde est de ¥0,00. Vous pouvez ",
    "pay.recharge_word": "recharger",
    "pay.balance_zero_post": " puis payer directement avec votre solde.",
    "pay.epay_btn": "Payer avec Alipay",
    "pay.note": "Après le paiement, la commande devient automatiquement « Payé / En attente de livraison » et le vendeur la traitera à son tour. Tant que le paiement n'est pas terminé, la commande reste impayée et rien n'est débité.",
    "pay.status_title": "Statut de la commande",
    "pay.status_amount": "Montant : ",
    "pay.status_now": "Statut : ",
    "pay.tip_paid": "Paiement confirmé. Le vendeur traitera votre commande à son tour.",
    "pay.tip_unpaid": "Le résultat de votre paiement est encore en cours de confirmation (la notification asynchrone de la plateforme de paiement fait foi). Veuillez actualiser Mes commandes dans un instant. Si le paiement n'a pas été terminé, la commande reste impayée et rien n'est débité.",
    "pay.tip_other": "Le statut de la commande est indiqué ci-dessus. Des questions ? Contactez le vendeur.",
    "pay.view_detail": "Voir les détails de la commande",
    "wallet.title": "Mon portefeuille",
    "wallet.balance_label": "Solde actuel",
    "wallet.custom_label": "Ou saisissez un montant personnalisé (CNY)",
    "wallet.custom_ph": "ex. 30",
    "wallet.recharge_btn": "Recharger avec Alipay",
    "wallet.note": "Rechargez via Alipay ; une fois le montant crédité, vous pourrez payer vos commandes directement avec votre solde. Recharge unique de ¥1 à ¥5 000. Le solde ne peut pas être retiré ; les remboursements des commandes payées avec le solde sont automatiquement recrédités sur votre solde.",
    "wallet.bonus_banner": "🎁 <b>Offre de première recharge</b> : première recharge de ¥10 ou plus créditée <b>¥12</b> ; ¥15 ou plus créditée <b>¥20</b>. Le bonus est crédité automatiquement avec le montant principal. Une fois par personne.",
    "wallet.paid_badge": "Crédité",
    "wallet.unpaid_link": "Impayé · Payer maintenant",
    "wallet.bonus_incl": "Bonus de première recharge de ¥{b} inclus ; ¥{t} crédités au total",
    "wallet.no_recharges": "Aucune recharge pour le moment",
    "wallet.no_logs": "Aucune transaction pour le moment",
    "wallet.records": "Historique des recharges",
    "wallet.rc_no": "N° de recharge",
    "wallet.amount": "Montant",
    "wallet.status": "Statut",
    "wallet.time": "Date",
    "wallet.logs": "Transactions",
    "wallet.type": "Type",
    "wallet.change": "Variation",
    "wallet.balance": "Solde",
    "wallet.note_col": "Note",
    "wallet.member_title": "👑 Niveau de membre",
    "wallet.member_now": "Niveau actuel : <b>{name}</b> ({n} niveaux au total ; les remises s'appliquent automatiquement lors de la commande)",
    "wallet.lv_current": "Actuel",
    "wallet.lv_next": "Suivant",
    "wallet.lv_member": "Membre",
    "wallet.lv_disc_all": "{label} sur tout le site",
    "wallet.lv_disc_default": "Niveau par défaut",
    "wallet.lv_req": "Passage automatique à ¥{s} dépensés ou ¥{r} rechargés",
    "wallet.lv_manual": "Votre niveau a été défini manuellement par le vendeur 🎁 (progression automatique : ¥{s} dépensés · ¥{r} rechargés)",
    "wallet.lv_progress": "Total dépensé ¥{s} · total rechargé ¥{r} ; pour atteindre {name} : encore ¥{ds} de dépenses ou ¥{dr} de recharges",
    "wallet.lv_max": "Total dépensé ¥{s} · total rechargé ¥{r} ; vous êtes au niveau le plus élevé 🎉",
    "wallet.err_amount": "Montant de recharge invalide : veuillez saisir un montant entre ¥1 et ¥5 000.",
    "wallet.err_expired": "Cette page a expiré — veuillez l'actualiser et réessayer.",
    "kind.recharge": "Recharge en ligne",
    "kind.bonus": "Bonus de première recharge",
    "kind.pay": "Paiement par solde",
    "kind.refund": "Remboursement",
    "kind.admin": "Ajustement du vendeur",
    "rpay.title": "Paiement de la recharge",
    "rpay.no": "N° de recharge : ",
    "rpay.amount": "Montant de la recharge : ",
    "rpay.bonus_hint": "🎁 C'est votre première recharge : un bonus supplémentaire de <b>¥{b}</b> sera crédité, soit <b>¥{t}</b> au total.",
    "rpay.note": "Après un paiement réussi, votre solde est crédité automatiquement — vérifiez-le dans Mon portefeuille. En cas de léger retard, le site vérifie auprès de la plateforme de paiement chaque minute.",
    "rpay.not_found": "Recharge introuvable",
    "forgot.title": "Mot de passe oublié",
    "forgot.p1": "La récupération par e-mail en libre-service n'est pas encore disponible. Si vous avez oublié votre mot de passe, contactez le vendeur pour vérifier votre identité et le réinitialiser :",
    "forgot.li1": "Écrivez-nous via le Service client en haut de la page, ou ajoutez le vendeur sur QQ <b>{qq}</b>, et indiquez votre <b>adresse e-mail d'inscription</b> ;",
    "forgot.li2": "Après vérification, le vendeur réinitialisera votre mot de passe dans l'administration et vous enverra le nouveau ;",
    "forgot.li3_pre": "Dès réception du nouveau mot de passe, veuillez vous ",
    "forgot.li3_post": " dès que possible pour vérifier qu'il fonctionne.",
    "forgot.hint": "Remarque : le vendeur ne vous demandera jamais le mot de passe de votre compte Google. Les réinitialisations de mot de passe se font uniquement de cette manière — méfiez-vous des autres canaux.",
    "forgot.back": "Retour à la connexion",
    "qq.title": "La recharge nécessite l'aide du vendeur",
    "qq.copy": "Copier le QQ",
    "qq.note": "Merci d'indiquer votre numéro de commande lors de l'ajout. Le vendeur vous aidera à effectuer la recharge. Remarque : le vendeur ne vous demandera jamais le mot de passe de votre compte Google.",
    "qq.pre": "Veuillez ajouter le vendeur sur QQ",
    "nf.title": "Page introuvable",
    "nf.body": "La page que vous avez visitée a peut-être été déplacée, ou l'adresse a été mal saisie.",
    "nf.home": "Retour à l'accueil",
    "nf.guide": "Lire le guide",
    "support.title": "Service client",
    "support.intro": "Le vendeur répond personnellement (pas un robot), généralement en quelques minutes. Vous pouvez aussi ajouter le vendeur sur QQ {qq}. Pour les questions sur une commande, merci d'indiquer votre numéro de commande.",
    "support.ph": "Saisissez un message, ex. : commande GM… pas encore créditée",
    "support.send": "Envoyer",
    "support.err_expired": "Cette page a expiré — veuillez l'actualiser et réessayer.",
    "orders.title": "Mes commandes",
    "orders.empty": "Aucune commande pour le moment.",
    "orders.go_order": "Passer une commande",
    "orders.no": "N° de commande",
    "orders.product": "Produit",
    "orders.status": "Statut",
    "orders.detail": "Détails",
    "orders.pay": "Payer maintenant",
    "orders.cancel": "Annuler la commande",
    "orders.cancel_confirm": "Annuler cette commande ?",
    "orders.cancel_confirm2": "Annuler cette commande ? Cette action est irréversible.",
    "orders.delivery_title": "📦 Livraison (informations du compte)",
    "common.copy": "Copier",
    "orders.gemini_qq_pre": "QQ d'assistance pour la recharge :",
    "orders.gemini_qq_note": "(indiquez votre numéro de commande lors de l'ajout)",
    "detail.title": "Détails de la commande",
    "detail.not_found": "Commande introuvable",
    "detail.order_no": "N° de commande",
    "detail.product": "Produit : ",
    "detail.amount": "Montant : ",
    "detail.created": "Commandé le : ",
    "detail.paid_at": "Payé le : ",
    "detail.status": "Statut : ",
    "detail.usage": "Mode d'emploi",
    "detail.delivery": "Livraison",
    "detail.delivery_keep": "Conservez précieusement le contenu de votre livraison — ne le transmettez à personne.",
    "detail.delivery_account": "📦 Informations du compte",
    "detail.copy_all": "Tout copier",
    "detail.download_all": "Télécharger la livraison",
    "detail.view_orders": "Voir les commandes",
    "detail.continue": "Continuer mes achats",
    "detail.file_suffix": "livraison",
    "hero.completed": "Commande terminée",
    "hero.paid": "Payé — Traitement par le vendeur en cours",
    "hero.unpaid": "En attente de paiement",
    "hero.failed": "Échec de la commande",
    "hero.refunded": "Commande remboursée",
    "hero.cancelled": "Commande annulée",
    "tip.completed": "Le vendeur a terminé cette commande ; la livraison se trouve ci-dessous (le cas échéant).",
    "tip.paid": "Paiement confirmé. Le vendeur traite les commandes à tour de rôle ; la livraison apparaîtra sur cette page une fois terminée.",
    "tip.unpaid": "Le vendeur ne commence le traitement qu'une fois le paiement terminé.",
    "tip.failed": "Le traitement de cette commande a échoué. Pour le service après-vente, contactez le vendeur sur QQ en indiquant votre numéro de commande.",
    "tip.refunded": "Cette commande a été remboursée. Des questions ? Contactez le vendeur.",
    "tip.cancelled": "Cette commande a été annulée et ne sera pas traitée. Veuillez passer une nouvelle commande si vous la souhaitez toujours.",
    "track.title": "Suivi de commande",
    "track.intro": "Aucune inscription ni connexion requise : saisissez le <b>numéro de commande</b> reçu après votre commande et les <b>coordonnées</b> utilisées (elles doivent correspondre exactement) pour voir le statut de la commande et sa livraison.",
    "track.order_no": "Numéro de commande",
    "track.order_no_ph": "Le numéro de commande affiché après la commande",
    "track.contact": "Coordonnées",
    "track.contact_ph": "Les coordonnées utilisées lors de la commande",
    "track.submit": "Suivre la commande",
    "track.alt_pre": "Les utilisateurs inscrits peuvent aussi ",
    "track.alt_login": "se connecter",
    "track.alt_mid": " et consulter Mes commandes. Vous ne la trouvez toujours pas ? Ajoutez le vendeur sur QQ ",
    "track.alt_post": " en indiquant votre numéro de commande.",
    "order.title": "Commander",
    "order.soldout_title": "Épuisé",
    "order.soldout_body": "😔 Ce produit vient d'être épuisé. Il reviendra dès que le vendeur aura réassorti le stock.",
    "order.soldout_hint": "Pressé ? Ajoutez le vendeur sur QQ {qq} ou parcourez d'abord les autres produits.",
    "order.back_home": "← Retour à l'accueil pour voir d'autres produits",
    "order.stock_hint": "🔥 Plus que {n} en stock — un exemplaire vous est réservé dès que le paiement réussit.",
    "order.required": "*obligatoire",
    "order.aux_label": "E-mail de secours",
    "order.aux_hint": "Utilisé si une vérification est nécessaire pendant la recharge. Obligatoire, au format valide.",
    "order.contact_label": "Coordonnées",
    "order.contact_ph": "WeChat / téléphone / QQ, pour que le vendeur puisse vous joindre",
    "order.submit": "Valider la commande et payer",
    "order.after_sale_pre": "Service après-vente : remboursement intégral avant la livraison ; si un compte livré ne permet pas de se connecter, contactez immédiatement le vendeur. Règles complètes dans le ",
    "order.after_sale_post": ".",
    "order.one_time": "paiement unique",
    "order.member_line": "👑 Avantage {name} : {label}, vous économisez ¥{off} sur cette commande",
    "order.err_expired": "Cette page a expiré — veuillez l'actualiser et réessayer",
    "order.err_soldout": "Ce produit est épuisé",
    "order.err_aux_required": "L'e-mail de secours est obligatoire et ne peut pas être vide",
    "order.err_aux_format": "Le format de l'e-mail de secours est incorrect",
    "order.err_contact_required": "Les coordonnées sont obligatoires",
    "trust.sold": "{n} commandes vendues",
    "trust.avg_min": "Livraison moyenne ≈ {n} min",
    "trust.avg_hour": "Livraison moyenne ≈ {n} h",
    "trust.nopass": "Nous ne demandons jamais le mot de passe de votre compte",
    "auth.register": "S'inscrire",
    "auth.register_sub": "Créez un compte et commencez à commander immédiatement",
    "auth.email": "E-mail",
    "auth.password_rule": "Mot de passe (8 caractères minimum)",
    "auth.password_set_ph": "Définissez un mot de passe",
    "auth.have_account": "Vous avez déjà un compte ?",
    "auth.go_login": "Se connecter",
    "auth.login": "Se connecter",
    "auth.login_sub": "Connectez-vous pour commander et suivre vos commandes à tout moment",
    "auth.password": "Mot de passe",
    "auth.password_ph": "Saisissez votre mot de passe",
    "auth.no_account": "Pas encore de compte ?",
    "auth.register_now": "S'inscrire maintenant",
    "auth.forgot": "Mot de passe oublié",
    "auth.track_hint": "Vous avez commandé sans vous inscrire ? Utilisez votre numéro de commande + vos coordonnées pour le",
    "auth.track_link": "suivi de commande invité",
    "auth.err_email": "Format d'e-mail invalide",
    "auth.err_pw_short": "Le mot de passe doit comporter au moins 8 caractères",
    "auth.err_email_taken": "Cet e-mail est déjà enregistré — veuillez vous connecter",
    "auth.err_login": "E-mail ou mot de passe incorrect",
}

STRINGS_DE = {
    "nav.home": "Startseite", "nav.order": "Jetzt bestellen",
    "nav.my_orders": "Meine Bestellungen", "nav.wallet": "Mein Guthaben",
    "nav.support": "Kundenservice", "nav.guide": "Anleitung",
    "nav.admin": "Verkäufer-Admin", "nav.logout": "Abmelden",
    "nav.login": "Anmelden", "nav.register": "Registrieren",
    "nav.track": "Bestellung verfolgen",
    "footer.tag": "Nur digitale Dienste, kein physischer Versand",
    "footer.privacy": "Datenschutzerklärung",
    "footer.terms": "Nutzungsbedingungen",
    "footer.cookies": "Cookie-Richtlinie",
    "home.search_ph": "Produkte suchen",
    "home.all": "Alle",
    "home.buy": "Jetzt kaufen →", "home.soldout": "Ausverkauft",
    "home.sold_n": "{n} verkauft",
    "home.stock_n": "{n} auf Lager",
    "home.stock_low": "🔥 Nur noch {n} verfügbar",
    "home.stock_plenty": "Auf Lager",
    "home.no_match": "Keine passenden Produkte",
    "common.yuan": "¥",
    "status.unpaid": "Zahlung ausstehend",
    "status.paid": "Bezahlt / Lieferung ausstehend",
    "status.completed": "Abgeschlossen (geliefert)",
    "status.failed": "Fehlgeschlagen",
    "status.refunded": "Erstattet",
    "status.cancelled": "Storniert",
    "home.title": "Alle Produkte",
    "track.err_notfound": "Bestellnummer oder Kontaktdaten sind falsch — bitte prüfen und erneut versuchen",
    "track.result_title": "Ergebnis der Bestellsuche",
    "track.more": "Weitere Bestellung suchen",
    "chat.me": "Ich",
    "chat.seller": "Verkäufer",
    "chat.customer": "Kunde",
    "chat.empty": "Noch keine Nachrichten. Hinterlassen Sie unten eine Nachricht, der Verkäufer antwortet, sobald er sie sieht.",
    "lock.msg": "Zu viele Versuche — bitte in {m} Min. erneut versuchen",
    "guide.contact": "Verkäufer kontaktieren",
    "guide.contact_hint": "Der Verkäufer ist in der Regel zu den Arbeitszeiten erreichbar. Geben Sie in Nachrichten Ihre Bestellnummer an, dann geht es schneller.",
    "legal.privacy_title": "Datenschutzerklärung",
    "legal.terms_title": "Nutzungsbedingungen",
    "legal.cookies_title": "Cookie-Richtlinie",
    "legal.updated": "Zuletzt aktualisiert: 08.11.2026 · Gilt für muse798.com (OBSIDIAN AI)",
    "legal.contact_pre": "Kontakt: ",
    "legal.contact_post": " oder den Verkäufer per QQ {qq}.",
    "rpay.result_title": "Aufladeergebnis",
    "rpay.credited": "Gutgeschrieben",
    "rpay.confirming": "Wird bestätigt",
    "rpay.tip_credited": "Ihre Aufladung wurde gutgeschrieben — prüfen Sie Ihr Guthaben unter Mein Guthaben.",
    "rpay.tip_confirming": "Ihre Zahlung wird noch bestätigt — bitte aktualisieren Sie Mein Guthaben in Kürze.",
    "pay.title": "Bestellung bezahlen",
    "pay.order_no": "Bestellnr.: ",
    "pay.product": "Produkt: ",
    "pay.amount": "Zu zahlender Betrag: ",
    "pay.balance_btn": "Mit Guthaben zahlen (Guthaben ¥{b})",
    "pay.balance_low_pre": "Ihr Guthaben beträgt ¥{b} und reicht für diese Bestellung nicht aus. Sie können ",
    "pay.goto_recharge": "zuerst aufladen",
    "pay.balance_low_post": ".",
    "pay.balance_zero_pre": "Ihr Guthaben beträgt ¥0,00. Sie können ",
    "pay.recharge_word": "aufladen",
    "pay.balance_zero_post": " und dann direkt mit Guthaben zahlen.",
    "pay.epay_btn": "Mit Alipay zahlen",
    "pay.note": "Nach der Zahlung wird die Bestellung automatisch zu „Bezahlt / Lieferung ausstehend“ und der Verkäufer bearbeitet sie der Reihe nach. Bis zum Abschluss der Zahlung bleibt die Bestellung unbezahlt und es wird nichts abgebucht.",
    "pay.status_title": "Bestellstatus",
    "pay.status_amount": "Betrag: ",
    "pay.status_now": "Status: ",
    "pay.tip_paid": "Zahlung bestätigt. Der Verkäufer bearbeitet Ihre Bestellung der Reihe nach.",
    "pay.tip_unpaid": "Ihr Zahlungsergebnis wird noch bestätigt (maßgeblich ist die asynchrone Benachrichtigung der Zahlungsplattform). Bitte aktualisieren Sie Meine Bestellungen in Kürze. Wurde die Zahlung nicht abgeschlossen, bleibt die Bestellung unbezahlt und es wird nichts abgebucht.",
    "pay.tip_other": "Der Bestellstatus ist oben angezeigt. Fragen? Wenden Sie sich an den Verkäufer.",
    "pay.view_detail": "Bestelldetails ansehen",
    "wallet.title": "Mein Guthaben",
    "wallet.balance_label": "Aktuelles Guthaben",
    "wallet.custom_label": "Oder eigenen Betrag eingeben (CNY)",
    "wallet.custom_ph": "z. B. 30",
    "wallet.recharge_btn": "Mit Alipay aufladen",
    "wallet.note": "Laden Sie per Alipay auf; nach der Gutschrift können Sie Bestellungen direkt mit Ihrem Guthaben bezahlen. Einzelaufladung ¥1–¥5.000. Guthaben kann nicht ausgezahlt werden; Erstattungen für mit Guthaben bezahlte Bestellungen werden automatisch auf Ihr Guthaben zurückgebucht.",
    "wallet.bonus_banner": "🎁 <b>Erstauflade-Aktion</b>: Erste Aufladung ab ¥10 wird mit <b>¥12</b> gutgeschrieben; ab ¥15 mit <b>¥20</b>. Der Bonus wird automatisch mit dem Hauptbetrag gutgeschrieben. Einmal pro Person.",
    "wallet.paid_badge": "Gutgeschrieben",
    "wallet.unpaid_link": "Unbezahlt · Jetzt zahlen",
    "wallet.bonus_incl": "Inkl. Erstauflade-Bonus ¥{b}; insgesamt ¥{t} gutgeschrieben",
    "wallet.no_recharges": "Noch keine Aufladungen",
    "wallet.no_logs": "Noch keine Umsätze",
    "wallet.records": "Aufladeverlauf",
    "wallet.rc_no": "Aufladenr.",
    "wallet.amount": "Betrag",
    "wallet.status": "Status",
    "wallet.time": "Zeit",
    "wallet.logs": "Umsätze",
    "wallet.type": "Typ",
    "wallet.change": "Änderung",
    "wallet.balance": "Guthaben",
    "wallet.note_col": "Hinweis",
    "wallet.member_title": "👑 Mitgliedsstufe",
    "wallet.member_now": "Aktuelle Stufe: <b>{name}</b> (insgesamt {n} Stufen; Rabatte werden bei der Bestellung automatisch angewendet)",
    "wallet.lv_current": "Aktuell",
    "wallet.lv_next": "Nächste",
    "wallet.lv_member": "Mitglied",
    "wallet.lv_disc_all": "{label} im gesamten Shop",
    "wallet.lv_disc_default": "Standardstufe",
    "wallet.lv_req": "Automatischer Aufstieg bei ¥{s} Ausgaben oder ¥{r} Aufladungen",
    "wallet.lv_manual": "Ihre Stufe wurde vom Verkäufer manuell festgelegt 🎁 (automatischer Fortschritt: ¥{s} ausgegeben · ¥{r} aufgeladen)",
    "wallet.lv_progress": "Insgesamt ausgegeben ¥{s} · insgesamt aufgeladen ¥{r}; bis {name}: noch ¥{ds} Ausgaben oder ¥{dr} Aufladungen",
    "wallet.lv_max": "Insgesamt ausgegeben ¥{s} · insgesamt aufgeladen ¥{r}; Sie sind auf der höchsten Stufe 🎉",
    "wallet.err_amount": "Ungültiger Aufladebetrag: Bitte geben Sie einen Betrag zwischen ¥1 und ¥5.000 ein.",
    "wallet.err_expired": "Diese Seite ist abgelaufen — bitte aktualisieren und erneut versuchen.",
    "kind.recharge": "Online-Aufladung",
    "kind.bonus": "Erstauflade-Bonus",
    "kind.pay": "Guthabenzahlung",
    "kind.refund": "Erstattung",
    "kind.admin": "Verkäufer-Anpassung",
    "rpay.title": "Aufladung bezahlen",
    "rpay.no": "Aufladenr.: ",
    "rpay.amount": "Aufladebetrag: ",
    "rpay.bonus_hint": "🎁 Dies ist Ihre erste Aufladung: Es werden zusätzlich <b>¥{b}</b> Bonus gutgeschrieben, insgesamt <b>¥{t}</b>.",
    "rpay.note": "Nach erfolgreicher Zahlung wird Ihr Guthaben automatisch gutgeschrieben — prüfen Sie es unter Mein Guthaben. Bei leichter Verzögerung prüft die Website jede Minute bei der Zahlungsplattform nach.",
    "rpay.not_found": "Aufladung nicht gefunden",
    "forgot.title": "Passwort vergessen",
    "forgot.p1": "Eine Wiederherstellung per E-Mail in Selbstbedienung ist noch nicht verfügbar. Wenn Sie Ihr Passwort vergessen haben, wenden Sie sich an den Verkäufer, um Ihre Identität zu bestätigen und es zurücksetzen zu lassen:",
    "forgot.li1": "Schreiben Sie uns über den Kundenservice oben auf der Seite oder fügen Sie den Verkäufer per QQ <b>{qq}</b> hinzu und geben Sie Ihre <b>Registrierungs-E-Mail</b> an;",
    "forgot.li2": "Nach der Überprüfung setzt der Verkäufer Ihr Passwort im Adminbereich zurück und sendet Ihnen das neue zu;",
    "forgot.li3_pre": "Sobald Sie das neue Passwort erhalten haben, bitte ",
    "forgot.li3_post": " und so bald wie möglich prüfen, ob es funktioniert.",
    "forgot.hint": "Hinweis: Der Verkäufer wird Sie niemals nach dem Passwort Ihres Google-Kontos fragen. Passwort-Zurücksetzungen erfolgen nur auf diesem Weg — Vorsicht vor anderen Kanälen.",
    "forgot.back": "Zurück zur Anmeldung",
    "qq.title": "Für die Aufladung ist die Hilfe des Verkäufers nötig",
    "qq.copy": "QQ kopieren",
    "qq.note": "Bitte geben Sie beim Hinzufügen Ihre Bestellnummer an. Der Verkäufer hilft Ihnen, die Aufladung abzuschließen. Hinweis: Der Verkäufer wird Sie niemals nach dem Passwort Ihres Google-Kontos fragen.",
    "qq.pre": "Bitte fügen Sie den Verkäufer per QQ hinzu",
    "nf.title": "Seite nicht gefunden",
    "nf.body": "Die aufgerufene Seite wurde möglicherweise verschoben, oder die Adresse wurde falsch eingegeben.",
    "nf.home": "Zurück zur Startseite",
    "nf.guide": "Anleitung lesen",
    "support.title": "Kundenservice",
    "support.intro": "Der Verkäufer antwortet persönlich (kein Bot), in der Regel innerhalb weniger Minuten. Sie können den Verkäufer auch per QQ {qq} hinzufügen. Geben Sie bei Fragen zu einer Bestellung bitte Ihre Bestellnummer an.",
    "support.ph": "Nachricht eingeben, z. B.: Bestellung GM… noch nicht gutgeschrieben",
    "support.send": "Senden",
    "support.err_expired": "Diese Seite ist abgelaufen — bitte aktualisieren und erneut versuchen.",
    "orders.title": "Meine Bestellungen",
    "orders.empty": "Noch keine Bestellungen.",
    "orders.go_order": "Bestellung aufgeben",
    "orders.no": "Bestellnr.",
    "orders.product": "Produkt",
    "orders.status": "Status",
    "orders.detail": "Details",
    "orders.pay": "Jetzt zahlen",
    "orders.cancel": "Bestellung stornieren",
    "orders.cancel_confirm": "Diese Bestellung stornieren?",
    "orders.cancel_confirm2": "Diese Bestellung stornieren? Dies kann nicht rückgängig gemacht werden.",
    "orders.delivery_title": "📦 Lieferung (Kontodaten)",
    "common.copy": "Kopieren",
    "orders.gemini_qq_pre": "QQ für Auflade-Hilfe:",
    "orders.gemini_qq_note": "(beim Hinzufügen bitte Bestellnummer angeben)",
    "detail.title": "Bestelldetails",
    "detail.not_found": "Bestellung nicht gefunden",
    "detail.order_no": "Bestellnr.",
    "detail.product": "Produkt: ",
    "detail.amount": "Betrag: ",
    "detail.created": "Bestellt am: ",
    "detail.paid_at": "Bezahlt am: ",
    "detail.status": "Status: ",
    "detail.usage": "So verwenden Sie es",
    "detail.delivery": "Lieferung",
    "detail.delivery_keep": "Bewahren Sie Ihre Lieferdaten sicher auf — geben Sie sie nicht an Dritte weiter.",
    "detail.delivery_account": "📦 Kontodaten",
    "detail.copy_all": "Alles kopieren",
    "detail.download_all": "Lieferung herunterladen",
    "detail.view_orders": "Bestellungen ansehen",
    "detail.continue": "Weiter einkaufen",
    "detail.file_suffix": "Lieferung",
    "hero.completed": "Bestellung abgeschlossen",
    "hero.paid": "Bezahlt — Verkäufer bearbeitet",
    "hero.unpaid": "Zahlung ausstehend",
    "hero.failed": "Bestellung fehlgeschlagen",
    "hero.refunded": "Bestellung erstattet",
    "hero.cancelled": "Bestellung storniert",
    "tip.completed": "Der Verkäufer hat diese Bestellung abgeschlossen; die Lieferung finden Sie unten (falls vorhanden).",
    "tip.paid": "Zahlung bestätigt. Der Verkäufer bearbeitet Bestellungen der Reihe nach; die Lieferung erscheint auf dieser Seite, sobald sie fertig ist.",
    "tip.unpaid": "Der Verkäufer beginnt mit der Bearbeitung erst nach abgeschlossener Zahlung.",
    "tip.failed": "Die Bearbeitung dieser Bestellung ist fehlgeschlagen. Für den Kundendienst wenden Sie sich mit Ihrer Bestellnummer per QQ an den Verkäufer.",
    "tip.refunded": "Diese Bestellung wurde erstattet. Fragen? Wenden Sie sich an den Verkäufer.",
    "tip.cancelled": "Diese Bestellung wurde storniert und wird nicht bearbeitet. Bitte geben Sie eine neue Bestellung auf, wenn Sie sie weiterhin möchten.",
    "track.title": "Bestellung verfolgen",
    "track.intro": "Keine Registrierung oder Anmeldung nötig: Geben Sie die <b>Bestellnummer</b> ein, die Sie nach der Bestellung erhalten haben, sowie die verwendeten <b>Kontaktdaten</b> (müssen exakt übereinstimmen), um Bestellstatus und Lieferung zu sehen.",
    "track.order_no": "Bestellnummer",
    "track.order_no_ph": "Die nach der Bestellung angezeigte Bestellnummer",
    "track.contact": "Kontaktdaten",
    "track.contact_ph": "Die bei der Bestellung angegebenen Kontaktdaten",
    "track.submit": "Bestellung verfolgen",
    "track.alt_pre": "Registrierte Nutzer können sich auch ",
    "track.alt_login": "anmelden",
    "track.alt_mid": " und unter Meine Bestellungen nachsehen. Immer noch nicht gefunden? Fügen Sie den Verkäufer per QQ ",
    "track.alt_post": " hinzu und geben Sie Ihre Bestellnummer an.",
    "order.title": "Bestellen",
    "order.soldout_title": "Ausverkauft",
    "order.soldout_body": "😔 Dieses Produkt ist gerade ausverkauft. Es ist wieder verfügbar, sobald der Verkäufer nachfüllt.",
    "order.soldout_hint": "Eilig? Fügen Sie den Verkäufer per QQ {qq} hinzu oder stöbern Sie zuerst in anderen Produkten.",
    "order.back_home": "← Zurück zur Startseite für andere Produkte",
    "order.stock_hint": "🔥 Nur noch {n} verfügbar — eines wird für Sie reserviert, sobald die Zahlung erfolgreich ist.",
    "order.required": "*Pflichtfeld",
    "order.aux_label": "Ersatz-E-Mail",
    "order.aux_hint": "Wird benötigt, falls bei der Aufladung eine Verifizierung nötig ist. Pflichtfeld, gültiges Format erforderlich.",
    "order.contact_label": "Kontaktdaten",
    "order.contact_ph": "WeChat / Telefon / QQ, damit der Verkäufer Sie erreichen kann",
    "order.submit": "Bestellung aufgeben & zahlen",
    "order.after_sale_pre": "Kundendienst: volle Rückerstattung vor der Lieferung; wenn ein geliefertes Konto keinen Login erlaubt, wenden Sie sich sofort an den Verkäufer. Die vollständigen Regeln finden Sie in der ",
    "order.after_sale_post": ".",
    "order.one_time": "Einmalzahlung",
    "order.member_line": "👑 {name}-Vorteil: {label}, Sie sparen ¥{off} bei dieser Bestellung",
    "order.err_expired": "Diese Seite ist abgelaufen — bitte aktualisieren und erneut versuchen",
    "order.err_soldout": "Dieses Produkt ist ausverkauft",
    "order.err_aux_required": "Die Ersatz-E-Mail ist ein Pflichtfeld und darf nicht leer sein",
    "order.err_aux_format": "Das Format der Ersatz-E-Mail ist falsch",
    "order.err_contact_required": "Kontaktdaten sind ein Pflichtfeld",
    "trust.sold": "{n} Bestellungen verkauft",
    "trust.avg_min": "Durchschn. Lieferung ≈ {n} Min.",
    "trust.avg_hour": "Durchschn. Lieferung ≈ {n} Std.",
    "trust.nopass": "Wir fragen niemals nach Ihrem Kontopasswort",
    "auth.register": "Registrieren",
    "auth.register_sub": "Erstellen Sie ein Konto und bestellen Sie sofort los",
    "auth.email": "E-Mail",
    "auth.password_rule": "Passwort (mindestens 8 Zeichen)",
    "auth.password_set_ph": "Legen Sie ein Passwort fest",
    "auth.have_account": "Haben Sie bereits ein Konto?",
    "auth.go_login": "Anmelden",
    "auth.login": "Anmelden",
    "auth.login_sub": "Melden Sie sich an, um zu bestellen und Ihre Bestellungen jederzeit zu verfolgen",
    "auth.password": "Passwort",
    "auth.password_ph": "Geben Sie Ihr Passwort ein",
    "auth.no_account": "Noch kein Konto?",
    "auth.register_now": "Jetzt registrieren",
    "auth.forgot": "Passwort vergessen",
    "auth.track_hint": "Ohne Registrierung bestellt? Nutzen Sie Bestellnummer + Kontaktdaten für die",
    "auth.track_link": "Gast-Bestellverfolgung",
    "auth.err_email": "Ungültiges E-Mail-Format",
    "auth.err_pw_short": "Das Passwort muss mindestens 8 Zeichen lang sein",
    "auth.err_email_taken": "Diese E-Mail ist bereits registriert — bitte melden Sie sich an",
    "auth.err_login": "E-Mail oder Passwort falsch",
}

STRINGS_ES = {
    "nav.home": "Inicio", "nav.order": "Pedir ahora",
    "nav.my_orders": "Mis pedidos", "nav.wallet": "Mi cartera",
    "nav.support": "Atención al cliente", "nav.guide": "Guía de uso",
    "nav.admin": "Administración del vendedor", "nav.logout": "Cerrar sesión",
    "nav.login": "Iniciar sesión", "nav.register": "Registrarse",
    "nav.track": "Rastrear pedido",
    "footer.tag": "Solo servicios digitales, sin envío físico",
    "footer.privacy": "Política de privacidad",
    "footer.terms": "Términos del servicio",
    "footer.cookies": "Política de cookies",
    "home.search_ph": "Buscar productos",
    "home.all": "Todos",
    "home.buy": "Comprar ahora →", "home.soldout": "Agotado",
    "home.sold_n": "{n} vendidos",
    "home.stock_n": "{n} en stock",
    "home.stock_low": "🔥 Quedan solo {n}",
    "home.stock_plenty": "En stock",
    "home.no_match": "Sin productos coincidentes",
    "common.yuan": "¥",
    "status.unpaid": "Pendiente de pago",
    "status.paid": "Pagado / Pendiente de entrega",
    "status.completed": "Completado (entregado)",
    "status.failed": "Fallido",
    "status.refunded": "Reembolsado",
    "status.cancelled": "Cancelado",
    "home.title": "Todos los productos",
    "track.err_notfound": "El número de pedido o los datos de contacto son incorrectos; compruébelos e inténtelo de nuevo",
    "track.result_title": "Resultado de la consulta del pedido",
    "track.more": "Consultar otro pedido",
    "chat.me": "Yo",
    "chat.seller": "Vendedor",
    "chat.customer": "Cliente",
    "chat.empty": "Aún no hay mensajes. Deje un mensaje abajo y el vendedor le responderá en cuanto lo vea.",
    "lock.msg": "Demasiados intentos; inténtelo de nuevo en {m} min",
    "guide.contact": "Contactar con el vendedor",
    "guide.contact_hint": "El vendedor suele estar disponible en horario laboral. Incluya su número de pedido en los mensajes para una gestión más rápida.",
    "legal.privacy_title": "Política de privacidad",
    "legal.terms_title": "Términos del servicio",
    "legal.cookies_title": "Política de cookies",
    "legal.updated": "Última actualización: 08/11/2026 · Aplicable a muse798.com (OBSIDIAN AI)",
    "legal.contact_pre": "Contacto: ",
    "legal.contact_post": " o con el vendedor por QQ {qq}.",
    "rpay.result_title": "Resultado de la recarga",
    "rpay.credited": "Acreditado",
    "rpay.confirming": "Confirmando",
    "rpay.tip_credited": "Su recarga ha sido acreditada; consulte el saldo en Mi cartera.",
    "rpay.tip_confirming": "Su pago aún se está confirmando; actualice Mi cartera dentro de un momento.",
    "pay.title": "Pagar el pedido",
    "pay.order_no": "N.º de pedido: ",
    "pay.product": "Producto: ",
    "pay.amount": "Importe a pagar: ",
    "pay.balance_btn": "Pagar con saldo (saldo ¥{b})",
    "pay.balance_low_pre": "Su saldo es de ¥{b}, insuficiente para este pedido. Puede ",
    "pay.goto_recharge": "recargar primero",
    "pay.balance_low_post": ".",
    "pay.balance_zero_pre": "Su saldo es de ¥0,00. Puede ",
    "pay.recharge_word": "recargar",
    "pay.balance_zero_post": " y luego pagar directamente con el saldo.",
    "pay.epay_btn": "Pagar con Alipay",
    "pay.note": "Tras el pago, el pedido pasará automáticamente a «Pagado / Pendiente de entrega» y el vendedor lo procesará por orden. Hasta que el pago se complete, el pedido permanecerá sin pagar y no se realizará ningún cargo.",
    "pay.status_title": "Estado del pedido",
    "pay.status_amount": "Importe: ",
    "pay.status_now": "Estado: ",
    "pay.tip_paid": "Pago confirmado. El vendedor procesará su pedido por orden.",
    "pay.tip_unpaid": "El resultado de su pago aún se está confirmando (prevalece la notificación asíncrona de la plataforma de pago). Actualice Mis pedidos dentro de un momento. Si el pago no se completó, el pedido permanecerá sin pagar y no se realizará ningún cargo.",
    "pay.tip_other": "El estado del pedido se muestra arriba. ¿Dudas? Contacte con el vendedor.",
    "pay.view_detail": "Ver detalles del pedido",
    "wallet.title": "Mi cartera",
    "wallet.balance_label": "Saldo actual",
    "wallet.custom_label": "O introduzca un importe personalizado (CNY)",
    "wallet.custom_ph": "p. ej., 30",
    "wallet.recharge_btn": "Recargar con Alipay",
    "wallet.note": "Recargue mediante Alipay; una vez acreditado el importe, podrá pagar los pedidos directamente con su saldo. Recarga única de ¥1 a ¥5.000. El saldo no puede retirarse; los reembolsos de pedidos pagados con saldo se devuelven automáticamente a su saldo.",
    "wallet.bonus_banner": "🎁 <b>Oferta de primera recarga</b>: la primera recarga de ¥10 o más acredita <b>¥12</b>; la de ¥15 o más acredita <b>¥20</b>. La bonificación se acredita automáticamente junto con el importe principal. Una por persona.",
    "wallet.paid_badge": "Acreditado",
    "wallet.unpaid_link": "Sin pagar · Pagar ahora",
    "wallet.bonus_incl": "Incluye la bonificación de primera recarga de ¥{b}; ¥{t} acreditados en total",
    "wallet.no_recharges": "Aún no hay recargas",
    "wallet.no_logs": "Aún no hay movimientos",
    "wallet.records": "Historial de recargas",
    "wallet.rc_no": "N.º de recarga",
    "wallet.amount": "Importe",
    "wallet.status": "Estado",
    "wallet.time": "Fecha",
    "wallet.logs": "Movimientos",
    "wallet.type": "Tipo",
    "wallet.change": "Variación",
    "wallet.balance": "Saldo",
    "wallet.note_col": "Nota",
    "wallet.member_title": "👑 Nivel de miembro",
    "wallet.member_now": "Nivel actual: <b>{name}</b> ({n} niveles en total; los descuentos se aplican automáticamente al pedir)",
    "wallet.lv_current": "Actual",
    "wallet.lv_next": "Siguiente",
    "wallet.lv_member": "Miembro",
    "wallet.lv_disc_all": "{label} en toda la tienda",
    "wallet.lv_disc_default": "Nivel predeterminado",
    "wallet.lv_req": "Subida automática al gastar ¥{s} o recargar ¥{r}",
    "wallet.lv_manual": "Su nivel lo ha fijado manualmente el vendedor 🎁 (progreso automático: ¥{s} gastados · ¥{r} recargados)",
    "wallet.lv_progress": "Total gastado ¥{s} · total recargado ¥{r}; para {name}: faltan ¥{ds} en compras o ¥{dr} en recargas",
    "wallet.lv_max": "Total gastado ¥{s} · total recargado ¥{r}; ya está en el nivel más alto 🎉",
    "wallet.err_amount": "Importe de recarga no válido: introduzca un importe entre ¥1 y ¥5.000.",
    "wallet.err_expired": "Esta página ha caducado; actualícela e inténtelo de nuevo.",
    "kind.recharge": "Recarga en línea",
    "kind.bonus": "Bonificación de primera recarga",
    "kind.pay": "Pago con saldo",
    "kind.refund": "Reembolso",
    "kind.admin": "Ajuste del vendedor",
    "rpay.title": "Pago de la recarga",
    "rpay.no": "N.º de recarga: ",
    "rpay.amount": "Importe de la recarga: ",
    "rpay.bonus_hint": "🎁 Es su primera recarga: se acreditará una bonificación extra de <b>¥{b}</b>, <b>¥{t}</b> en total.",
    "rpay.note": "Tras un pago correcto, su saldo se acredita automáticamente; consúltelo en Mi cartera. Si la acreditación se retrasa un poco, el sitio lo comprueba con la plataforma de pago cada minuto.",
    "rpay.not_found": "Recarga no encontrada",
    "forgot.title": "Contraseña olvidada",
    "forgot.p1": "La recuperación por correo electrónico en autoservicio aún no está disponible. Si ha olvidado su contraseña, contacte con el vendedor para verificar su identidad y restablecerla:",
    "forgot.li1": "Escríbanos mediante Atención al cliente en la parte superior de la página, o añada al vendedor por QQ <b>{qq}</b>, e indique su <b>correo de registro</b>;",
    "forgot.li2": "Tras la verificación, el vendedor restablecerá su contraseña en el panel de administración y le enviará la nueva;",
    "forgot.li3_pre": "En cuanto reciba la nueva contraseña, ",
    "forgot.li3_post": " lo antes posible para comprobar que funciona.",
    "forgot.hint": "Nota: el vendedor nunca le pedirá la contraseña de su cuenta de Google. Los restablecimientos de contraseña solo se gestionan de este modo; desconfíe de otros canales.",
    "forgot.back": "Volver a iniciar sesión",
    "qq.title": "La recarga necesita la ayuda del vendedor",
    "qq.copy": "Copiar QQ",
    "qq.note": "Indique su número de pedido al añadirlo. El vendedor le ayudará a completar la recarga. Nota: el vendedor nunca le pedirá la contraseña de su cuenta de Google.",
    "qq.pre": "Añada al vendedor por QQ",
    "nf.title": "Página no encontrada",
    "nf.body": "Es posible que la página que ha visitado se haya movido, o que la dirección se haya escrito mal.",
    "nf.home": "Volver al inicio",
    "nf.guide": "Leer la guía",
    "support.title": "Atención al cliente",
    "support.intro": "El vendedor responde personalmente (no es un robot), normalmente en pocos minutos. También puede añadir al vendedor por QQ {qq}. Para consultas sobre un pedido, incluya su número de pedido.",
    "support.ph": "Escriba un mensaje, p. ej.: el pedido GM… aún no se ha acreditado",
    "support.send": "Enviar",
    "support.err_expired": "Esta página ha caducado; actualícela e inténtelo de nuevo.",
    "orders.title": "Mis pedidos",
    "orders.empty": "Aún no hay pedidos.",
    "orders.go_order": "Hacer un pedido",
    "orders.no": "N.º de pedido",
    "orders.product": "Producto",
    "orders.status": "Estado",
    "orders.detail": "Detalles",
    "orders.pay": "Pagar ahora",
    "orders.cancel": "Cancelar pedido",
    "orders.cancel_confirm": "¿Cancelar este pedido?",
    "orders.cancel_confirm2": "¿Cancelar este pedido? No se puede deshacer.",
    "orders.delivery_title": "📦 Entrega (datos de la cuenta)",
    "common.copy": "Copiar",
    "orders.gemini_qq_pre": "QQ de ayuda para la recarga:",
    "orders.gemini_qq_note": "(indique su número de pedido al añadirlo)",
    "detail.title": "Detalles del pedido",
    "detail.not_found": "Pedido no encontrado",
    "detail.order_no": "N.º de pedido",
    "detail.product": "Producto: ",
    "detail.amount": "Importe: ",
    "detail.created": "Fecha del pedido: ",
    "detail.paid_at": "Fecha de pago: ",
    "detail.status": "Estado: ",
    "detail.usage": "Cómo usarlo",
    "detail.delivery": "Entrega",
    "detail.delivery_keep": "Guarde bien el contenido de su entrega; no lo reenvíe a nadie.",
    "detail.delivery_account": "📦 Datos de la cuenta",
    "detail.copy_all": "Copiar todo",
    "detail.download_all": "Descargar la entrega",
    "detail.view_orders": "Ver pedidos",
    "detail.continue": "Seguir comprando",
    "detail.file_suffix": "entrega",
    "hero.completed": "Pedido completado",
    "hero.paid": "Pagado: el vendedor lo está procesando",
    "hero.unpaid": "Pendiente de pago",
    "hero.failed": "Pedido fallido",
    "hero.refunded": "Pedido reembolsado",
    "hero.cancelled": "Pedido cancelado",
    "tip.completed": "El vendedor ha completado este pedido; la entrega está abajo (si la hay).",
    "tip.paid": "Pago confirmado. El vendedor procesa los pedidos por orden; la entrega aparecerá en esta página cuando esté lista.",
    "tip.unpaid": "El vendedor empezará a procesar el pedido solo cuando se complete el pago.",
    "tip.failed": "El procesamiento de este pedido ha fallado. Para el servicio posventa, contacte con el vendedor por QQ indicando su número de pedido.",
    "tip.refunded": "Este pedido ha sido reembolsado. ¿Dudas? Contacte con el vendedor.",
    "tip.cancelled": "Este pedido se canceló y no se procesará. Haga un nuevo pedido si aún lo desea.",
    "track.title": "Rastrear pedido",
    "track.intro": "No hace falta registrarse ni iniciar sesión: introduzca el <b>número de pedido</b> que recibió al pedir y los <b>datos de contacto</b> que utilizó (deben coincidir exactamente) para ver el estado del pedido y su entrega.",
    "track.order_no": "Número de pedido",
    "track.order_no_ph": "El número de pedido mostrado tras pedir",
    "track.contact": "Datos de contacto",
    "track.contact_ph": "Los datos de contacto que utilizó al pedir",
    "track.submit": "Rastrear pedido",
    "track.alt_pre": "Los usuarios registrados también pueden ",
    "track.alt_login": "iniciar sesión",
    "track.alt_mid": " y consultar Mis pedidos. ¿Sigue sin encontrarlo? Añada al vendedor por QQ ",
    "track.alt_post": " indicando su número de pedido.",
    "order.title": "Pedir",
    "order.soldout_title": "Agotado",
    "order.soldout_body": "😔 Este producto acaba de agotarse. Volverá cuando el vendedor reponga el stock.",
    "order.soldout_hint": "¿Tiene prisa? Añada al vendedor por QQ {qq} o eche un vistazo primero a otros productos.",
    "order.back_home": "← Volver al inicio para ver otros productos",
    "order.stock_hint": "🔥 Quedan solo {n}: se le reservará uno en cuanto el pago se complete.",
    "order.required": "*obligatorio",
    "order.aux_label": "Correo de respaldo",
    "order.aux_hint": "Se utiliza si se necesita una verificación durante la recarga. Es obligatorio y debe tener un formato válido.",
    "order.contact_label": "Datos de contacto",
    "order.contact_ph": "WeChat / teléfono / QQ, para que el vendedor pueda localizarle",
    "order.submit": "Confirmar pedido y pagar",
    "order.after_sale_pre": "Posventa: reembolso completo antes de la entrega; si una cuenta entregada no permite iniciar sesión, contacte de inmediato con el vendedor. Las normas completas están en la ",
    "order.after_sale_post": ".",
    "order.one_time": "pago único",
    "order.member_line": "👑 Ventaja {name}: {label}, ahorra ¥{off} en este pedido",
    "order.err_expired": "Esta página ha caducado; actualícela e inténtelo de nuevo",
    "order.err_soldout": "Este producto está agotado",
    "order.err_aux_required": "El correo de respaldo es obligatorio y no puede estar vacío",
    "order.err_aux_format": "El formato del correo de respaldo es incorrecto",
    "order.err_contact_required": "Los datos de contacto son obligatorios",
    "trust.sold": "{n} pedidos vendidos",
    "trust.avg_min": "Entrega media ≈ {n} min",
    "trust.avg_hour": "Entrega media ≈ {n} h",
    "trust.nopass": "Nunca pedimos la contraseña de su cuenta",
    "auth.register": "Registrarse",
    "auth.register_sub": "Cree una cuenta y empiece a pedir de inmediato",
    "auth.email": "Correo electrónico",
    "auth.password_rule": "Contraseña (mínimo 8 caracteres)",
    "auth.password_set_ph": "Establezca una contraseña",
    "auth.have_account": "¿Ya tiene una cuenta?",
    "auth.go_login": "Iniciar sesión",
    "auth.login": "Iniciar sesión",
    "auth.login_sub": "Inicie sesión para pedir y seguir sus pedidos en cualquier momento",
    "auth.password": "Contraseña",
    "auth.password_ph": "Introduzca su contraseña",
    "auth.no_account": "¿Aún no tiene cuenta?",
    "auth.register_now": "Registrarse ahora",
    "auth.forgot": "Contraseña olvidada",
    "auth.track_hint": "¿Pidió sin registrarse? Use su número de pedido + datos de contacto para el",
    "auth.track_link": "rastreo de pedidos como invitado",
    "auth.err_email": "Formato de correo no válido",
    "auth.err_pw_short": "La contraseña debe tener al menos 8 caracteres",
    "auth.err_email_taken": "Este correo ya está registrado; inicie sesión",
    "auth.err_login": "Correo o contraseña incorrectos",
}

PRODUCTS_FR = {
    "gemini-pro-24m": {
        "name": "Recharge Gemini Pro 24 mois",
        "points": ["Rechargé sur votre propre compte Google, 24 mois d'abonnement",
                   "Aucun mot de passe de compte requis — seulement l'e-mail de recharge et un e-mail de secours",
                   "Alipay accepté",
                   "Recharge manuelle après le paiement ; suivez l'avancement dans Mes commandes"],
        "desc": "Service de recharge d'abonnement Gemini Pro, 24 mois. Après le paiement, le vendeur recharge manuellement le compte Google que vous indiquez — aucun mot de passe de compte ne vous sera jamais demandé.",
        "first_label": "E-mail du compte Google à recharger",
        "password_hint": "Nous ne vous demanderons le mot de passe de votre compte Google à aucune étape.",
        "first_err": "L'adresse e-mail du compte Google à recharger n'est pas au format valide",
    },
    "muse-account-1b": {
        "name": "Compte Muse prêt à l'emploi · 1 milliard de tokens",
        "points": ["Compte prêt à l'emploi avec 1 milliard de tokens d'utilisation",
                   "En termes simples : les tokens ≈ la quantité de texte que l'IA lit et écrit ; 1 milliard de tokens représente environ plusieurs centaines de millions de caractères chinois — de quoi discuter et écrire au quotidien pendant longtemps (estimation ; la consommation réelle dépend de la longueur des conversations)",
                   "Livré manuellement par le vendeur via vos coordonnées après le paiement",
                   "Alipay accepté",
                   "Suivez l'avancement de la livraison dans Mes commandes"],
        "desc": "Compte Muse prêt à l'emploi avec 1 milliard de tokens. Livré manuellement par le vendeur via les coordonnées que vous indiquez.",
        "first_label": "E-mail de réception du compte",
        "password_hint": "Après le paiement, le vendeur livrera le compte via les coordonnées que vous indiquez — veuillez vous assurer qu'elles sont exactes.",
        "first_err": "Le format de l'adresse e-mail de réception du compte est incorrect",
    },
    "muse-2b": {
        "name": "Muse · 2 milliards de tokens",
        "points": ["Compte Muse avec 2 milliards de tokens",
                   "En termes simples : les tokens ≈ la quantité de texte que l'IA lit et écrit ; 2 milliards, c'est le double de 1 milliard, et cela tient bien même en cas d'utilisation quotidienne intensive (estimation ; la consommation réelle dépend de la longueur des conversations)",
                   "Traité manuellement par le vendeur après le paiement et livré via vos coordonnées",
                   "Alipay accepté",
                   "Suivez l'avancement dans Mes commandes"],
        "desc": "Muse, 2 milliards de tokens. Traité manuellement par le vendeur après le paiement et livré via vos coordonnées.",
        "first_label": "E-mail de réception",
        "password_hint": "Après le paiement, le vendeur effectuera la livraison via les coordonnées que vous indiquez — veuillez vous assurer qu'elles sont exactes.",
        "first_err": "Le format de l'adresse e-mail de réception est incorrect",
    },
    "muse3-1b": {
        "name": "Muse · 31 milliards de tokens",
        "points": ["Compte Muse avec 31 milliards de tokens",
                   "En termes simples : les tokens ≈ la quantité de texte que l'IA lit et écrit ; 31 milliards, c'est environ 31 fois l'offre à 1 milliard, conçu pour un usage intensif et durable (estimation ; la consommation réelle dépend de la longueur des conversations)",
                   "Traité manuellement par le vendeur après le paiement et livré via vos coordonnées",
                   "Alipay accepté",
                   "Suivez l'avancement dans Mes commandes"],
        "desc": "Muse, 31 milliards de tokens. Traité manuellement par le vendeur après le paiement et livré via vos coordonnées.",
        "first_label": "E-mail de réception",
        "password_hint": "Après le paiement, le vendeur effectuera la livraison via les coordonnées que vous indiquez — veuillez vous assurer qu'elles sont exactes.",
        "first_err": "Le format de l'adresse e-mail de réception est incorrect",
    },
    "chatgpt-go-3m": {
        "name": "ChatGPT Go 3 mois",
        "points": ["Compte prêt à l'emploi, 3 mois d'abonnement ChatGPT Go",
                   "Format de livraison : e-mail | mot de passe | clé secrète 2FA",
                   "Garantie de 3 jours",
                   "Codes 2FA : ouvrez https://2fa.fun/ , saisissez la clé secrète 2FA et cliquez sur Obtenir le code — les codes se renouvellent toutes les 30 secondes",
                   "Livré manuellement par le vendeur via vos coordonnées après le paiement",
                   "Alipay accepté",
                   "Suivez l'avancement de la livraison dans Mes commandes"],
        "desc": "Compte ChatGPT Go prêt à l'emploi, 3 mois, activé via Apple Pay. Livré manuellement par le vendeur via vos coordonnées.",
        "first_label": "E-mail de réception du compte",
        "password_hint": "Après le paiement, le vendeur livrera le compte via les coordonnées que vous indiquez — veuillez vous assurer qu'elles sont exactes.",
        "first_err": "Le format de l'adresse e-mail de réception du compte est incorrect",
    },
    "chatgpt-plus-1m-applepay": {
        "name": "ChatGPT Plus 1 mois (Apple Pay)",
        "points": ["Compte prêt à l'emploi, 1 mois de ChatGPT Plus, activé via Apple Pay",
                   "Format de livraison : e-mail / mot de passe / clé secrète 2FA",
                   "Garantie : couvre uniquement la première connexion dans un délai de 1 heure (garantie première connexion 1 h) — connectez-vous et vérifiez dès réception",
                   "Livré manuellement par le vendeur via vos coordonnées après le paiement",
                   "Alipay accepté",
                   "Suivez l'avancement de la livraison dans Mes commandes"],
        "desc": "Compte ChatGPT Plus prêt à l'emploi, 1 mois, activé via Apple Pay. Livré manuellement par le vendeur via vos coordonnées.",
        "first_label": "E-mail de réception du compte",
        "password_hint": "Après le paiement, le vendeur livrera le compte via les coordonnées que vous indiquez — veuillez vous assurer qu'elles sont exactes.",
        "first_err": "Le format de l'adresse e-mail de réception du compte est incorrect",
    },
    "grok-plus-1m": {
        "name": "Grok Plus 1 mois",
        "points": ["Compte prêt à l'emploi, 1 mois d'abonnement Grok Plus",
                   "Pool d'utilisation IA partagé, incluant le chat Grok, la voix, Imagine et Build",
                   "Inclut l'accès à l'API Grok ; à utiliser sur grok.com",
                   "Format de livraison : e-mail + mot de passe (tous deux modifiables)",
                   "Ne dissociez pas le compte de X, sous peine d'affecter l'utilisation",
                   "Aucune garantie sur ce produit ; les services de vérification de connexion ne sont pas couverts",
                   "Livré manuellement par le vendeur via vos coordonnées après le paiement",
                   "Alipay accepté",
                   "Suivez l'avancement de la livraison dans Mes commandes"],
        "desc": "Compte Grok Plus prêt à l'emploi, 1 mois. Livré manuellement par le vendeur via vos coordonnées.",
        "first_label": "E-mail de réception du compte",
        "password_hint": "Après le paiement, le vendeur livrera le compte via les coordonnées que vous indiquez — veuillez vous assurer qu'elles sont exactes.",
        "first_err": "Le format de l'adresse e-mail de réception du compte est incorrect",
    },
    "grok-plus-7d": {
        "name": "Grok Plus 7 jours",
        "points": ["Compte prêt à l'emploi, 7 jours d'abonnement Grok Plus",
                   "Garantie de 1 jour",
                   "Pool d'utilisation IA partagé, incluant le chat Grok, la voix, Imagine et Build",
                   "Inclut l'accès à l'API Grok ; à utiliser sur grok.com",
                   "Format de livraison : e-mail + mot de passe (tous deux modifiables)",
                   "Ne dissociez pas le compte de X, sous peine d'affecter l'utilisation",
                   "Les services de vérification de connexion ne sont pas couverts par la garantie",
                   "Livré manuellement par le vendeur via vos coordonnées après le paiement",
                   "Alipay accepté",
                   "Suivez l'avancement de la livraison dans Mes commandes"],
        "desc": "Compte Grok Plus prêt à l'emploi, 7 jours. Livré manuellement par le vendeur via vos coordonnées.",
        "first_label": "E-mail de réception du compte",
        "password_hint": "Après le paiement, le vendeur livrera le compte via les coordonnées que vous indiquez — veuillez vous assurer qu'elles sont exactes.",
        "first_err": "Le format de l'adresse e-mail de réception du compte est incorrect",
    },
    "gmail-old-account": {
        "name": "Compte Gmail ancien (2010–2022), région aléatoire",
        "points": ["Compte Gmail ancien enregistré entre 2010 et 2022, région attribuée aléatoirement",
                   "Format de livraison : compte e-mail + mot de passe de connexion + e-mail de secours + 2FA",
                   "Garantie première connexion 24 h : couvre uniquement la première connexion dans les 24 heures — connectez-vous et vérifiez dès réception",
                   "La connexion peut exiger une vérification par téléphone ; veuillez prévoir votre propre moyen de réception de SMS",
                   "Un environnement réseau stable et fiable est recommandé pour la connexion",
                   "Livré manuellement par le vendeur via vos coordonnées après le paiement",
                   "Alipay accepté",
                   "Suivez l'avancement de la livraison dans Mes commandes"],
        "desc": "Compte Gmail ancien, enregistré entre 2010 et 2022, région aléatoire. Livré manuellement par le vendeur via vos coordonnées.",
        "first_label": "E-mail de réception du compte",
        "password_hint": "Après le paiement, le vendeur livrera le compte via les coordonnées que vous indiquez — veuillez vous assurer qu'elles sont exactes.",
        "first_err": "Le format de l'adresse e-mail de réception du compte est incorrect",
    },
}

PRODUCTS_DE = {
    "gemini-pro-24m": {
        "name": "Gemini Pro Aufladung, 24 Monate",
        "points": ["Wird auf Ihr eigenes Google-Konto aufgeladen, 24 Monate Mitgliedschaft",
                   "Kein Kontopasswort nötig — nur die Auflade-E-Mail und eine Ersatz-E-Mail",
                   "Alipay wird akzeptiert",
                   "Manuelle Aufladung nach der Zahlung; Fortschritt unter Meine Bestellungen verfolgen"],
        "desc": "Aufladeservice für die Gemini Pro Mitgliedschaft, 24 Monate. Nach der Zahlung lädt der Verkäufer das von Ihnen angegebene Google-Konto manuell auf — ein Kontopasswort wird zu keinem Zeitpunkt benötigt.",
        "first_label": "E-Mail des aufzuladenden Google-Kontos",
        "password_hint": "Wir werden Sie in keinem Schritt nach dem Passwort Ihres Google-Kontos fragen.",
        "first_err": "Die E-Mail des aufzuladenden Google-Kontos hat kein gültiges Format",
    },
    "muse-account-1b": {
        "name": "Muse Fertigkonto · 1 Mrd. Token",
        "points": ["Einsatzbereites Konto mit 1 Mrd. Token Nutzungsguthaben",
                   "Einfach gesagt: Token ≈ die Menge an Text, die die KI liest und schreibt; 1 Mrd. Token entspricht grob mehreren hundert Millionen chinesischen Schriftzeichen — genug für alltägliche Chats und Texte über lange Zeit (Schätzung; der tatsächliche Verbrauch hängt von der Gesprächslänge ab)",
                   "Nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert",
                   "Alipay wird akzeptiert",
                   "Lieferfortschritt unter Meine Bestellungen verfolgen"],
        "desc": "Muse Fertigkonto mit 1 Mrd. Token. Wird nach der Zahlung vom Verkäufer manuell über die von Ihnen angegebenen Kontaktdaten geliefert.",
        "first_label": "E-Mail zum Empfang des Kontos",
        "password_hint": "Nach der Zahlung liefert der Verkäufer das Konto über Ihre angegebenen Kontaktdaten — bitte stellen Sie sicher, dass sie korrekt sind.",
        "first_err": "Das Format der E-Mail für den Kontoempfang ist falsch",
    },
    "muse-2b": {
        "name": "Muse · 2 Mrd. Token",
        "points": ["Muse Konto mit 2 Mrd. Token",
                   "Einfach gesagt: Token ≈ die Menge an Text, die die KI liest und schreibt; 2 Mrd. sind das Doppelte von 1 Mrd. und halten selbst bei intensiver täglicher Nutzung gut durch (Schätzung; der tatsächliche Verbrauch hängt von der Gesprächslänge ab)",
                   "Nach der Zahlung vom Verkäufer manuell bearbeitet und über Ihre Kontaktdaten geliefert",
                   "Alipay wird akzeptiert",
                   "Fortschritt unter Meine Bestellungen verfolgen"],
        "desc": "Muse, 2 Mrd. Token. Wird nach der Zahlung vom Verkäufer manuell bearbeitet und über Ihre Kontaktdaten geliefert.",
        "first_label": "Empfangs-E-Mail",
        "password_hint": "Nach der Zahlung liefert der Verkäufer über Ihre angegebenen Kontaktdaten — bitte stellen Sie sicher, dass sie korrekt sind.",
        "first_err": "Das Format der Empfangs-E-Mail ist falsch",
    },
    "muse3-1b": {
        "name": "Muse · 31 Mrd. Token",
        "points": ["Muse Konto mit 31 Mrd. Token",
                   "Einfach gesagt: Token ≈ die Menge an Text, die die KI liest und schreibt; 31 Mrd. sind etwa das 31-Fache des 1-Mrd.-Tarifs, ausgelegt für langfristige intensive Nutzung (Schätzung; der tatsächliche Verbrauch hängt von der Gesprächslänge ab)",
                   "Nach der Zahlung vom Verkäufer manuell bearbeitet und über Ihre Kontaktdaten geliefert",
                   "Alipay wird akzeptiert",
                   "Fortschritt unter Meine Bestellungen verfolgen"],
        "desc": "Muse, 31 Mrd. Token. Wird nach der Zahlung vom Verkäufer manuell bearbeitet und über Ihre Kontaktdaten geliefert.",
        "first_label": "Empfangs-E-Mail",
        "password_hint": "Nach der Zahlung liefert der Verkäufer über Ihre angegebenen Kontaktdaten — bitte stellen Sie sicher, dass sie korrekt sind.",
        "first_err": "Das Format der Empfangs-E-Mail ist falsch",
    },
    "chatgpt-go-3m": {
        "name": "ChatGPT Go 3 Monate",
        "points": ["Fertigkonto, 3 Monate ChatGPT Go Mitgliedschaft",
                   "Lieferformat: E-Mail | Passwort | 2FA-Geheimnis",
                   "3 Tage Garantie",
                   "2FA-Codes: Öffnen Sie https://2fa.fun/ , geben Sie das 2FA-Geheimnis ein und klicken Sie auf „Code abrufen“ — die Codes erneuern sich alle 30 Sekunden",
                   "Nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert",
                   "Alipay wird akzeptiert",
                   "Lieferfortschritt unter Meine Bestellungen verfolgen"],
        "desc": "ChatGPT Go Fertigkonto, 3 Monate, per Apple Pay aktiviert. Wird nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert.",
        "first_label": "E-Mail zum Empfang des Kontos",
        "password_hint": "Nach der Zahlung liefert der Verkäufer das Konto über Ihre angegebenen Kontaktdaten — bitte stellen Sie sicher, dass sie korrekt sind.",
        "first_err": "Das Format der E-Mail für den Kontoempfang ist falsch",
    },
    "chatgpt-plus-1m-applepay": {
        "name": "ChatGPT Plus 1 Monat (Apple Pay)",
        "points": ["Fertigkonto, 1 Monat ChatGPT Plus, per Apple Pay aktiviert",
                   "Lieferformat: E-Mail / Passwort / 2FA-Geheimnis",
                   "Garantie: deckt nur den ersten Login innerhalb von 1 Stunde ab (1-Std.-Erstlogin-Garantie) — bitte melden Sie sich nach Erhalt sofort an und prüfen Sie das Konto",
                   "Nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert",
                   "Alipay wird akzeptiert",
                   "Lieferfortschritt unter Meine Bestellungen verfolgen"],
        "desc": "ChatGPT Plus Fertigkonto, 1 Monat, per Apple Pay aktiviert. Wird nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert.",
        "first_label": "E-Mail zum Empfang des Kontos",
        "password_hint": "Nach der Zahlung liefert der Verkäufer das Konto über Ihre angegebenen Kontaktdaten — bitte stellen Sie sicher, dass sie korrekt sind.",
        "first_err": "Das Format der E-Mail für den Kontoempfang ist falsch",
    },
    "grok-plus-1m": {
        "name": "Grok Plus 1 Monat",
        "points": ["Fertigkonto, 1 Monat Grok Plus Mitgliedschaft",
                   "Gemeinsamer KI-Nutzungspool, inklusive Grok Chat, Sprache, Imagine und Build",
                   "Inklusive Grok API-Zugang; Nutzung auf grok.com",
                   "Lieferformat: E-Mail + Passwort (beides änderbar)",
                   "Trennen Sie die Verknüpfung des Kontos mit X nicht, sonst kann die Nutzung beeinträchtigt werden",
                   "Keine Garantie für dieses Produkt; Login-Prüfdienste sind nicht abgedeckt",
                   "Nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert",
                   "Alipay wird akzeptiert",
                   "Lieferfortschritt unter Meine Bestellungen verfolgen"],
        "desc": "Grok Plus Fertigkonto, 1 Monat. Wird nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert.",
        "first_label": "E-Mail zum Empfang des Kontos",
        "password_hint": "Nach der Zahlung liefert der Verkäufer das Konto über Ihre angegebenen Kontaktdaten — bitte stellen Sie sicher, dass sie korrekt sind.",
        "first_err": "Das Format der E-Mail für den Kontoempfang ist falsch",
    },
    "grok-plus-7d": {
        "name": "Grok Plus 7 Tage",
        "points": ["Fertigkonto, 7 Tage Grok Plus Mitgliedschaft",
                   "1 Tag Garantie",
                   "Gemeinsamer KI-Nutzungspool, inklusive Grok Chat, Sprache, Imagine und Build",
                   "Inklusive Grok API-Zugang; Nutzung auf grok.com",
                   "Lieferformat: E-Mail + Passwort (beides änderbar)",
                   "Trennen Sie die Verknüpfung des Kontos mit X nicht, sonst kann die Nutzung beeinträchtigt werden",
                   "Login-Prüfdienste sind von der Garantie nicht abgedeckt",
                   "Nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert",
                   "Alipay wird akzeptiert",
                   "Lieferfortschritt unter Meine Bestellungen verfolgen"],
        "desc": "Grok Plus Fertigkonto, 7 Tage. Wird nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert.",
        "first_label": "E-Mail zum Empfang des Kontos",
        "password_hint": "Nach der Zahlung liefert der Verkäufer das Konto über Ihre angegebenen Kontaktdaten — bitte stellen Sie sicher, dass sie korrekt sind.",
        "first_err": "Das Format der E-Mail für den Kontoempfang ist falsch",
    },
    "gmail-old-account": {
        "name": "Altes Gmail-Konto (2010–2022), zufällige Region",
        "points": ["Altes Gmail-Konto, registriert 2010–2022, Region wird zufällig zugewiesen",
                   "Lieferformat: E-Mail-Konto + Login-Passwort + Ersatz-E-Mail + 2FA",
                   "24-Std.-Erstlogin-Garantie: deckt nur den ersten Login innerhalb von 24 Stunden ab — bitte melden Sie sich nach Erhalt sofort an und prüfen Sie das Konto",
                   "Beim Login kann eine Telefonverifizierung nötig sein; bitte sorgen Sie selbst für eine SMS-Empfangsmöglichkeit",
                   "Für den Login wird eine stabile, vertrauenswürdige Netzwerkumgebung empfohlen",
                   "Nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert",
                   "Alipay wird akzeptiert",
                   "Lieferfortschritt unter Meine Bestellungen verfolgen"],
        "desc": "Altes Gmail-Konto, registriert 2010–2022, zufällige Region. Wird nach der Zahlung vom Verkäufer manuell über Ihre Kontaktdaten geliefert.",
        "first_label": "E-Mail zum Empfang des Kontos",
        "password_hint": "Nach der Zahlung liefert der Verkäufer das Konto über Ihre angegebenen Kontaktdaten — bitte stellen Sie sicher, dass sie korrekt sind.",
        "first_err": "Das Format der E-Mail für den Kontoempfang ist falsch",
    },
}

PRODUCTS_ES = {
    "gemini-pro-24m": {
        "name": "Recarga de Gemini Pro por 24 meses",
        "points": ["Recargado en su propia cuenta de Google, 24 meses de suscripción",
                   "No se necesita la contraseña de la cuenta: solo el correo de recarga y un correo de respaldo",
                   "Se acepta Alipay",
                   "Recarga manual tras el pago; siga el progreso en Mis pedidos"],
        "desc": "Servicio de recarga de la suscripción Gemini Pro, 24 meses. Tras el pago, el vendedor recarga manualmente la cuenta de Google que usted indique; nunca se le pedirá la contraseña de la cuenta.",
        "first_label": "Correo de la cuenta de Google a recargar",
        "password_hint": "En ningún paso le pediremos la contraseña de su cuenta de Google.",
        "first_err": "El correo de la cuenta de Google a recargar no tiene un formato válido",
    },
    "muse-account-1b": {
        "name": "Cuenta Muse lista para usar · 1 000 millones de tokens",
        "points": ["Cuenta lista para usar con 1 000 millones de tokens de uso",
                   "En términos sencillos: los tokens ≈ la cantidad de texto que la IA lee y escribe; 1 000 millones de tokens equivalen aproximadamente a cientos de millones de caracteres chinos, suficiente para chatear y escribir a diario durante mucho tiempo (estimación; el consumo real depende de la longitud de las conversaciones)",
                   "Entregada manualmente por el vendedor a través de sus datos de contacto tras el pago",
                   "Se acepta Alipay",
                   "Siga el progreso de la entrega en Mis pedidos"],
        "desc": "Cuenta Muse lista para usar con 1 000 millones de tokens. Entregada manualmente por el vendedor a través de los datos de contacto que usted indique.",
        "first_label": "Correo para recibir la cuenta",
        "password_hint": "Tras el pago, el vendedor entregará la cuenta a través de los datos de contacto que usted indique; asegúrese de que sean correctos.",
        "first_err": "El formato del correo de recepción de la cuenta es incorrecto",
    },
    "muse-2b": {
        "name": "Muse · 2 000 millones de tokens",
        "points": ["Cuenta Muse con 2 000 millones de tokens",
                   "En términos sencillos: los tokens ≈ la cantidad de texto que la IA lee y escribe; 2 000 millones es el doble de 1 000 millones y rinde bien incluso con un uso diario intensivo (estimación; el consumo real depende de la longitud de las conversaciones)",
                   "Procesada manualmente por el vendedor tras el pago y entregada a través de sus datos de contacto",
                   "Se acepta Alipay",
                   "Siga el progreso en Mis pedidos"],
        "desc": "Muse, 2 000 millones de tokens. Procesada manualmente por el vendedor tras el pago y entregada a través de sus datos de contacto.",
        "first_label": "Correo de recepción",
        "password_hint": "Tras el pago, el vendedor realizará la entrega a través de los datos de contacto que usted indique; asegúrese de que sean correctos.",
        "first_err": "El formato del correo de recepción es incorrecto",
    },
    "muse3-1b": {
        "name": "Muse · 31 000 millones de tokens",
        "points": ["Cuenta Muse con 31 000 millones de tokens",
                   "En términos sencillos: los tokens ≈ la cantidad de texto que la IA lee y escribe; 31 000 millones es unas 31 veces el plan de 1 000 millones, pensado para un uso intensivo a largo plazo (estimación; el consumo real depende de la longitud de las conversaciones)",
                   "Procesada manualmente por el vendedor tras el pago y entregada a través de sus datos de contacto",
                   "Se acepta Alipay",
                   "Siga el progreso en Mis pedidos"],
        "desc": "Muse, 31 000 millones de tokens. Procesada manualmente por el vendedor tras el pago y entregada a través de sus datos de contacto.",
        "first_label": "Correo de recepción",
        "password_hint": "Tras el pago, el vendedor realizará la entrega a través de los datos de contacto que usted indique; asegúrese de que sean correctos.",
        "first_err": "El formato del correo de recepción es incorrecto",
    },
    "chatgpt-go-3m": {
        "name": "ChatGPT Go 3 meses",
        "points": ["Cuenta lista para usar, 3 meses de suscripción ChatGPT Go",
                   "Formato de entrega: correo | contraseña | clave secreta 2FA",
                   "Garantía de 3 días",
                   "Códigos 2FA: abra https://2fa.fun/ , introduzca la clave secreta 2FA y haga clic en Obtener código; los códigos se renuevan cada 30 segundos",
                   "Entregada manualmente por el vendedor a través de sus datos de contacto tras el pago",
                   "Se acepta Alipay",
                   "Siga el progreso de la entrega en Mis pedidos"],
        "desc": "Cuenta ChatGPT Go lista para usar, 3 meses, activada mediante Apple Pay. Entregada manualmente por el vendedor a través de sus datos de contacto.",
        "first_label": "Correo para recibir la cuenta",
        "password_hint": "Tras el pago, el vendedor entregará la cuenta a través de los datos de contacto que usted indique; asegúrese de que sean correctos.",
        "first_err": "El formato del correo de recepción de la cuenta es incorrecto",
    },
    "chatgpt-plus-1m-applepay": {
        "name": "ChatGPT Plus 1 mes (Apple Pay)",
        "points": ["Cuenta lista para usar, 1 mes de ChatGPT Plus, activada mediante Apple Pay",
                   "Formato de entrega: correo / contraseña / clave secreta 2FA",
                   "Garantía: cubre solo el primer inicio de sesión dentro de 1 hora (garantía de primer inicio de sesión de 1 h); inicie sesión y verifíquela en cuanto la reciba",
                   "Entregada manualmente por el vendedor a través de sus datos de contacto tras el pago",
                   "Se acepta Alipay",
                   "Siga el progreso de la entrega en Mis pedidos"],
        "desc": "Cuenta ChatGPT Plus lista para usar, 1 mes, activada mediante Apple Pay. Entregada manualmente por el vendedor a través de sus datos de contacto.",
        "first_label": "Correo para recibir la cuenta",
        "password_hint": "Tras el pago, el vendedor entregará la cuenta a través de los datos de contacto que usted indique; asegúrese de que sean correctos.",
        "first_err": "El formato del correo de recepción de la cuenta es incorrecto",
    },
    "grok-plus-1m": {
        "name": "Grok Plus 1 mes",
        "points": ["Cuenta lista para usar, 1 mes de suscripción Grok Plus",
                   "Fondo compartido de uso de IA, que incluye el chat de Grok, la voz, Imagine y Build",
                   "Incluye acceso a la API de Grok; se usa en grok.com",
                   "Formato de entrega: correo + contraseña (ambos pueden cambiarse)",
                   "No desvincule la cuenta de X, o el uso podría verse afectado",
                   "Este producto no tiene garantía; los servicios de comprobación de inicio de sesión no están cubiertos",
                   "Entregada manualmente por el vendedor a través de sus datos de contacto tras el pago",
                   "Se acepta Alipay",
                   "Siga el progreso de la entrega en Mis pedidos"],
        "desc": "Cuenta Grok Plus lista para usar, 1 mes. Entregada manualmente por el vendedor a través de sus datos de contacto.",
        "first_label": "Correo para recibir la cuenta",
        "password_hint": "Tras el pago, el vendedor entregará la cuenta a través de los datos de contacto que usted indique; asegúrese de que sean correctos.",
        "first_err": "El formato del correo de recepción de la cuenta es incorrecto",
    },
    "grok-plus-7d": {
        "name": "Grok Plus 7 días",
        "points": ["Cuenta lista para usar, 7 días de suscripción Grok Plus",
                   "Garantía de 1 día",
                   "Fondo compartido de uso de IA, que incluye el chat de Grok, la voz, Imagine y Build",
                   "Incluye acceso a la API de Grok; se usa en grok.com",
                   "Formato de entrega: correo + contraseña (ambos pueden cambiarse)",
                   "No desvincule la cuenta de X, o el uso podría verse afectado",
                   "Los servicios de comprobación de inicio de sesión no están cubiertos por la garantía",
                   "Entregada manualmente por el vendedor a través de sus datos de contacto tras el pago",
                   "Se acepta Alipay",
                   "Siga el progreso de la entrega en Mis pedidos"],
        "desc": "Cuenta Grok Plus lista para usar, 7 días. Entregada manualmente por el vendedor a través de sus datos de contacto.",
        "first_label": "Correo para recibir la cuenta",
        "password_hint": "Tras el pago, el vendedor entregará la cuenta a través de los datos de contacto que usted indique; asegúrese de que sean correctos.",
        "first_err": "El formato del correo de recepción de la cuenta es incorrecto",
    },
    "gmail-old-account": {
        "name": "Cuenta Gmail antigua (2010–2022), región aleatoria",
        "points": ["Cuenta Gmail antigua registrada entre 2010 y 2022, región asignada al azar",
                   "Formato de entrega: cuenta de correo + contraseña de acceso + correo de respaldo + 2FA",
                   "Garantía de primer inicio de sesión de 24 h: cubre solo el primer inicio de sesión dentro de las 24 horas; inicie sesión y verifíquela en cuanto la reciba",
                   "El inicio de sesión puede requerir verificación telefónica; prevea su propio método de recepción de SMS",
                   "Se recomienda un entorno de red estable y de confianza para iniciar sesión",
                   "Entregada manualmente por el vendedor a través de sus datos de contacto tras el pago",
                   "Se acepta Alipay",
                   "Siga el progreso de la entrega en Mis pedidos"],
        "desc": "Cuenta Gmail antigua, registrada entre 2010 y 2022, región aleatoria. Entregada manualmente por el vendedor a través de sus datos de contacto.",
        "first_label": "Correo para recibir la cuenta",
        "password_hint": "Tras el pago, el vendedor entregará la cuenta a través de los datos de contacto que usted indique; asegúrese de que sean correctos.",
        "first_err": "El formato del correo de recepción de la cuenta es incorrecto",
    },
}

WARRANTY_FR = {
    "gemini-pro-24m": "🛡 Remboursement intégral si la recharge échoue",
    "muse-account-1b": "🛡 Première connexion garantie",
    "muse-2b": "🛡 Première connexion garantie",
    "muse3-1b": "🛡 Première connexion garantie",
    "chatgpt-go-3m": "🛡 Garantie 3 jours",
    "chatgpt-plus-1m-applepay": "🛡 Garantie 1 heure · première connexion",
    "grok-plus-1m": None,
    "grok-plus-7d": "🛡 Garantie 1 jour",
    "gmail-old-account": "🛡 Garantie 24 heures · première connexion",
}
WARRANTY_DE = {
    "gemini-pro-24m": "🛡 Volle Rückerstattung, wenn die Aufladung fehlschlägt",
    "muse-account-1b": "🛡 Erste Anmeldung garantiert",
    "muse-2b": "🛡 Erste Anmeldung garantiert",
    "muse3-1b": "🛡 Erste Anmeldung garantiert",
    "chatgpt-go-3m": "🛡 3 Tage Garantie",
    "chatgpt-plus-1m-applepay": "🛡 1 Stunde Garantie · erster Login",
    "grok-plus-1m": None,
    "grok-plus-7d": "🛡 1 Tag Garantie",
    "gmail-old-account": "🛡 24 Stunden Garantie · erster Login",
}
WARRANTY_ES = {
    "gemini-pro-24m": "🛡 Reembolso completo si falla la recarga",
    "muse-account-1b": "🛡 Primer inicio de sesión garantizado",
    "muse-2b": "🛡 Primer inicio de sesión garantizado",
    "muse3-1b": "🛡 Primer inicio de sesión garantizado",
    "chatgpt-go-3m": "🛡 Garantía de 3 días",
    "chatgpt-plus-1m-applepay": "🛡 Garantía de 1 hora · primer inicio de sesión",
    "grok-plus-1m": None,
    "grok-plus-7d": "🛡 Garantía de 1 día",
    "gmail-old-account": "🛡 Garantía de 24 horas · primer inicio de sesión",
}

CAT_FR = {"gemini": "Gemini", "muse": "Muse", "openai": "OpenAI", "grok": "Grok", "gmail": "Gmail"}
CAT_DE = {"gemini": "Gemini", "muse": "Muse", "openai": "OpenAI", "grok": "Grok", "gmail": "Gmail"}
CAT_ES = {"gemini": "Gemini", "muse": "Muse", "openai": "OpenAI", "grok": "Grok", "gmail": "Gmail"}

ANN_FR = [
    ("🎉 Bonus de première recharge : première recharge du portefeuille de ¥10 ou plus = ¥2 offerts, ¥15 ou plus = ¥5 offerts — voir Mon portefeuille →", "/wallet"),
    ("🛡 Protection de l'acheteur : remboursement intégral avant la livraison ; voir le badge de garantie de chaque produit et le Guide →", "/guide"),
    ("💬 Livraison manuelle : le vendeur traite les commandes à la main après le paiement ; suivez l'avancement dans Mes commandes ou contactez le Service client →", "/support"),
]
ANN_DE = [
    ("🎉 Erstauflade-Bonus: Erste Guthaben-Aufladung ab ¥10 gibt ¥2 gratis, ab ¥15 gibt ¥5 gratis — siehe Mein Guthaben →", "/wallet"),
    ("🛡 Käuferschutz: volle Rückerstattung vor der Lieferung; siehe das Garantie-Badge der einzelnen Produkte und die Anleitung →", "/guide"),
    ("💬 Manuelle Lieferung: Der Verkäufer bearbeitet Bestellungen nach der Zahlung von Hand; Fortschritt unter Meine Bestellungen verfolgen oder den Kundenservice kontaktieren →", "/support"),
]
ANN_ES = [
    ("🎉 Bonificación por primera recarga: la primera recarga de la cartera de ¥10 o más regala ¥2; la de ¥15 o más regala ¥5 — ver Mi cartera →", "/wallet"),
    ("🛡 Protección del comprador: reembolso completo antes de la entrega; consulte la garantía de cada producto y la Guía →", "/guide"),
    ("💬 Entrega manual: el vendedor procesa los pedidos a mano tras el pago; siga el progreso en Mis pedidos o contacte con Atención al cliente →", "/support"),
]

LEVEL_FR = [("Standard", ""), ("Argent", "-2 %"), ("Or", "-5 %"), ("Platine", "-8 %"), ("Or noir", "-12 %")]
LEVEL_DE = [("Standard", ""), ("Silber", "2 % Rabatt"), ("Gold", "5 % Rabatt"), ("Platin", "8 % Rabatt"), ("Schwarzgold", "12 % Rabatt")]
LEVEL_ES = [("Estándar", ""), ("Plata", "2 % de descuento"), ("Oro", "5 % de descuento"), ("Platino", "8 % de descuento"), ("Oro negro", "12 % de descuento")]

BLOBS_FR = {
    "usage_muse": """<ol>
          <li>Rendez-vous sur muse.ai et connectez-vous avec l'<b>e-mail et le mot de passe</b> figurant dans la livraison.</li>
          <li>Le format de livraison est généralement « e-mail - mot de passe - lien de code » ; si un code de vérification est requis, ouvrez le lien de code pour l'obtenir.</li>
          <li>Si le message « vous avez rejoint la liste d'attente » s'affiche, il s'agit généralement d'une restriction régionale — basculez sur un nœud réseau des <b>États-Unis ou du Canada</b> et reconnectez-vous.</li>
          <li>Certains comptes peuvent exiger une vérification par photo du visage ; l'acceptation ou le refus relève de la décision officielle de Muse.</li>
          <li>Un problème de compte ou besoin d'aide ? Contactez le vendeur sur QQ 1006025461 (en indiquant votre numéro de commande).</li>
        </ol>""",
    "usage_gemini": """<ol>
          <li>Assurez-vous que l'e-mail Google et l'e-mail de secours saisis lors de la commande sont corrects.</li>
          <li>Ajoutez le vendeur sur QQ 1006025461 en indiquant votre numéro de commande, et coopérez pour effectuer la recharge.</li>
          <li>Ensuite, vérifiez sur la page d'abonnement de votre compte Google que Gemini Pro est actif (24 mois).</li>
          <li>Vous n'avez jamais besoin de fournir le mot de passe de votre compte Google — refusez toute personne qui le demande.</li>
        </ol>""",
    "usage_grok": """<ol>
          <li>Rendez-vous sur grok.com et connectez-vous avec l'<b>e-mail et le mot de passe</b> figurant dans la livraison.</li>
          <li>L'e-mail et le mot de passe peuvent tous deux être modifiés ; <b>ne dissociez pas le compte de X</b>, sous peine d'affecter l'utilisation.</li>
          <li>L'offre 7 jours bénéficie d'une garantie de 1 jour ; l'offre 1 mois n'a aucune garantie ; les services de vérification de connexion ne sont pas couverts.</li>
          <li>Un problème de compte ou besoin d'aide ? Contactez le vendeur sur QQ 1006025461 (en indiquant votre numéro de commande).</li>
        </ol>""",
    "usage_gmail": """<ol>
          <li>Connectez-vous à Gmail avec le <b>compte e-mail et le mot de passe</b> figurant dans la livraison ; utilisez l'e-mail de secours et la 2FA lorsqu'une vérification est requise.</li>
          <li>Ce produit n'est couvert que pour la <b>première connexion dans les 24 heures</b> — connectez-vous et vérifiez dès réception.</li>
          <li>Une vérification par téléphone peut être requise à la connexion ; veuillez prévoir votre propre moyen de réception de SMS et utiliser un réseau stable et fiable.</li>
          <li>Un problème de compte ou besoin d'aide ? Contactez le vendeur sur QQ 1006025461 (en indiquant votre numéro de commande).</li>
        </ol>""",
    "usage_openai": """<ol>
          <li>Rendez-vous sur chatgpt.com et connectez-vous avec l'<b>e-mail et le mot de passe</b> figurant dans la livraison.</li>
          <li>Si un code de vérification est requis, ouvrez https://2fa.fun/ , saisissez la <b>clé secrète 2FA</b> figurant dans la livraison et cliquez sur « Obtenir le code » — les codes se renouvellent toutes les 30 secondes.</li>
          <li>L'offre ChatGPT Plus 1 mois couvre uniquement la <b>première connexion dans un délai de 1 heure</b> — connectez-vous et vérifiez dès réception ; l'offre ChatGPT Go 3 mois bénéficie d'une garantie de 3 jours.</li>
          <li>Un problème de compte ou besoin d'aide ? Contactez le vendeur sur QQ 1006025461 (en indiquant votre numéro de commande).</li>
        </ol>""",
    "usage_default": """<ul>
          <li>Suivez simplement le contenu de la livraison ci-dessus.</li>
          <li>Des questions ? Contactez le vendeur sur QQ 1006025461 en indiquant votre numéro de commande.</li>
        </ul>""",
    "legal_privacy": """
        <h2>Ce que nous collectons</h2>
        <ul>
          <li><b>Informations de compte</b> : votre e-mail d'inscription et votre mot de passe de connexion (conservés salés et hachés — nous ne pouvons pas les voir en clair).</li>
          <li><b>Informations de commande</b> : les produits et montants achetés, ainsi que l'e-mail de recharge, l'e-mail de secours, les coordonnées et le contenu de livraison que vous avez fournis lors de la commande.</li>
          <li><b>Portefeuille et échanges avec le service client</b> : l'historique des recharges et des dépenses, ainsi que le contenu de vos échanges avec le service client.</li>
          <li><b>Données de sécurité</b> : pour prévenir le piratage de compte et la fraude sur les commandes, le système enregistre des informations de sécurité telles que le nombre d'échecs de connexion.</li>
        </ul>
        <h2>À quoi cela sert</h2>
        <ul>
          <li>Traiter les commandes, effectuer les livraisons et assurer le service après-vente ;</li>
          <li>Protéger les comptes et les fonds ;</li>
          <li>Nous ne vendons ni ne louons vos informations personnelles, et ne les utilisons pas pour du profilage publicitaire.</li>
        </ul>
        <h2>Ce que nous ne ferons jamais</h2>
        <ul>
          <li>À aucun moment ce site ne vous <b>demandera le mot de passe de votre compte Google ou de tout autre compte tiers</b> — ne le communiquez à personne.</li>
          <li>Les paiements sont effectués via des plateformes de paiement tierces ; ce site ne touche ni ne conserve vos coordonnées bancaires ou vos mots de passe de paiement.</li>
        </ul>
        <h2>Conservation et suppression</h2>
        <p>Les enregistrements de commandes sont conservés un certain temps pour le service après-vente et la réconciliation. Pour supprimer votre compte et vos informations personnelles, contactez-nous via le Service client ou le QQ du vendeur 1006025461 ; nous traiterons votre demande après vérification de votre identité.</p>""",
    "legal_terms": """
        <h2>Nature du service</h2>
        <p>Ce site vend des produits numériques (services de recharge d'abonnement et comptes prêts à l'emploi), livrés manuellement par le vendeur, sans aucun envoi physique.</p>
        <h2>Commande et paiement</h2>
        <ul>
          <li>Les prix, le stock et la garantie des produits sont ceux affichés sur les pages produits.</li>
          <li>La réussite d'un paiement est déterminée par le statut de la commande ; si le système de paiement confirme avec retard, contactez le vendeur avec votre preuve de paiement pour une vérification manuelle — on ne vous demandera jamais de payer deux fois.</li>
          <li>Veillez à ce que l'e-mail de recharge, vos coordonnées et les autres informations soient exacts lors de la commande ; les pertes causées par des informations erronées fournies par l'acheteur sont à sa charge. Si vous constatez une erreur, contactez immédiatement le vendeur.</li>
        </ul>
        <h2>Garantie et remboursements</h2>
        <ul>
          <li>Les commandes non encore livrées peuvent être intégralement remboursées à tout moment en contactant le vendeur.</li>
          <li>La portée et la durée de garantie de chaque produit sont celles indiquées dans les badges des fiches produits et dans les <a href="/guide">règles après-vente du Guide</a>, qui font foi.</li>
          <li>Les commandes livrées hors du champ de la garantie ne sont pas remboursables.</li>
        </ul>
        <h2>Remarques pour l'acheteur</h2>
        <ul>
          <li>Après réception d'un compte prêt à l'emploi, connectez-vous et vérifiez-le pendant la période de garantie ;</li>
          <li>Les bannissements ou invalidations causés par un changement de mot de passe de votre fait, par le prêt du compte ou par un usage abusif (y compris la violation des règles de la plateforme cible) ne sont pas couverts par la garantie.</li>
        </ul>
        <h2>Modification des présentes conditions</h2>
        <p>Les mises à jour de ces conditions sont publiées sur cette page ; continuer à utiliser ce site vaut acceptation. Des questions ? Contactez-nous via le Service client ou le QQ du vendeur 1006025461.</p>""",
    "legal_cookies": """
        <h2>Quels cookies ce site utilise</h2>
        <ul>
          <li><b>Cookie de session de connexion (essentiel)</b> : il vous maintient connecté après la connexion et effectue les contrôles de sécurité des formulaires ; il expire lorsque vous vous déconnectez ou à la fin de sa durée de vie.</li>
          <li>La préférence « fermé » de l'annonce de la page d'accueil est stockée localement dans votre navigateur (localStorage) et n'est pas envoyée au serveur.</li>
        </ul>
        <h2>Ce que nous ne faisons pas</h2>
        <ul>
          <li>Aucun cookie publicitaire, aucun suivi intersites ;</li>
          <li>Aucun service tiers d'analyse ou de profilage des utilisateurs.</li>
        </ul>
        <h2>Pages tierces</h2>
        <p>Pendant le paiement, vous êtes redirigé vers des pages de paiement tierces telles qu'Alipay ; les cookies utilisés par ces pages relèvent des politiques propres à ces tiers, et non de ce site.</p>
        <h2>Vos choix</h2>
        <p>Vous pouvez effacer ou désactiver les cookies dans votre navigateur, mais sans cookies vous ne pourrez pas rester connecté, et donc ni commander ni consulter vos commandes.</p>""",
    "guide": '<div class="card guide"><h1>Guide d\'utilisation</h1>\n        <h2>1. Comment acheter</h2>\n        <ol>\n          <li><b>Inscription / connexion</b> : créez un compte avec votre e-mail (nécessaire pour commander et suivre vos commandes).</li>\n          <li><b>Choisissez un produit et commandez</b> : sur la page d\'accueil, cliquez sur « Acheter » sur un produit, remplissez les informations demandées et validez.</li>\n          <li><b>Paiement</b> : nous acceptons actuellement <b>Alipay</b>. Après un paiement réussi, la commande devient automatiquement « Payé / En attente de livraison » en environ 1 minute.</li>\n          <li><b>Attendez le vendeur</b> : le vendeur traite les commandes dans l\'ordre des paiements ; suivez l\'avancement à tout moment dans Mes commandes.</li>\n        </ol>\n        <h2>2. Recharge Gemini Pro (votre coopération est nécessaire)</h2>\n        <ol>\n          <li>Lors de la commande, indiquez l\'<b>e-mail Google à recharger</b> et un <b>e-mail de secours</b> — tous deux doivent être corrects.</li>\n          <li>Après le paiement, veuillez <b>ajouter le vendeur sur QQ (voir ci-dessous)</b> en mentionnant votre numéro de commande lors de l\'ajout — la recharge nécessite une coopération en temps réel avec le vendeur.</li>\n          <li>Une fois terminée, l\'abonnement est crédité sur votre propre compte Google, pour 24 mois.</li>\n        </ol>\n        <p class="hint">⚠️ Important : vous n\'avez <b>jamais besoin de fournir le mot de passe de votre compte Google</b>. Le vendeur ne vous demandera jamais votre mot de passe ; ne le donnez jamais à quiconque le demande.</p>\n        <h2>3. Comptes Muse prêts à l\'emploi (il suffit d\'attendre la livraison)</h2>\n        <ol>\n          <li>Lors de la commande, vous n\'avez qu\'à indiquer vos <b>coordonnées</b> pour que le vendeur puisse vous joindre.</li>\n          <li>Après le paiement, le vendeur envoie le <b>compte et le mot de passe dans votre commande</b> : ouvrez Mes commandes et retrouvez-les dans la section « Livraison » de la commande — copie en un clic.</li>\n          <li>Dès réception, connectez-vous rapidement à muse.ai pour vérifier que le compte fonctionne, et conservez vos identifiants en lieu sûr.</li>\n          <li>Les « tokens » ≈ la quantité de texte que l\'IA lit et écrit : 100 millions de tokens représentent environ plusieurs dizaines de millions de caractères chinois, et 1 milliard de tokens dure longtemps pour discuter et écrire au quotidien (estimations ; la consommation réelle dépend de la longueur des conversations).</li>\n        </ol>\n        <h2>4. Paiement et service après-vente</h2>\n        <ul>\n          <li>Si le statut de votre commande ne s\'est pas mis à jour longtemps après le paiement (plus de 10 minutes), contactez le vendeur sur QQ en indiquant votre numéro de commande.</li>\n          <li>Tous les statuts de commande sont ceux affichés sur la page Mes commandes.</li>\n        </ul>\n        <h2>Règles après-vente et de remboursement (commandez en toute confiance)</h2>\n        <ul>\n          <li><b>Remboursable avant la livraison</b> : à tout moment avant qu\'une commande soit livrée (marquée « Terminé »), contactez le vendeur pour annuler et obtenir un <b>remboursement intégral</b>.</li>\n          <li><b>Comment arrivent les remboursements</b> : pour les commandes payées avec le solde, le remboursement revient instantanément et automatiquement sur votre solde du site ; pour les commandes payées via Alipay, le vendeur rembourse via Alipay par le moyen de paiement d\'origine.</li>\n          <li><b>Recharges Gemini</b> : si la recharge échoue pour des raisons imputables au vendeur, remboursement intégral ; si un e-mail erroné que vous avez fourni a causé une recharge mal dirigée, contactez immédiatement le vendeur pour vérifier et résoudre le problème ; les abonnements crédités avec succès ne sont pas remboursables sans motif.</li>\n          <li><b>Comptes Muse prêts à l\'emploi</b> : première connexion garantie — connectez-vous et vérifiez rapidement après la livraison ; si la première connexion échoue, contactez immédiatement le vendeur (avec votre numéro de commande) — après vérification, nous le remplacerons ou vous rembourserons ; une fois la première connexion réussie, les problèmes ultérieurs du compte (y compris un changement de mot de passe de votre fait ou un usage abusif) ne sont pas couverts.</li>\n          <li>Tout le service après-vente passe par le <b>Service client</b> ou le QQ du vendeur (voir ci-dessous) — merci d\'indiquer votre numéro de commande.</li>\n        </ul>\n        <h2>5. Recharges du portefeuille et service client</h2>\n        <ul>\n          <li><b>Recharge</b> : dans Mon portefeuille, vous pouvez recharger à l\'avance via Alipay ; vos commandes ultérieures pourront alors être payées directement avec votre solde, sans redirection vers Alipay à chaque fois.</li>\n          <li><b>Service client</b> : l\'élément « Service client » de la navigation supérieure vous permet d\'écrire directement au vendeur ; après sa réponse, un badge numérique rouge apparaît dans la navigation.</li>\n          <li>Si une commande payée avec le solde est remboursée, le montant revient automatiquement sur votre solde.</li>\n        </ul>\n        </div>',
}

BLOBS_DE = {
    "usage_muse": """<ol>
          <li>Gehen Sie zu muse.ai und melden Sie sich mit der <b>E-Mail und dem Passwort</b> aus der Lieferung an.</li>
          <li>Das Lieferformat lautet in der Regel „E-Mail - Passwort - Code-Link“; wird ein Verifizierungscode benötigt, öffnen Sie den Code-Link, um ihn zu erhalten.</li>
          <li>Wenn „Sie sind der Warteliste beigetreten“ angezeigt wird, liegt das meist an einer regionalen Einschränkung — wechseln Sie zu einem Netzwerkknoten in den <b>USA oder Kanada</b> und melden Sie sich erneut an.</li>
          <li>Bei manchen Konten kann eine Verifizierung per Gesichtsfoto erforderlich sein; ob sie besteht, entscheidet Muse offiziell.</li>
          <li>Kontoprobleme oder Hilfe nötig? Wenden Sie sich per QQ 1006025461 an den Verkäufer (unter Angabe Ihrer Bestellnummer).</li>
        </ol>""",
    "usage_gemini": """<ol>
          <li>Stellen Sie sicher, dass die beim Bestellen angegebene Google-E-Mail und Ersatz-E-Mail korrekt sind.</li>
          <li>Fügen Sie den Verkäufer per QQ 1006025461 hinzu, geben Sie Ihre Bestellnummer an und wirken Sie an der Aufladung mit.</li>
          <li>Prüfen Sie danach auf der Abo-Seite Ihres Google-Kontos, dass Gemini Pro aktiv ist (24 Monate).</li>
          <li>Sie müssen zu keinem Zeitpunkt das Passwort Ihres Google-Kontos angeben — verweigern Sie es jeder Person, die danach fragt.</li>
        </ol>""",
    "usage_grok": """<ol>
          <li>Gehen Sie zu grok.com und melden Sie sich mit der <b>E-Mail und dem Passwort</b> aus der Lieferung an.</li>
          <li>E-Mail und Passwort können beide geändert werden; <b>trennen Sie die Verknüpfung des Kontos mit X nicht</b>, sonst kann die Nutzung beeinträchtigt werden.</li>
          <li>Der 7-Tage-Tarif hat 1 Tag Garantie; der 1-Monats-Tarif hat keine Garantie; Login-Prüfdienste sind nicht abgedeckt.</li>
          <li>Kontoprobleme oder Hilfe nötig? Wenden Sie sich per QQ 1006025461 an den Verkäufer (unter Angabe Ihrer Bestellnummer).</li>
        </ol>""",
    "usage_gmail": """<ol>
          <li>Melden Sie sich bei Gmail mit dem <b>E-Mail-Konto und Passwort</b> aus der Lieferung an; verwenden Sie bei Bedarf die Ersatz-E-Mail und die 2FA zur Verifizierung.</li>
          <li>Dieses Produkt ist nur für den <b>ersten Login innerhalb von 24 Stunden</b> abgedeckt — bitte melden Sie sich nach Erhalt sofort an und prüfen Sie das Konto.</li>
          <li>Beim Login kann eine Telefonverifizierung erforderlich sein; bitte sorgen Sie selbst für eine SMS-Empfangsmöglichkeit und nutzen Sie ein stabiles, vertrauenswürdiges Netzwerk.</li>
          <li>Kontoprobleme oder Hilfe nötig? Wenden Sie sich per QQ 1006025461 an den Verkäufer (unter Angabe Ihrer Bestellnummer).</li>
        </ol>""",
    "usage_openai": """<ol>
          <li>Gehen Sie zu chatgpt.com und melden Sie sich mit der <b>E-Mail und dem Passwort</b> aus der Lieferung an.</li>
          <li>Wird ein Verifizierungscode benötigt, öffnen Sie https://2fa.fun/ , geben Sie das <b>2FA-Geheimnis</b> aus der Lieferung ein und klicken Sie auf „Code abrufen“ — die Codes erneuern sich alle 30 Sekunden.</li>
          <li>Der ChatGPT Plus 1-Monats-Tarif deckt nur den <b>ersten Login innerhalb von 1 Stunde</b> ab — melden Sie sich nach Erhalt sofort an und prüfen Sie das Konto; der ChatGPT Go 3-Monats-Tarif hat 3 Tage Garantie.</li>
          <li>Kontoprobleme oder Hilfe nötig? Wenden Sie sich per QQ 1006025461 an den Verkäufer (unter Angabe Ihrer Bestellnummer).</li>
        </ol>""",
    "usage_default": """<ul>
          <li>Folgen Sie einfach dem obigen Lieferinhalt.</li>
          <li>Fragen? Wenden Sie sich per QQ 1006025461 unter Angabe Ihrer Bestellnummer an den Verkäufer.</li>
        </ul>""",
    "legal_privacy": """
        <h2>Welche Daten wir erheben</h2>
        <ul>
          <li><b>Kontodaten</b>: Ihre Registrierungs-E-Mail und Ihr Login-Passwort (gesalzen und gehasht gespeichert — wir können es nicht im Klartext sehen).</li>
          <li><b>Bestelldaten</b>: die gekauften Produkte und Beträge sowie die beim Bestellen angegebene Auflade-E-Mail, Ersatz-E-Mail, Kontaktdaten und Lieferinhalte.</li>
          <li><b>Guthaben- &amp; Kundendienst-Aufzeichnungen</b>: Auflade- / Ausgabenverlauf und Ihre Chatinhalte mit dem Kundenservice.</li>
          <li><b>Sicherheitsaufzeichnungen</b>: Zum Schutz vor Kontodiebstahl und Bestellbetrug zeichnet das System Sicherheitsinformationen wie die Anzahl fehlgeschlagener Logins auf.</li>
        </ul>
        <h2>Wofür sie verwendet werden</h2>
        <ul>
          <li>Bestellungen bearbeiten, Lieferungen abschließen und Kundendienst leisten;</li>
          <li>Konten und Gelder schützen;</li>
          <li>Wir verkaufen oder vermieten Ihre personenbezogenen Daten nicht und nutzen sie nicht für Werbeprofile.</li>
        </ul>
        <h2>Was wir niemals tun werden</h2>
        <ul>
          <li>Diese Website wird Sie zu keinem Zeitpunkt <b>nach dem Passwort Ihres Google-Kontos oder eines anderen Drittanbieter-Kontos fragen</b> — geben Sie es an niemanden weiter.</li>
          <li>Zahlungen werden über Zahlungsplattformen Dritter abgewickelt; diese Website berührt oder speichert weder Ihre Bankkartendaten noch Ihre Zahlungspasswörter.</li>
        </ul>
        <h2>Aufbewahrung &amp; Löschung</h2>
        <p>Bestelldaten werden eine Zeit lang für Kundendienst und Abgleich aufbewahrt. Um Ihr Konto und Ihre personenbezogenen Daten löschen zu lassen, wenden Sie sich über den Kundenservice oder per QQ 1006025461 an den Verkäufer; wir bearbeiten dies nach Identitätsprüfung.</p>""",
    "legal_terms": """
        <h2>Art des Dienstes</h2>
        <p>Diese Website verkauft digitale Produkte (Aufladedienste für Mitgliedschaften und Fertigkonten), die vom Verkäufer manuell geliefert werden, ohne physischen Versand.</p>
        <h2>Bestellung &amp; Zahlung</h2>
        <ul>
          <li>Produktpreise, Lagerbestand und Garantie richten sich nach den Angaben auf den Produktseiten.</li>
          <li>Ob eine Zahlung erfolgreich war, entscheidet der Bestellstatus; bestätigt das Zahlungssystem mit Verzögerung, wenden Sie sich mit Ihrem Zahlungsnachweis an den Verkäufer zur manuellen Prüfung — Sie werden niemals aufgefordert, zweimal zu zahlen.</li>
          <li>Bitte stellen Sie beim Bestellen sicher, dass Auflade-E-Mail, Kontaktdaten und andere Angaben korrekt sind; Verluste durch falsche Angaben des Käufers trägt der Käufer. Wenn Sie einen Fehler bemerken, wenden Sie sich sofort an den Verkäufer.</li>
        </ul>
        <h2>Garantie &amp; Erstattungen</h2>
        <ul>
          <li>Noch nicht gelieferte Bestellungen können jederzeit durch Kontaktaufnahme mit dem Verkäufer vollständig erstattet werden.</li>
          <li>Umfang und Dauer der Garantie jedes Produkts richten sich nach den Badges auf den Produktkarten und den <a href="/guide">Kundendienst-Regeln der Anleitung</a>, die maßgeblich sind.</li>
          <li>Gelieferte Bestellungen außerhalb des Garantieumfangs sind nicht erstattungsfähig.</li>
        </ul>
        <h2>Hinweise für Käufer</h2>
        <ul>
          <li>Bitte melden Sie sich nach Erhalt eines Fertigkontos innerhalb der Garantiezeit an und prüfen Sie es;</li>
          <li>Sperrungen oder Ungültigwerden durch eigenes Ändern des Passworts, Weiterverleihen des Kontos oder Missbrauch (einschließlich Verstoß gegen die Regeln der Zielplattform) sind von der Garantie nicht abgedeckt.</li>
        </ul>
        <h2>Änderungen dieser Bedingungen</h2>
        <p>Aktualisierungen dieser Bedingungen werden auf dieser Seite veröffentlicht; die weitere Nutzung dieser Website gilt als Zustimmung. Fragen? Wenden Sie sich über den Kundenservice oder per QQ 1006025461 an den Verkäufer.</p>""",
    "legal_cookies": """
        <h2>Welche Cookies diese Website verwendet</h2>
        <ul>
          <li><b>Login-Sitzungs-Cookie (erforderlich)</b>: hält Sie nach der Anmeldung eingeloggt und führt Sicherheitsprüfungen für Formulare durch; es erlischt bei der Abmeldung oder nach Ablauf seiner Lebensdauer.</li>
          <li>Die Einstellung „geschlossen“ der Ankündigung auf der Startseite wird lokal in Ihrem Browser gespeichert (localStorage) und nicht an den Server übertragen.</li>
        </ul>
        <h2>Was wir nicht tun</h2>
        <ul>
          <li>Keine Werbe-Cookies, kein seitenübergreifendes Tracking;</li>
          <li>Keine Drittanbieter-Analysen oder Nutzerprofil-Dienste.</li>
        </ul>
        <h2>Seiten Dritter</h2>
        <p>Während der Zahlung werden Sie auf Zahlungsseiten Dritter wie Alipay weitergeleitet; die dort verwendeten Cookies unterliegen den eigenen Richtlinien der Dritten, nicht dieser Website.</p>
        <h2>Ihre Wahlmöglichkeiten</h2>
        <p>Sie können Cookies in Ihrem Browser löschen oder deaktivieren, aber ohne Cookies können Sie nicht eingeloggt bleiben und somit weder bestellen noch Bestellungen ansehen.</p>""",
    "guide": '<div class="card guide"><h1>Anleitung</h1>\n        <h2>1. So funktioniert der Kauf</h2>\n        <ol>\n          <li><b>Registrieren / anmelden</b>: Erstellen Sie ein Konto mit Ihrer E-Mail (wird zum Bestellen und Verfolgen von Bestellungen benötigt).</li>\n          <li><b>Produkt wählen und bestellen</b>: Klicken Sie auf der Startseite bei einem Produkt auf „Jetzt kaufen“, füllen Sie die Angaben wie aufgefordert aus und senden Sie ab.</li>\n          <li><b>Bezahlen</b>: Wir akzeptieren derzeit <b>Alipay</b>. Nach erfolgreicher Zahlung wird die Bestellung innerhalb von etwa 1 Minute automatisch zu „Bezahlt / Lieferung ausstehend“.</li>\n          <li><b>Auf den Verkäufer warten</b>: Der Verkäufer bearbeitet Bestellungen in der Reihenfolge der Zahlung; verfolgen Sie den Fortschritt jederzeit unter Meine Bestellungen.</li>\n        </ol>\n        <h2>2. Gemini Pro Aufladung (Ihre Mitwirkung ist nötig)</h2>\n        <ol>\n          <li>Geben Sie beim Bestellen die <b>aufzuladende Google-E-Mail</b> und eine <b>Ersatz-E-Mail</b> an — beide müssen korrekt sein.</li>\n          <li>Bitte <b>fügen Sie den Verkäufer nach der Zahlung per QQ hinzu (siehe unten)</b> und geben Sie beim Hinzufügen Ihre Bestellnummer an — die Aufladung erfordert eine Zusammenarbeit mit dem Verkäufer in Echtzeit.</li>\n          <li>Nach Abschluss wird die Mitgliedschaft Ihrem eigenen Google-Konto gutgeschrieben, für 24 Monate.</li>\n        </ol>\n        <p class="hint">⚠️ Wichtig: Sie müssen zu keinem Zeitpunkt <b>das Passwort Ihres Google-Kontos angeben</b>. Der Verkäufer wird Sie niemals nach Ihrem Passwort fragen; geben Sie es niemals an jemanden weiter, der danach fragt.</p>\n        <h2>3. Muse Fertigkonten (einfach auf die Lieferung warten)</h2>\n        <ol>\n          <li>Beim Bestellen müssen Sie nur Ihre <b>Kontaktdaten</b> angeben, damit der Verkäufer Sie erreichen kann.</li>\n          <li>Nach der Zahlung sendet der Verkäufer <b>Konto und Passwort in Ihre Bestellung</b>: Öffnen Sie Meine Bestellungen und finden Sie sie im Abschnitt „Lieferung“ der Bestellung — mit einem Klick kopierbar.</li>\n          <li>Melden Sie sich nach Erhalt umgehend auf muse.ai an, um zu prüfen, ob das Konto funktioniert, und bewahren Sie die Zugangsdaten sicher auf.</li>\n          <li>„Token“ ≈ die Menge an Text, die die KI liest und schreibt: 100 Mio. Token entsprechen grob mehreren zehn Millionen chinesischen Schriftzeichen, und 1 Mrd. Token reicht für alltägliche Chats und Texte lange aus (Schätzungen; der tatsächliche Verbrauch hängt von der Gesprächslänge ab).</li>\n        </ol>\n        <h2>4. Zahlung &amp; Kundendienst</h2>\n        <ul>\n          <li>Wenn sich Ihr Bestellstatus lange nach der Zahlung nicht aktualisiert hat (über 10 Minuten), wenden Sie sich mit Ihrer Bestellnummer per QQ an den Verkäufer.</li>\n          <li>Alle Bestellstatus sind die auf der Seite Meine Bestellungen angezeigten.</li>\n        </ul>\n        <h2>Kundendienst- &amp; Erstattungsregeln (bestellen Sie mit Vertrauen)</h2>\n        <ul>\n          <li><b>Vor der Lieferung erstattbar</b>: Jederzeit, bevor eine Bestellung geliefert wurde (als „Abgeschlossen“ markiert), können Sie den Verkäufer kontaktieren, um zu stornieren und eine <b>volle Rückerstattung</b> zu erhalten.</li>\n          <li><b>So kommen Erstattungen an</b>: Bei mit Guthaben bezahlten Bestellungen geht die Erstattung sofort und automatisch auf Ihr Website-Guthaben zurück; bei per Alipay bezahlten Bestellungen erstattet der Verkäufer über Alipay auf dem ursprünglichen Zahlungsweg.</li>\n          <li><b>Gemini-Aufladungen</b>: Schlägt die Aufladung aus Gründen auf Verkäuferseite fehl, gibt es eine volle Rückerstattung; hat eine von Ihnen falsch angegebene E-Mail eine Fehlaufladung verursacht, wenden Sie sich sofort an den Verkäufer, um dies zu prüfen und zu klären; erfolgreich gutgeschriebene Mitgliedschaften sind ohne Grund nicht erstattungsfähig.</li>\n          <li><b>Muse Fertigkonten</b>: Erste Anmeldung garantiert — bitte führen Sie nach der Lieferung umgehend Ihre erste Anmeldung durch und prüfen Sie das Konto; wenn die erste Anmeldung nicht möglich ist, wenden Sie sich sofort an den Verkäufer (mit Ihrer Bestellnummer) — nach Prüfung ersetzen wir es oder erstatten den Betrag; nach erfolgreicher erster Anmeldung sind spätere Probleme des Kontos (einschließlich eigenen Änderns des Passworts oder Missbrauchs) nicht abgedeckt.</li>\n          <li>Der gesamte Kundendienst läuft über den <b>Kundenservice</b> oder per QQ an den Verkäufer (siehe unten) — bitte geben Sie Ihre Bestellnummer an.</li>\n        </ul>\n        <h2>5. Guthaben-Aufladungen &amp; Kundenservice</h2>\n        <ul>\n          <li><b>Aufladen</b>: Unter Mein Guthaben können Sie vorab per Alipay aufladen; spätere Bestellungen können dann direkt mit Ihrem Guthaben bezahlt werden, ohne jedes Mal zu Alipay weitergeleitet zu werden.</li>\n          <li><b>Kundenservice</b>: Über den Punkt „Kundenservice“ in der oberen Navigation können Sie dem Verkäufer direkt schreiben; nach seiner Antwort erscheint ein rotes Zahlen-Badge in der Navigation.</li>\n          <li>Wird eine mit Guthaben bezahlte Bestellung erstattet, geht der Betrag automatisch auf Ihr Guthaben zurück.</li>\n        </ul>\n        </div>',
}

BLOBS_ES = {
    "usage_muse": """<ol>
          <li>Vaya a muse.ai e inicie sesión con el <b>correo y la contraseña</b> de la entrega.</li>
          <li>El formato de entrega suele ser «correo - contraseña - enlace de código»; si se necesita un código de verificación, abra el enlace de código para obtenerlo.</li>
          <li>Si aparece «se ha unido a la lista de espera», suele tratarse de una restricción regional: cambie a un nodo de red de <b>EE. UU. o Canadá</b> e inicie sesión de nuevo.</li>
          <li>Algunas cuentas pueden requerir una verificación con foto del rostro; su aprobación la decide oficialmente Muse.</li>
          <li>¿Problemas con la cuenta o necesita ayuda? Contacte con el vendedor por QQ 1006025461 (indicando su número de pedido).</li>
        </ol>""",
    "usage_gemini": """<ol>
          <li>Asegúrese de que el correo de Google y el correo de respaldo indicados al pedir son correctos.</li>
          <li>Añada al vendedor por QQ 1006025461 indicando su número de pedido, y colabore para completar la recarga.</li>
          <li>Después, confirme en la página de suscripción de su cuenta de Google que Gemini Pro está activo (24 meses).</li>
          <li>Nunca necesita facilitar la contraseña de su cuenta de Google; rechace a cualquiera que se la pida.</li>
        </ol>""",
    "usage_grok": """<ol>
          <li>Vaya a grok.com e inicie sesión con el <b>correo y la contraseña</b> de la entrega.</li>
          <li>Tanto el correo como la contraseña pueden cambiarse; <b>no desvincule la cuenta de X</b>, o el uso podría verse afectado.</li>
          <li>El plan de 7 días tiene una garantía de 1 día; el plan de 1 mes no tiene garantía; los servicios de comprobación de inicio de sesión no están cubiertos.</li>
          <li>¿Problemas con la cuenta o necesita ayuda? Contacte con el vendedor por QQ 1006025461 (indicando su número de pedido).</li>
        </ol>""",
    "usage_gmail": """<ol>
          <li>Inicie sesión en Gmail con la <b>cuenta de correo y la contraseña</b> de la entrega; utilice el correo de respaldo y la 2FA cuando se requiera verificación.</li>
          <li>Este producto solo está cubierto para el <b>primer inicio de sesión dentro de las 24 horas</b>; inicie sesión y verifíquela en cuanto la reciba.</li>
          <li>Es posible que se requiera verificación telefónica al iniciar sesión; prevea su propio método de recepción de SMS y utilice una red estable y de confianza.</li>
          <li>¿Problemas con la cuenta o necesita ayuda? Contacte con el vendedor por QQ 1006025461 (indicando su número de pedido).</li>
        </ol>""",
    "usage_openai": """<ol>
          <li>Vaya a chatgpt.com e inicie sesión con el <b>correo y la contraseña</b> de la entrega.</li>
          <li>Si se necesita un código de verificación, abra https://2fa.fun/ , introduzca la <b>clave secreta 2FA</b> de la entrega y haga clic en «Obtener código»; los códigos se renuevan cada 30 segundos.</li>
          <li>El plan ChatGPT Plus de 1 mes cubre solo el <b>primer inicio de sesión dentro de 1 hora</b>; inicie sesión y verifíquelo en cuanto lo reciba; el plan ChatGPT Go de 3 meses tiene una garantía de 3 días.</li>
          <li>¿Problemas con la cuenta o necesita ayuda? Contacte con el vendedor por QQ 1006025461 (indicando su número de pedido).</li>
        </ol>""",
    "usage_default": """<ul>
          <li>Simplemente siga el contenido de la entrega anterior.</li>
          <li>¿Alguna duda? Contacte con el vendedor por QQ 1006025461 indicando su número de pedido.</li>
        </ul>""",
    "legal_privacy": """
        <h2>Qué recopilamos</h2>
        <ul>
          <li><b>Datos de la cuenta</b>: su correo de registro y su contraseña de acceso (almacenada con sal y hash; no podemos verla en texto claro).</li>
          <li><b>Datos del pedido</b>: los productos e importes adquiridos, además del correo de recarga, el correo de respaldo, los datos de contacto y el contenido de entrega que facilitó al pedir.</li>
          <li><b>Registros de la cartera y de atención al cliente</b>: el historial de recargas y gastos, y el contenido de sus conversaciones con atención al cliente.</li>
          <li><b>Registros de seguridad</b>: para prevenir el robo de cuentas y el fraude en los pedidos, el sistema registra información de seguridad como el número de inicios de sesión fallidos.</li>
        </ul>
        <h2>Para qué se utiliza</h2>
        <ul>
          <li>Procesar pedidos, completar entregas y prestar el servicio posventa;</li>
          <li>Mantener seguras las cuentas y los fondos;</li>
          <li>No vendemos ni alquilamos su información personal, ni la utilizamos para elaborar perfiles publicitarios.</li>
        </ul>
        <h2>Lo que nunca haremos</h2>
        <ul>
          <li>En ningún momento este sitio le <b>pedirá la contraseña de su cuenta de Google ni de ninguna otra cuenta de terceros</b>; no se la facilite a nadie.</li>
          <li>Los pagos se realizan a través de plataformas de pago de terceros; este sitio nunca toca ni almacena los datos de su tarjeta bancaria ni sus contraseñas de pago.</li>
        </ul>
        <h2>Conservación y eliminación</h2>
        <p>Los registros de pedidos se conservan durante un tiempo para el servicio posventa y la conciliación. Para eliminar su cuenta y su información personal, contacte con nosotros mediante Atención al cliente o el QQ del vendedor 1006025461; lo tramitaremos tras verificar su identidad.</p>""",
    "legal_terms": """
        <h2>Naturaleza del servicio</h2>
        <p>Este sitio vende productos digitales (servicios de recarga de suscripciones y cuentas listas para usar), entregados manualmente por el vendedor, sin envío físico.</p>
        <h2>Pedidos y pago</h2>
        <ul>
          <li>Los precios, el stock y la garantía de los productos son los mostrados en las páginas de producto.</li>
          <li>La confirmación de un pago se determina por el estado del pedido; si el sistema de pago confirma con retraso, contacte con el vendedor con su justificante de pago para una verificación manual; nunca se le pedirá que pague dos veces.</li>
          <li>Asegúrese de que el correo de recarga, los datos de contacto y demás información sean correctos al pedir; las pérdidas causadas por información incorrecta facilitada por el comprador correrán por su cuenta. Si detecta un error, contacte de inmediato con el vendedor.</li>
        </ul>
        <h2>Garantía y reembolsos</h2>
        <ul>
          <li>Los pedidos aún no entregados pueden reembolsarse íntegramente en cualquier momento contactando con el vendedor.</li>
          <li>El alcance y el plazo de garantía de cada producto son los indicados en las insignias de las tarjetas de producto y en las <a href="/guide">normas posventa de la Guía</a>, que prevalecen.</li>
          <li>Los pedidos entregados fuera del alcance de la garantía no son reembolsables.</li>
        </ul>
        <h2>Notas para el comprador</h2>
        <ul>
          <li>Tras recibir una cuenta lista para usar, inicie sesión y verifíquela dentro del periodo de garantía;</li>
          <li>Los bloqueos o la invalidez causados por cambiar usted mismo la contraseña, prestar la cuenta o hacer un uso indebido (incluida la infracción de las normas de la plataforma de destino) no están cubiertos por la garantía.</li>
        </ul>
        <h2>Cambios en estos términos</h2>
        <p>Las actualizaciones de estos términos se publican en esta página; seguir utilizando este sitio implica su aceptación. ¿Dudas? Contacte con nosotros mediante Atención al cliente o el QQ del vendedor 1006025461.</p>""",
    "legal_cookies": """
        <h2>Qué cookies utiliza este sitio</h2>
        <ul>
          <li><b>Cookie de sesión de inicio de sesión (esencial)</b>: le mantiene conectado tras iniciar sesión y realiza comprobaciones de seguridad en los formularios; caduca cuando cierra sesión o al finalizar su vida útil.</li>
          <li>La preferencia de «cerrado» del anuncio de la página de inicio se guarda localmente en su navegador (localStorage) y no se sube al servidor.</li>
        </ul>
        <h2>Lo que no hacemos</h2>
        <ul>
          <li>Sin cookies publicitarias, sin rastreo entre sitios;</li>
          <li>Sin servicios de análisis de terceros ni de elaboración de perfiles de usuario.</li>
        </ul>
        <h2>Páginas de terceros</h2>
        <p>Durante el pago se le redirige a páginas de pago de terceros como Alipay; las cookies que esas páginas utilizan se rigen por las políticas propias de esos terceros, no por este sitio.</p>
        <h2>Sus opciones</h2>
        <p>Puede borrar o desactivar las cookies en su navegador, pero con las cookies desactivadas no podrá mantenerse conectado y, por tanto, no podrá pedir ni consultar pedidos.</p>""",
    "guide": '<div class="card guide"><h1>Guía de uso</h1>\n        <h2>1. Cómo funciona la compra</h2>\n        <ol>\n          <li><b>Registrarse / iniciar sesión</b>: cree una cuenta con su correo electrónico (necesaria para pedir y seguir los pedidos).</li>\n          <li><b>Elija un producto y pida</b>: en la página de inicio, haga clic en «Comprar ahora» en un producto, complete los datos que se le piden y envíe el pedido.</li>\n          <li><b>Pague</b>: actualmente aceptamos <b>Alipay</b>. Tras un pago correcto, el pedido pasa automáticamente a «Pagado / Pendiente de entrega» en aproximadamente 1 minuto.</li>\n          <li><b>Espere al vendedor</b>: el vendedor procesa los pedidos por orden de pago; siga el progreso en cualquier momento en Mis pedidos.</li>\n        </ol>\n        <h2>2. Recarga de Gemini Pro (necesita su colaboración)</h2>\n        <ol>\n          <li>Al pedir, indique el <b>correo de Google a recargar</b> y un <b>correo de respaldo</b>; ambos deben ser correctos.</li>\n          <li>Tras el pago, <b>añada al vendedor por QQ (véase abajo)</b> indicando su número de pedido al añadirlo; la recarga requiere una colaboración en tiempo real con el vendedor.</li>\n          <li>Al finalizar, la suscripción se acredita en su propia cuenta de Google, por 24 meses.</li>\n        </ol>\n        <p class="hint">⚠️ Importante: <b>nunca necesita facilitar la contraseña de su cuenta de Google</b> en ningún momento. El vendedor nunca le pedirá su contraseña; no se la dé nunca a quien se la pida.</p>\n        <h2>3. Cuentas Muse listas para usar (solo hay que esperar la entrega)</h2>\n        <ol>\n          <li>Al pedir, solo necesita indicar sus <b>datos de contacto</b> para que el vendedor pueda localizarle.</li>\n          <li>Tras el pago, el vendedor enviará la <b>cuenta y la contraseña a su pedido</b>: abra Mis pedidos y encuéntrelas en la sección «Entrega» del pedido, con copia en un clic.</li>\n          <li>Al recibirla, inicie sesión cuanto antes en muse.ai para confirmar que la cuenta funciona, y guarde bien las credenciales.</li>\n          <li>Los «tokens» ≈ la cantidad de texto que la IA lee y escribe: 100 millones de tokens equivalen aproximadamente a varias decenas de millones de caracteres chinos, y 1 000 millones de tokens duran mucho tiempo para chatear y escribir a diario (estimaciones; el consumo real depende de la longitud de las conversaciones).</li>\n        </ol>\n        <h2>4. Pago y servicio posventa</h2>\n        <ul>\n          <li>Si el estado de su pedido no se ha actualizado mucho tiempo después del pago (más de 10 minutos), contacte con el vendedor por QQ indicando su número de pedido.</li>\n          <li>Todos los estados de los pedidos son los mostrados en la página Mis pedidos.</li>\n        </ul>\n        <h2>Normas de posventa y reembolso (pida con confianza)</h2>\n        <ul>\n          <li><b>Reembolsable antes de la entrega</b>: en cualquier momento antes de que un pedido se entregue (se marque como «Completado»), contacte con el vendedor para cancelarlo y obtener un <b>reembolso completo</b>.</li>\n          <li><b>Cómo llegan los reembolsos</b>: en los pedidos pagados con saldo, el reembolso vuelve instantánea y automáticamente a su saldo del sitio; en los pedidos pagados mediante Alipay, el vendedor reembolsa a través de Alipay por la vía de pago original.</li>\n          <li><b>Recargas de Gemini</b>: si la recarga falla por motivos imputables al vendedor, reembolso completo; si un correo incorrecto facilitado por usted causó una recarga mal dirigida, contacte de inmediato con el vendedor para verificarlo y resolverlo; las suscripciones acreditadas con éxito no son reembolsables sin motivo.</li>\n          <li><b>Cuentas Muse listas para usar</b>: primer inicio de sesión garantizado — inicie sesión y verifíquela cuanto antes tras la entrega; si el primer inicio de sesión falla, contacte de inmediato con el vendedor (con su número de pedido); tras la verificación, la reemplazaremos o le reembolsaremos; una vez realizado el primer inicio de sesión, los problemas posteriores de la cuenta (incluidos cambiar usted mismo la contraseña o un uso indebido) no están cubiertos.</li>\n          <li>Todo el servicio posventa se gestiona mediante <b>Atención al cliente</b> o el QQ del vendedor (véase abajo); incluya su número de pedido.</li>\n        </ul>\n        <h2>5. Recargas de la cartera y atención al cliente</h2>\n        <ul>\n          <li><b>Recarga</b>: en Mi cartera puede recargar por adelantado mediante Alipay; después podrá pagar los pedidos directamente con su saldo, sin redirigirse a Alipay cada vez.</li>\n          <li><b>Atención al cliente</b>: el elemento «Atención al cliente» de la navegación superior le permite escribir directamente al vendedor; cuando el vendedor responda, aparecerá una insignia numérica roja en la navegación.</li>\n          <li>Si un pedido pagado con saldo se reembolsa, el importe vuelve automáticamente a su saldo.</li>\n        </ul>\n        </div>',
}

STRINGS_FR.update({
    "hero.tagline": "Les grands abonnements IA au même endroit — recharges et comptes prêts à l'emploi",
    "hero.cta": "Voir les produits",
})
STRINGS_DE.update({
    "hero.tagline": "Die großen KI-Abos an einem Ort — Aufladung und Fertigkonten",
    "hero.cta": "Produkte ansehen",
})
STRINGS_ES.update({
    "hero.tagline": "Las principales membresías de IA en un solo lugar — recargas y cuentas listas",
    "hero.cta": "Ver productos",
})
