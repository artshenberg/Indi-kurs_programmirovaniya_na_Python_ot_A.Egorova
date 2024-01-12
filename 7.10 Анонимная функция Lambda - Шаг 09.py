"""
Хорошо постарались с прошлой задачей! Однако мы забыли, что скидка должна быть только для тех товаров, стоимость
которых больше 50. Вам стоит внести это изменение в прошлый код

Ваша задача только переопределить переменную sale_lambda

Sample Input 1:

50.0
Sample Output 1:

50.0
Sample Input 2:

60.0
Sample Output 2:

54.0
Sample Input 3:

12.33
Sample Output 3:

12.33
"""


sale_lambda = lambda x: x * 0.9 if x > 50 else x


assert sale_lambda(60) == 54.0  # x > 50, ожидается 60 * 0.9 = 54.0
assert sale_lambda(40) == 40     # x <= 50, ожидается 40 (без скидки)
assert sale_lambda(75) == 67.5   # x > 50, ожидается 75 * 0.9 = 67.5
assert sale_lambda(30) == 30     # x <= 50, ожидается 30 (без скидки)
assert sale_lambda(100) == 90.0  # x > 50, ожидается 100 * 0.9 = 90.0
print('Все проверки пройдены!')
