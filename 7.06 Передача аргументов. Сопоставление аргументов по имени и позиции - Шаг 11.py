"""
В HTML используются специальные теги для определения заголовков в веб-странице.

Всего существует шесть тегов заголовков HTML:

<h1> - заголовок первого уровня;
<h2> - заголовок второго уровня;
<h3> - заголовок третьего уровня;
<h4> - заголовок четвертого уровня;
<h5> - заголовок пятого уровня;
<h6> - заголовок шестого уровня.

Разница между заголовками только в размере.

Ваша задача создать функцию make_header, которая принимает

обязательный параметр - строку, которую нужно обернуть в тег заголовка
необязательный числовой параметр - уровень заголовка, по умолчанию принимает значение 1.

Функция make_header должна возвращать переданную строку в обернутый тег заголовка определенного уровня

Ваша задача дописать только тело функции make_header
"""


def make_header(text: str, size: int = 1) -> str:
    """
    Оборачивает строку в тег заголовка.
    :param text: Текст.
    :param size: Размер (уровень) заголовка.
    :return: Обернутый в тег текст.
    """
    return f'<h{size}>{text}</h{size}>'


assert make_header('Нет') == '<h1>Нет</h1>'
assert make_header('Bella Ciao', 4) == '<h4>Bella Ciao</h4>'
assert make_header('Go little rock star', 6) == '<h6>Go little rock star</h6>'
assert make_header('Девальвации не будет. Твердо и четко') == '<h1>Девальвации не будет. Твердо и четко</h1>'

print('Все проверки пройдены!')
