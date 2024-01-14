"""
Ваша задача найти в файле 'numbers.txt'

1. количество трехзначных чисел;
2. сумму двухзначных чисел.

В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов.
Сперва количество, потом сумма
"""


def solving_some_problem(file_name: str) -> str | tuple:
    """
    Находит:
    1. количество трехзначных чисел;
    2. сумму двухзначных чисел.
    :param file_name: Имя открываемого файла, в котором нужно найти ответы.
    :return:
    """

    # try:
    #     with open(file_name, 'r', encoding='utf-8') as file:
    #         lines = file.readlines()
    # except FileNotFoundError:
    #     return f'Файл "{file_name}" не найден'
    #
    # if not lines:
    #     return f'Файл "{file_name}" пуст'
    #
    # qty_of_len_3 = sum(1 for line in lines if len(line.strip()) == 3)
    # sum_of_len_2 = sum(int(line.strip()) for line in lines if len(line.strip()) == 2)
    #
    # return qty_of_len_3, sum_of_len_2

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            qty_of_len_3 = 0
            sum_of_len_2 = 0

            for line in file:
                stripped_line = line.strip()
                if len(stripped_line) == 3:
                    qty_of_len_3 += 1
                elif len(stripped_line) == 2:
                    sum_of_len_2 += int(stripped_line)

    except FileNotFoundError:
        return f'Файл "{file_name}" не найден'

    if qty_of_len_3 == 0 and sum_of_len_2 == 0:
        return f'Файл "{file_name}" пуст'

    return qty_of_len_3, sum_of_len_2


print(*solving_some_problem('numbers.txt'))
