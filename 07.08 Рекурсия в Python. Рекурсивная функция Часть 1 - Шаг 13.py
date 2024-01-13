"""
Напишите функцию list_sum_recursive, которая принимает на вход список из целых чисел и возвращает сумму элементов
переданного списка. Не забывайте, что реализовать это нужно при помощи рекурсии.

Ваша задача только написать определение функции list_sum_recursive

Sample Input:

1 2 3
Sample Output:

6
"""


def list_sum_recursive(lst: list[int]) -> int:
    """Возвращает сумму элементов переданного списка."""
    # if not lst:
    #     return 0
    # return lst[0] + list_sum_recursive(lst[1:])
    return lst.pop() + list_sum_recursive(lst) if lst else 0


assert list_sum_recursive([1, 2, 3]) == 6
assert list_sum_recursive([4, 5, 6]) == 15
assert list_sum_recursive([10, 20, 30]) == 60
assert list_sum_recursive([0, 0, 0, 0, 0]) == 0
assert list_sum_recursive([-1, -2, -3]) == -6
assert list_sum_recursive([]) == 0  # пустой список
assert list_sum_recursive([42]) == 42  # один элемент в списке
assert list_sum_recursive([0]) == 0   # один элемент в списке
assert list_sum_recursive([-5, 10, 3, -2, 7]) == 13
assert list_sum_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
print('Все проверки пройдены!')
