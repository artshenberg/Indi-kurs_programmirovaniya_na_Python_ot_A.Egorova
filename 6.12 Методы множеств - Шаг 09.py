"""
Даны два списка чисел.

Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.

Sample Input:

1 3 2 5
4 3 2 6
Sample Output:

2 3
"""

print(*sorted(set(map(int, input().split())).intersection(map(int, input().split()))))
