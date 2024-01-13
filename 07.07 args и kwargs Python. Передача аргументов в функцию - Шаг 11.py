"""
Напишите функцию only_one_positive, которая принимает произвольное количество числовых аргументов и возвращает True,
когда из всех переданных значений только одно положительное, в противном случае верните False

Вам необходимо написать только определение функции only_one_positive
"""


def only_one_positive(*args: int | float) -> bool:
    """
    Возвращает True, когда из всех значений *args только одно положительное, в противном случае - False
    :param args: Неопределенное количество неименованных параметров.
    :return: Bool.
    """
    return True if sum(True for n in args if n > 0) == 1 else False


assert only_one_positive(1, 2) == False
assert only_one_positive(-1, 0, -3, 5, -3) == True
assert only_one_positive() == False

print('Все проверки пройдены!')
