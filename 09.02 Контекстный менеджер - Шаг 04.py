"""
В вашем распоряжении имеется файл 'lorem.txt'. Ваша задача найти сколько уникальных слов используется в его
этом тексте, при этом регистр букв не нужно учитывать. Это значит, что слова Lorem и loRem являются эквивалентными.

Например, если перед вами был бы такой текст:

Привет как дела
привет хорошо
то здесь четыре уникальных слова.

Между словами в файле стоят только пробелы и переносы строк, других разделителей нет.

В качестве ответа укажите количество уникальных слов
"""
from string import punctuation


def count_uniq(file_name: str) -> int | str:
    """Находит сколько уникальных слов используется в тексте переданного файла"""

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            result = len({word.strip(punctuation).lower() for line in file for word in line.split()})

    except FileNotFoundError:
        return f'Файл "{file_name}" не найден'

    if result == 0:
        return f'Файл "{file_name}" пуст'

    return result


print(count_uniq('lorem.txt'))
