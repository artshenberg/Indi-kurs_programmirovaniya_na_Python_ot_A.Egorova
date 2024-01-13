"""
Быстрая сортировка (quick sort) | Разбор

Быстрая сортировка - еще один вид сортировки, который использует рекурсию.

Ваша задача реализовать этот алгоритм. Для этого нужно будет создать функцию quick_sort, которая будет принимать
исходный список и возвращать новый отсортированный в порядке не убывания список.

Необходимо написать только определение функций quick_sort,
при этом нельзя пользоваться встроенными сортировками в Python.

Sample Input 1:

5
19 4 5 17 1
Sample Output 1:

1 4 5 17 19
Sample Input 2:

8
16 19 2 12 20 15 20 15
Sample Output 2:

2 12 15 15 16 19 20 20
"""


def quick_sort(lst: list) -> list:
    """Возвращает новый отсортированный в порядке не убывания список."""
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [i for i in lst if i < pivot]
    middle = [i for i in lst if i == pivot]
    right = [i for i in lst if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)


assert quick_sort([16, 19, 2, 12, 20, 15, 20, 15]) == [2, 12, 15, 15, 16, 19, 20, 20]
assert quick_sort([5, 8, 1, 3, 7, 9, 2]) == [1, 2, 3, 5, 7, 8, 9]
assert quick_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert quick_sort([]) == []
assert quick_sort([1]) == [1]
assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
assert quick_sort([-5, -1, -8, 0, -2]) == [-8, -5, -2, -1, 0]
assert quick_sort([8, 8, 3, 2, 3, 5, 7, 9, 1, 4, 6]) == [1, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9]
assert quick_sort([4, 2, 1, 3, 5]) == [1, 2, 3, 4, 5]
print('Все проверки пройдены!')
