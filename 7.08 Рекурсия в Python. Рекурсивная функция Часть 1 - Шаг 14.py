"""
Превращаем вложенный список в плоский
Представьте, что у нас есть список целых чисел неограниченной вложенности. То есть наш список может состоять из списков,
внутри которых также могут быть списки. Ваша задача превратить все это в линейный список при помощи функции flatten

Ваша задача только написать определение функции flatten
"""


from typing import List, Union, Optional

NestedList = List[Optional[Union[int, "NestedList"]]]

def flatten(lst: NestedList) -> list[int]:
    """Превращает вложенный список в плоский"""

    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


assert flatten([1, [2, 3, [4]], 5]) == [1, 2, 3, 4, 5]
assert flatten([1, [2, 3], [[2], 5], 6]) == [1, 2, 3, 2, 5, 6]
assert flatten([[[[9]]], [1, 2], [[8]]]) == [9, 1, 2, 8]
assert flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]
assert flatten([1, [2, 3], [4, 5], 6]) == [1, 2, 3, 4, 5, 6]
assert flatten([1, 2, [3, 4, [5, 6]], [7, [8], 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert flatten([1, [2, [3, [4, [5, [6]]]]]]) == [1, 2, 3, 4, 5, 6]
assert flatten([1, [2, 3], [[4], [5, 6]], [7], [8, [9]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert flatten([1, [2, [3, [4, [5, [6, [7]]]]]]]) == [1, 2, 3, 4, 5, 6, 7]
assert flatten([]) == []  # пустой список
assert flatten([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # одномерный список
assert flatten([[1], [2], [3], [4], [5]]) == [1, 2, 3, 4, 5]  # список списков
print('Все проверки пройдены!')
