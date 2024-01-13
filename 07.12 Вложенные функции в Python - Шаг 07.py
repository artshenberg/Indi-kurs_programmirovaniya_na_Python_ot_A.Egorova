"""
Пользуясь вложенными функциями, реализуйте простой калькулятор.
Необходимо реализовать функцию calculate, которая принимает три параметра:

обязательный числовой параметр x
обязательный числовой параметр y
необязательный строковый параметр operation, по умолчанию принимает значение английской буквы a

В данной функции должны быть реализованы следующие функции:
addition - печатаем сложение двух чисел,
subtraction - печатаем вычитание из первого переданного параметра второго;
division - печатаем деление первого на второго,
multiplication - печатаем умножение двух чисел.
Каждая из этих четырёх вложенных функций должна распечатать результат математической операции и ничего не возвращать

А при помощи параметра operation и условного оператора нужно выбрать какая из функций должна быть вызвана:

если operation = a, вызываем функцию addition;
если operation = s, вызываем функции subtraction;
если operation = d, вызываем функции division;
если operation = m, вызываем функции multiplication;
calculate(2, 5) # Печатает 7.0
calculate(2.2, 15, 'a') # Печатает 17.2
calculate(22, 15, 's') # Печатает 7.0
calculate(2, 3.2, 'm') # Печатает 6.4
calculate(10, 0.4, 'd') # Печатает 25.0

Если operation принимает значение, отличное от перечисленных выше букв, то необходимо вывести на экран сообщение Ошибка.
Данной операции не существует.

Также если мы выполняем деление, то второе число (y) не должен равняться нулю, в противном случае необходимо вывести
на экран: На ноль делить нельзя!

Вам необходимо написать только определение функции calculate

Sample Input 1:

10
4
s
Sample Output 1:

6.0
Sample Input 2:

10
0
d
Sample Output 2:

На ноль делить нельзя!
Sample Input 3:

10
4
w
Sample Output 3:

Ошибка. Данной операции не существует
Sample Input 4:

1
2
a
Sample Output 4:

3.0
Sample Input 5:

3
1
d
Sample Output 5:

3.0
"""


def calculate(x: float, y: float, operation: str = 'a') -> None:

    def addition(x: float, y: float) -> None:
        print(float(x + y))

    def subtraction(x: float, y: float) -> None:
        print(float(x - y))

    def division(x: float, y: float) -> None:
        if not y:
            print('На ноль делить нельзя!')
            return
        print(x / y)

    def multiplication(x: float, y: float) -> None:
        print(float(x * y))

    match operation:
        case 'a':
            addition(x, y)
        case 's':
            subtraction(x, y)
        case 'd':
            division(x, y)
        case 'm':
            multiplication(x, y)
        case _:
            print('Ошибка. Данной операции не существует')


calculate(2, 5) # Печатает 7.0
calculate(2.2, 15, 'a') # Печатает 17.2
calculate(22, 15, 's') # Печатает 7.0
calculate(2, 3.2, 'm') # Печатает 6.4
calculate(10, 0.4, 'd') # Печатает 25.0
calculate(10, 0, 'd') # Печатает На ноль делить нельзя!
calculate(10, 10, 'u') # Печатает Ошибка. Данной операции не существует
