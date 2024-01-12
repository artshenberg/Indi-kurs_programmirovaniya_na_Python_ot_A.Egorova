"""
Имеется функция sale, которая возвращает цену товара со скидкой 10%.

def sale(x):
    return x*0.9

Однако мы изучаем анонимные функции, поэтому на основе данной функции создайте анонимную функцию и присвойте её
переменной sale_lambda
"""

sale_lambda = lambda x: x * 0.9


assert sale_lambda(100) == 90.0   # 10% скидка на 100 равна 90
assert sale_lambda(50) == 45.0     # 10% скидка на 50 равна 45
assert sale_lambda(200) == 180.0   # 10% скидка на 200 равна 180
assert sale_lambda(75) == 67.5     # 10% скидка на 75 равна 67.5
assert sale_lambda(120.5) == 108.45 # 10% скидка на 120.5 равна 108.45
print('Все проверки пройдены!')
