"""
В переменную starts_with присвойте lambda функцию, которая принимает строку и возвращает True, когда переданная строка
начинается с буквы W. Во всех остальных случаях нужно возвращать False

Ничего кроме создания переменной starts_with делать не нужно

Sample Input 1:

World
Sample Output 1:

True
Sample Input 2:

when
Sample Output 2:

False
Sample Input 3:

Сурикаты
Sample Output 3:

False
"""


starts_with = lambda s: s.startswith('W')


assert starts_with("Hello") == False  # Начинается с 'H', ожидается False
assert starts_with("World") == True   # Начинается с 'W', ожидается True
assert starts_with("WOW") == True     # Начинается с 'W', ожидается True
assert starts_with("Water") == True   # Начинается с 'W', ожидается True
assert starts_with("Python") == False # Начинается с 'P', ожидается False
assert starts_with("W") == True       # Начинается с 'W', ожидается True
assert starts_with("") == False       # Пустая строка, ожидается False
assert starts_with("wonderful") == False  # Начинается с маленькой 'w', ожидается False
assert starts_with("wOW") == False         # Начинается с маленькой 'w', ожидается False
assert starts_with("Wall") == True   # Начинается с 'W', ожидается True
print('Все проверки пройдены!')
