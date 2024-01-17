"""
Копия range

Ваша задача создать функцию-генератор my_range_gen, которая копирует работу range.

my_range_gen можно запускать, передав ей один параметр stop
my_range_gen(stop)
и она должна генерировать последовательность от 0 до stop не включительно
for i in my_range_gen(5):
    print(i)

# Будет напечатано
# 0
# 1
# 2
# 3
# 4

 my_range_gen можно запускать, передав ей два параметра start и stop

my_range_gen(start, stop)
и она должна генерировать последовательность от start включительно до stop не включительно

for i in my_range_gen(4, 8):
    print(i)

# Будет напечатано
# 4
# 5
# 6
# 7
 my_range_gen можно запускать, передав ей три параметра start, stop и step

my_range_gen(start, stop, step)
и она должна генерировать последовательность от start включительно до stop не включительно c шагом step

for i in my_range_gen(4, 8, 2):
    print(i)

# Будет напечатано
# 4
# 6

for i in my_range_gen(8, 5, -1):
    print(i)

# Будет напечатано
# 8
# 7
# 6

Предусмотрите вариант запуска my_range_gen со значением step=0. При таком варианте вызова, функция не должна
генерировать ни одной последовательности и закончить свою работу. Такое же поведение должно быть если переданы
нелогичные значения start, stop и step(см. примеры)

for i in my_range_gen(4, 8, 0):
    print(i)
# Ничего не печатает

for i in my_range_gen(20, 10, 3):
    print(i)
# Ничего не печатает, потому что нельзя пройти от 20 до 10 с шагом 3


for i in my_range_gen(1, 10, -2):
    print(i)
# Ничего не печатает, потому что нельзя пройти от 1 до 10 с шагом -2

Ваша задача написать только определение функции my_range_gen

И да, функцией range пользоваться нельзя, можете конечно попробовать, но у вас ничего не получится
"""
from typing import Generator


def my_range_gen(*args) -> Generator[int, int, None]:
    """Копирует работу range()"""

    # match len(args):
    #     case 1:
    #         """
    #         При передаче одного параметра stop my_range_gen(stop),
    #         должна генерироваться последовательность от 0 до stop не включительно
    #         """
    #         start = 0
    #         stop = args[0]
    #
    #         if stop < 0:
    #             """
    #             Ничего не печатает, потому что нельзя пройти от 0 до -5
    #             """
    #             return
    #
    #         while stop > start:
    #             yield start
    #             start += 1
    #
    #     case 2:
    #         """
    #         При передаче одного параметра stop my_range_gen(start, stop),
    #         должна генерироваться последовательность от start включительно до stop не включительно
    #         """
    #         start = args[0]
    #         stop = args[1]
    #
    #         if start > stop:
    #             """
    #             Ничего не печатает, потому что нельзя пройти от 10 до 5 с шагом 1 (шаг по умолчанию)
    #             """
    #             return
    #
    #         while stop > start:
    #             yield start
    #             start += 1
    #
    #     case 3:
    #         """
    #         При передаче одного параметра stop my_range_gen(start, stop и step),
    #         должна генерироваться последовательность от start включительно до stop не включительно c шагом step
    #         """
    #         start = args[0]
    #         stop = args[1]
    #         step = args[2]
    #
    #         if step == 0:
    #             """
    #             При значении step=0, функция не должна генерировать ни одной последовательности и закончить свою работу
    #             """
    #             return
    #
    #         if start < stop:
    #
    #             if step < 0:
    #                 """
    #                 Ничего не печатает, потому что нельзя пройти от 1 до 10 с шагом -2
    #                 """
    #                 return
    #
    #             while stop > start:
    #                 yield start
    #                 start += step
    #
    #         elif start > stop:
    #
    #             if step > 0:
    #                 """
    #                 Ничего не печатает, потому что нельзя пройти от 20 до 10 с шагом 3
    #                 """
    #                 return
    #
    #             while stop < start:
    #                 yield start
    #                 start += step
    #
    #     case _:
    #         raise TypeError("Ожидается от 1 до 3 аргументов. Передано неверное количество аргументов")

    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise TypeError("Ожидается от 1 до 3 аргументов. Передано неверное количество аргументов")

    if step == 0:
        return  # raise ValueError("Шаг не может быть равен 0")

    if (start < stop and step < 0) or (start > stop and step > 0):
        return  # raise ValueError(f"Нельзя пройти от {start} до {stop} с шагом {step}")

    while (start < stop, start > stop)[step < 0]:
        yield start
        start += step


for i in my_range_gen(5):
    print(i, end=' ')

print()
for i in my_range_gen(4, 8):
    print(i, end=' ')

print()
for i in my_range_gen(4, 8, 2):
    print(i, end=' ')

print()
for i in my_range_gen(8, 5, -1):
    print(i, end=' ')

print()
for i in my_range_gen(4, 8, 0):
    print(i, end=' ')

print()
for i in my_range_gen(20, 10, 3):
    print(i, end=' ')

print()
for i in my_range_gen(1, 10, -2):
    print(i, end=' ')

print()
for i in my_range_gen(100, 300, 13):
    print(i, end=' ')

print()
for i in my_range_gen(10, 30, 3):
    print(i, end=' ')

print()
for i in my_range_gen(1, 5, 1, 5):
    print(i, end=' ')
