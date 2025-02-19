from data import get_goods, get_good_by_id


def calculate(ids):
    text = ""
    res = 0
    for i, _id in enumerate(ids):
        good = get_good_by_id(_id)
        if not good:
            continue
        res += good[2]
        text += f"{good[1]} ({good[2]})"
        if i + 1 == len(ids):
            break
        text += " + "
    text += f" = {res}"
    return text, res


def create_str_table(data):
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [str(data[row][col]) for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)
    lines = []

    for i, row in enumerate(range(rows)):
        result = []
        for col in range(cols):
            item = str(data[row][col]).rjust(col_width[col])
            result.append(item)

        lines.append(' | '.join(result))

        if not i:
            lines.append(separator)

    return '\n'.join(lines)


def get_availability_text():
    goods = get_goods()
    # Формируем список товаров с использованием ссылки
    items = [f"*ID:* {item[0]}  *Товары:* {item[1]} *Цена:* {item[2]} [ссылка]({item[3]})" for item in goods]
    
    # Формируем текст для отправки
    text = "\n\n".join(items)
    
    # Ограничиваем длину текста
    max_length = 1024
    if len(text) > max_length:
        # Обрезаем текст и добавляем многоточие для первой части
        first_part = text[:max_length-3] + "..."
        # Остальная часть текста
        second_part = text[max_length-3:]
        return first_part, second_part
    return text, None  # Если текст подходит по длине

def get_availability_text():
    goods = get_goods()
    # Формируем список товаров с использованием ссылки
    items = [
        f"*ID:* {item[0]}  *Товары:* {item[1]} *Цена:* {item[2]} [ссылка]({item[3]})" 
        for item in goods
    ]

    # Разделяем на группы по 5 товаров
    chunk_size = 9
    chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

    # Формируем текст для каждой группы
    texts = ["\n\n".join(chunk) for chunk in chunks]
    return texts

def get_availability_text():
    goods = get_goods()
    # Формируем список товаров с использованием ссылки
    items = [
        f"*ID:* {item[0]}  *Товары:* {item[1]} *Цена:* {item[2]} руб [описание товара]({item[3]})" 
        for item in goods
    ]

    # Разделяем на группы по 5 товаров
    chunk_size = 9
    chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

    # Формируем текст для каждой группы
    texts = ["\n\n".join(chunk) for chunk in chunks]
    return texts

def send_availability_message(call):
    texts = get_availability_text()

    # Отправляем сообщения по очереди
    for index, text in enumerate(texts):
        if index == 0:
            # Первое сообщение с изменением подписи
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.id,
                caption=f'\ud83d\uded2Товары:\n{text}',
                parse_mode="markdown"
            )
        else:
            # Остальные сообщения отправляются как новые
            bot.send_message(
                chat_id=call.message.chat.id,
                text=f'\ud83d\uded2Товары (продолжение):\n{text}',
                parse_mode="markdown"
            )

        # Задержка между отправкой сообщений (по необходимости)
        import time
        time.sleep(2)




def convert_text(text):
    lines = list(map(str.strip, text.split("\n")))
    res = ""
    for line in lines:
        if not line:
            res += "\n"
        res += "\n"
        res += line
    return res
