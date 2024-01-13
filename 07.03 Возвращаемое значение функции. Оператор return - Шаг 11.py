"""
Ваша задача написать функцию find_duplicate, которая принимает один аргумент - список чисел.
Функция должна возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке,
в котором они встречаются в исходном списке. Под дублем будем подразумевать число, которое присутствовало
в списке несколько раз.

find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) => [1, 2]
find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) => [2, 1]
find_duplicate([1, 2, 3, 4]) => []
find_duplicate([1, 2, 3, 4, 3]) => [3]
Ваша задача написать только определение функции find_duplicate

Про инструкцию assert можно прочитать здесь

Разбор Youtube Boosty Patreon

Sample Input:

Sample Output:

Все успешно
"""


# def find_duplicate(lst):
#     result = []
#     for item in lst:
#         if lst.count(item) > 1 and item not in result:
#             result.append(item)
#
#     return result


def find_duplicate(lst):
    frequency = {}
    result = []

    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1

    for item, count in frequency.items():
        if count > 1:
            result.append(item)

    return result


assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
print('Все успешно')
