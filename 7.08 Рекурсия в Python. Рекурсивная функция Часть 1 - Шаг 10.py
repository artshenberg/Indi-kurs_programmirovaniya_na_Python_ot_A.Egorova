"""
Числа Трибоначчи
Описать рекурсивную функцию tribonacci, которая принимает на вход целое число n - порядковый номер чисел Трибоначчи.
Функция по параметру n должна вычислить и вернуть значение, стоящее на n-м месте в ряде чисел Трибоначчи:
        / 0                     if n == 0 or n == 1
f(n) = <  1                     if n == 2
        \ fib(n-1) + fib(n-2)   if n > 0

Ваша задача только написать определение функции tribonacci

Sample Input 1:

1
Sample Output 1:

0
Sample Input 2:

3
Sample Output 2:

1
Sample Input 3:

5
Sample Output 3:

4
Sample Input 4:

8
Sample Output 4:

24
"""


# def tribonacci(n: int) -> int:
#     """Находит N-е число Трибоначчи."""
#     if n == 0 or n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


def tribonacci(n: int, memo=None):
    """Находит N-е число Трибоначчи с использованием мемоизации."""
    if memo is None:
        memo = {}

    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    if n in memo:
        return memo[n]

    result = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
    memo[n] = result
    return result


assert tribonacci(0) == 0
assert tribonacci(2) == 1
assert tribonacci(4) == 2
assert tribonacci(6) == 7
assert tribonacci(7) == 13
print('Все проверки пройдены!')
