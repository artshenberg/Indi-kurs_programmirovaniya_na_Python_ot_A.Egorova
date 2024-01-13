"""
Числа Фибоначчи
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где число, стоящее на n-ой
позиции можно вычислить по формуле:
        / 0                     if n == 0
f(n) = <  1                     if n == 1
        \ fib(n-1) + fib(n-2)   if n > 0

Требуется найти N-е число Фибоначчи.

Входные данные
Программе поступает на вход целое число N (0 ≤ N ≤ 30) - порядковый номер числа Фибоначчи.

Выходные данные
Вам необходимо вывести на экран N-е число Фибоначчи.

Sample Input 1:

7
Sample Output 1:

13
Sample Input 2:

10
Sample Output 2:

55
"""


def fibonacci(n: int, memo=None) -> int:
    """Находит N-е число Фибоначчи."""
    if memo is None:
        memo = {}

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]

    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result

print(fibonacci(int(input())))
