from telebot import types


def create_main_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item0 = types.InlineKeyboardButton("💸 Купить", callback_data='купить')
    item1 = types.InlineKeyboardButton("📲 Профиль", callback_data='профиль')
    item2 = types.InlineKeyboardButton("⚙️ Калькулятор", callback_data='калькулятор')
    item3 = types.InlineKeyboardButton("🆘 Помощь", callback_data='помощь')
    item4 = types.InlineKeyboardButton("📌 Правила", callback_data='правила')
    item5 = types.InlineKeyboardButton("🛒 Наличие товара", callback_data='наличие')
    item7 = types.InlineKeyboardButton("🛒 Группа ВК", callback_data='группа_вк')
    item6 = types.InlineKeyboardButton(" Вызвать Администратора", callback_data='админ')
    # markup.row(item0)
    markup.row(item5)
    markup.row(item1, item2)
    markup.row(item3, item4)
    markup.row(item7, item6)
    return markup


def create_back_to_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("🔙 Назад в меню", callback_data='назад_в_меню')
    markup.add(item1)
    item1 = types.InlineKeyboardButton("💸 Купить", callback_data='купить')
    markup.add(item1)
    return markup


def create_del_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("❌ Закрыть", callback_data='закрыть')
    markup.add(item1)
    return markup


def create_admin_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("🔱 Рассылка", callback_data='ADMрассылка')
    item2 = types.InlineKeyboardButton("❌ Бан", callback_data='ADMбан')
    item3 = types.InlineKeyboardButton("ℹ️ Инфо о пользователе", callback_data='ADMинфо_юзер')
    item4 = types.InlineKeyboardButton("✅ Разбан", callback_data='ADMразбан')
    markup.row(item1, item2)
    markup.row(item3, item4)
    return markup


def create_buy_menu_markup(payment_id, url):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("💳Оплатить", url=url)
    item2 = types.InlineKeyboardButton("⚠️Проверить платеж", callback_data=f"проверить_платеж:{payment_id}")
    item3 = types.InlineKeyboardButton("test pay", callback_data=f"проверить_платежTEST:{payment_id}")
    markup.row(item1, item2)
    markup.row(item3)
    return markup
    markup = create_main_menu_markup()
    item7 = types.InlineKeyboardButton("🛒 Группа ВК", callback_data='группа_вк')
    bot.answer_callback_query(call.id)  # Убирает "зависание" кнопки
    bot.send_message(call.message.chat.id, "Наша группа ВКонтакте: https://vk.com/keytrade_ru")
    return markup

