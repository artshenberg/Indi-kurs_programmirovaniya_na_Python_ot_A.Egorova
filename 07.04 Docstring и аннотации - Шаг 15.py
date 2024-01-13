"""
Напишите функцию shift_letter , которая принимает два аргумента:

letter одна английская буква в нижнем регистре
shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift .Сдвиг может быть цикличным в
пределах от a до z. Ниже примеры:

shift_letter('b', 2)=> 'd'
shift_letter('d', 1) => 'e'
shift_letter('z', 1) => 'a'
shift_letter('d', -2) => 'b'
shift_letter('d', 26) => 'd'
shift_letter('b', -3) => 'y'

Не забудьте проаннотировать аргументы и также добавьте doc-строку «Функция сдвигает символ letter на shift позиций»

Функция shift_letter  должна вернуть новый символ. Вам нужны только символы в нижнем регистре

Нужно написать только определение функции shift_letter

🚀Подсказка🚀
Sample Input 1:

z 5
Sample Output 1:

e
Sample Input 2:

w 28
Sample Output 2:

y
Sample Input 3:

w -26
Sample Output 3:

w
Sample Input 4:

w -27
Sample Output 4:

v
Sample Input 5:

a 53
Sample Output 5:

b
"""

# import string
#
#
# def shift_letter(letter: str, shift: int) -> str:
#     """Функция сдвигает символ letter на shift позиций"""
#     if letter.isalpha():
#         alphabet = string.ascii_lowercase if letter.islower() else string.ascii_uppercase
#         shifted_index = (alphabet.index(letter) + shift) % len(alphabet)
#         shifted_letter = alphabet[shifted_index]
#         return shifted_letter
#     else:
#         return letter


def shift_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))


assert shift_letter('d', 1) == 'e'
assert shift_letter('d', 26) == 'd'
assert shift_letter('z', 5) == 'e'

print('Все проверки пройдены!')
