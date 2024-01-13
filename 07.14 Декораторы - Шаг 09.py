"""
Напишите декоратор repeater, который дважды вызывает декорированную функцию

@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 7) # после этого на отдельных строка дважды распечатается значение 14
multiply(5, 3) # после этого на отдельных строка дважды распечатается значение 15

Ваша задача написать только определение функции декоратора repeater
"""


def repeater(func):
    """Дважды вызывает декорированную функцию"""

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 7) # после этого на отдельных строках дважды распечатается значение 14
multiply(5, 3) # после этого на отдельных строках дважды распечатается значение 15
