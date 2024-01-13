"""
Заменяем символы

Напишите функцию replace, которая принимает три параметра:

обязательный строковый параметр text - текст, в котором необходимо выполнить замены;
обязательный строковый параметр old - строка поиска для замены;
необязательный строковый параметр new - значение замены для найденного значения old. По умолчанию равен пустой строке.

Функция replace должна возвращать новую строку, в которой все символы old были заменены на new.
При замене регистр букв должен учитываться

Ваша задача дописать только тело функции replace
"""


def replace(text: str, old: str, new: str = '') -> str:
    """
    Возвращает новую строку, в которой все символы old были заменены на new.
    :param text: Текст, в котором нужно заменить символы.
    :param old: Заменяемый символ.
    :param new: Новый символ.
    :return: Текст с замененными символами.
    """
    # return ''.join([new if char == old else char for char in text])
    # return new.join(text.split(old))
    return text.replace(old, new)

assert replace('Нет', 'т') == 'Не'
assert replace('Bella Ciao', 'a') == 'Bell Cio'
assert replace('nobody; i myself farewell analysis', 'l', 'z') == 'nobody; i mysezf farewezz anazysis'
assert replace('commend me to my kind lord meaning', 'M', 'w') == 'commend me to my kind lord meaning'

print('Все проверки пройдены!')
