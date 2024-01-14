"""
Напишите функцию find_lines_len_more_6, которая принимает имя файла и находит количество строк, длиннее 6 символов.
Не забывайте исключать знак переноса на новую строку, стоящий в конце строки.

Функция find_lines_len_more_6 должна возвращать найденное количество строк

Ваша задача написать только определение функции find_lines_len_more_6
"""


def find_lines_len_more_6(file_name: str) -> int | str:
    """Находит количество строк, длиннее 6 символов."""

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            result = sum(1 for line in file if len(line.strip()) > 6)

    except FileNotFoundError:
        return f'Файл "{file_name}" не найден'

    if result == 0:
        return f'Файл "{file_name}" пуст или не содержит строк, длиннее 6 символов'

    return result
