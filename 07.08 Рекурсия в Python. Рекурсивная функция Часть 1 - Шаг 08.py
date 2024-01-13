"""
Двойной факториал
Описать рекурсивную функцию double_fact, которая принимает на вход целое число и вычисляет значение двойного факториала
по формуле:
        / 1                                     if n == 1
f(n) = <  2                                     if n == 2
        \ n * (n - 2) * (n - 4) * (n - 6) *...  if n > 2

Ваша задача только написать определение функции double_fact
"""


def double_fact(n: int) -> int:
    """Вычисляет значение двойного факториала"""
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return n * double_fact(n - 2)


assert double_fact(7) == 105
assert double_fact(5) == 15
assert double_fact(4) == 8
assert double_fact(1) == 1
assert double_fact(10) == 3840
print('Все проверки пройдены!')
