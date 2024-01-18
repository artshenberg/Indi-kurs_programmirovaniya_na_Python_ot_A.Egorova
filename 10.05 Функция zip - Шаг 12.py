"""
Напишите функцию zip_with_function(), которая принимает список списков и функцию, которая принимает несколько аргументов
и возвращает значение. Функция zip_with_function() должна использовать функцию zip() для объединения списков в кортежи,
а затем применять заданную функцию к кортежам из соответствующих позиций каждого списка. Результатом должен быть новый
список, содержащий значения, возвращаемые функцией для каждой комбинации элементов.

Например, имеется функция

def get_sum_two_numbers(a, b):
    return a + b
Тогда вызов

zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers)
должен вернуть список [4, 7, 12].

Ваша задача написать только определение функции zip_with_function

Sample Input:

Sample Output:

GOOD
"""
# Напишите определение функции zip_with_function
from typing import List, Callable, Union


def zip_with_function(lst: list[list[Union[str, int]]], func: Callable[..., Union[str, int]]) -> List[Union[str, int]]:
    """
    Принимает список списков lst и функцию func, которая принимает несколько аргументов и возвращает значение.
    Использует функцию zip() для объединения списков в кортежи, а затем применяет заданную функцию к кортежам из
    соответствующих позиций каждого списка.
    :param lst: Список списков строк или целых чисел
    :param func: Функция
    :return: Список результатов
    """
    return list(map(lambda args: func(*args), zip(*lst)))


def combine_strings(a: str, b: str) -> str:
    return a + b


def get_sum_two_numbers(a: int, b: int) -> int:
    return a + b


def get_sum_three_numbers(a: int, b: int, c: int) -> int:
    return a + b + c


assert zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers) == [4, 7, 12]
assert zip_with_function([[10, 20], [30, 0]], get_sum_two_numbers) == [40, 20]
assert zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers) == [10, 15, 20]
assert zip_with_function([[1, 2, 3], [4, 5, 6], [7, 8, 9]], get_sum_three_numbers) == [12, 15, 18]
assert zip_with_function([["a", "b"], ["1", "2"]], combine_strings) == ['a1', 'b2']
print('GOOD')
