"""
Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.

Функция должна создать файл с названием "range_<number>.txt" и наполнить его целыми числами от 1 до n включительно,
причем каждое число записывается в отдельной строке

Пример: функция create_file_with_numbers(5) должна создать файл range_5.txt с содержимым

1
2
3
4
5
"""


def create_file_with_numbers(n: int) -> None:
    """Принимает на вход одно целое положительное число - n."""

    with open(rf'range_{n}.txt', 'w+', encoding='utf-8') as file:
        for i in range(1, n + 1):
            file.write(str(i) + '\n')
