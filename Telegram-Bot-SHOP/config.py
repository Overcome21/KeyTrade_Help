bot_token = "7088537132:AAGWu_AsG-KharILQNh9AxTyh0Ya4k87WHI"
y_token = "0D54056E6E17DD95D67BDA0E63C4BD61FCFB40C7B9488BF74B206ABD629561CC"
card = "4100119019335028"
support = "overcome21"
support_id = "929877709,730872773" # id support

# ~~CLIENT TEXT~~

main_menu_text = "👋🏻 Добро пожаловать KeyTrade | Игры и программы, {name}!\n🧨 Здесь ты можешь приобрести нужный тебе товар!"
# NAME - для замены

profile_text = """👤 Профиль
🔮 Ваше Имя: {first_name}
⚙️ Ваш ID: {user_id}
🔱 Ваш Username: @{username}
📌 Дата регистрации: {reg_date}
💳 Количество покупок: {count}
"""

order_capt = """⛓ Ожидаем платеж... (кнопка действительна 15 минут)

💸 Конечная сумма: {price}
🛍 Товар(ы): {items}
⚙️ Номер заказа: <code>{payment_id}</code>"""

buy_menu_text = "🛍 Введите ID товаров через пробел, например: 1 5 (товар товар)\n(для отмены введите 0)\n\n\n🔒 Покупая товар, вы автоматически соглашаетесь с правилами магазина (ознакомиться с ними можно в главном меню)."
calc_menu_text = "Для рассчета отправьте ID товаров через пробел с командой !calc, например: !calc 1 5"
address_menu_text = "🌠 Введите адрес электроной почты для доставки"
order_capt_1 = "⛔️Заказы можно делать раз в 2 минуты!"
order_capt_2 = "📵Неверный формат ввода или товара нет в наличии!\n(за 1 раз можно купить не более 5 товаров)"
paid_text = "✅оплачено, с вами свяжется администратор (@{support}) в течении 5 минут."
rules = """🔒 Правила
...
🔒 Оплата

Оплата принимается через банковские карты, электронные кошельки и VK Pay.
Заказ считается подтверждённым после получения оплаты.

🚀 Доставка

Ключи отправляются автоматически в личные сообщения ВКонтакте или на email.
Если ключ не получен, проверьте папку "Спам" или обратитесь в поддержку.

✅ Возврат

Возврат возможен при неисправности ключа с предоставлением доказательств (скриншот ошибки, номер заказа).
Возврат не осуществляется, если:
Ошибка связана с выбором платформы.
Нарушены условия использования ключа.
Данные ввода указаны неверно.

❗ Ответственность

Покупатель обязан ознакомиться с правилами и требованиями перед покупкой.
Покупая товар, вы соглашаетесь с условиями магазина.

"""

# ~~ADMIN TEXT~~
adm_menu_text = "⚡️ADMIN PANEL"
canceled_action = "❌ Действие отменено"
success_ban = "🔱 Вы успешно забанили {user}"
success_pardon = "🔱 Вы успешно разбанили {user}!"
error_text = "❌ Ошибка"
sender_started = "✅ Рассылка началась!"
sender_ended = "🔱 Рассылка завершена!\n📤 Отправлено {success_sent} сообщений!"
notification = "Новый пользователь -> @{username}"
new_order_capt = """ℹ️ Новый заказ!

👤 Покупатель: @{username}
💸 Сумма: {price}
🛍 Товары: {items}
-> {processed_items}
🏠 Адрес: {address}
⚙️ Айди заказа: {payment_id}
🕰 Время заказа: {purchase_date}"""
