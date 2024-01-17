"""
Генератор квадратов
Ваша задача создать функцию-генератор gen_squares, которая принимает аргумент n и генерирует квадраты чисел от 1 до n
включительно.

Ниже несколько вариантов использования:

for i in gen_squares(5):
    print(i)

# Будет напечатано
# 1
# 4
# 9
# 16
# 25

for i in gen_squares(3):
    print(i)

# Будет напечатано
# 1
# 4
# 9

Ваша задача написать только определение функции gen_squares
"""
from typing import Generator


def gen_squares(n: int) -> Generator[int, int, None]:
    """Принимает аргумент n и генерирует квадраты чисел от 1 до n включительно."""
    for i in range(1, n + 1):
        yield i * i


for i in gen_squares(3):
    print(i)
