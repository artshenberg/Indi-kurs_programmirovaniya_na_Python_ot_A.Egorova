"""
Напишите функцию summa_n, которая принимает одно целое положительное t число и находит сумму всех чисел от 1 до t
включительно. Программа должна распечатать сообщение

"Я знаю, что сумма чисел от 1 до {t} равна {S}", где в качестве t и S вам необходимо подставить значения (см. тестовые
данные)

Ваша задача написать только определение функции summa_n, вызывать ее не нужно

Sample Input 1:

5
Sample Output 1:

Я знаю, что сумма чисел от 1 до 5 равна 15
Sample Input 2:

3
Sample Output 2:

Я знаю, что сумма чисел от 1 до 3 равна 6
"""


def summa_n(t):
    print(f"Я знаю, что сумма чисел от 1 до {t} равна {sum(range(1, t + 1))}")
