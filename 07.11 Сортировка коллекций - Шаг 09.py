"""
Представьте, у нас есть список товаров и их стоимость, но мы хотим взглянуть на него в отсортированном виде.
Вверху хотим видеть самые дорогие товары, внизу самые дешевые

Программа будет принимать строки, в которых сперва указывается название товара, а затем через двоеточие с пробелом
его цена - целое положительное число.

Строка «конец» означает завершение списка товаров и соответственно окончание ввода

Все товары имеют уникальные названия, цены не дублируются.

Ваша задача вывести список товаров по уменьшению цены

Sample Input:

Sony PlayStation 5: 46000
Телевизор QLED Samsung QE65Q60TAU: 87090
Смартфон Samsung Galaxy A11: 10000
Планшет Samsung Galaxy Tab S6: 26600
конец
Sample Output:

Телевизор QLED Samsung QE65Q60TAU
Sony PlayStation 5
Планшет Samsung Galaxy Tab S6
Смартфон Samsung Galaxy A11
"""


from io import StringIO
import sys

# Подготовка данных для проверок
input_data = """Sony PlayStation 5: 46000
Телевизор QLED Samsung QE65Q60TAU: 87090
Смартфон Samsung Galaxy A11: 10000
Планшет Samsung Galaxy Tab S6: 26600
конец
"""

# Перенаправление ввода для тестирования
sys.stdin = StringIO(input_data)

# Запуск кода
goods = []
while True:
    string = input()
    if string == 'конец':
        break

    good = tuple(item.strip() for item in string.split(':'))
    goods.append(good)

goods.sort(key=lambda x: (-int(x[1]), x[0].lower))
for good in goods:
    print(good[0])

# Проверки
assert goods[0] == ('Телевизор QLED Samsung QE65Q60TAU', '87090')
assert goods[1] == ('Sony PlayStation 5', '46000')
assert goods[2] == ('Планшет Samsung Galaxy Tab S6', '26600')
assert goods[3] == ('Смартфон Samsung Galaxy A11', '10000')
assert len(goods) == 4
print('Все проверки пройдены!')
