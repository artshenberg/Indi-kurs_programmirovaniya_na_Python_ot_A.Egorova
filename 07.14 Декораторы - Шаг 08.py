"""
Напишите декоратор text_decor, который оборачивает вызов декорированной функции фразами «Hello» и «Goodbye!»:
фраза «Hello» печатается до вызова, фраза «Goodbye!» - после

@text_decor
def simple_func():
    print('I just simple python func')

simple_func()

# Вывод
Hello
I just simple python func
Goodbye!

@text_decor
def multiply(num1, num2):
    print(num1 * num2)

multiply(3, 5)

# Вывод
Hello
15
Goodbye!

Ваша задача написать только определение функции декоратора text_decor
"""


def text_decor(func):
    """Оборачивает вызов декорированной функции фразами «Hello» и «Goodbye!»"""

    def wrapper(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')

    return wrapper


@text_decor
def simple_func():
    print('I just simple python func')


@text_decor
def multiply(num1, num2):
    print(num1 * num2)


simple_func()
print()
multiply(3, 5)
