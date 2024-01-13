"""
Функция Аккермана
Описать рекурсивную функцию ackermann, которая принимает на вход два целых числа  m и n находит значение,
определенное следующим образом:
            / n + 1                   if m == 0
A(m, n) =  <  A(m - 1, 1)             if m > 0, n == 0
            \ A(m - 1, A(m, n - 1))   if m > 0, n > 0

Ваша задача только написать определение функции ackermann

В тестовых примерах сперва поступает на вход значение аргумента m, затем аргумента n.

Sample Input 1:

1
5
Sample Output 1:

7
Sample Input 2:

2
4
Sample Output 2:

11
Sample Input 3:

3
3
Sample Output 3:

61
Sample Input 4:

3
2
Sample Output 4:

29
"""


# def ackermann(m: int, n: int) -> int:
#     """Находит значение функции Аккермана"""
#     if m == 0:
#         return n + 1
#     if m > 0 and n == 0:
#         return ackermann(m - 1, 1)
#     return ackermann(m - 1, ackermann(m, n - 1))


def ackermann(m: int, n: int, memo=None):
    """Находит значение функции Аккермана с использованием мемоизации"""
    if memo is None:
        memo = {}

    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0:
        result = n + 1
    elif m > 0 and n == 0:
        result = ackermann(m - 1, 1)
    else:
        result = ackermann(m - 1, ackermann(m, n - 1))

    memo[(m, n)] = result
    return result


assert ackermann(3, 2) == 29
assert ackermann(3, 0) == 5
assert ackermann(1, 0) == 2
assert ackermann(3, 5) == 253
print('Все проверки пройдены!')
