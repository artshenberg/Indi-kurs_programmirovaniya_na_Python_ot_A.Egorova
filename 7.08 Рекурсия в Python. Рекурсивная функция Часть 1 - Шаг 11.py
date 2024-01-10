"""
Число сочетаний
Описать рекурсивную функцию get_combin, которая принимает на вход два целых числа  и находит C(N,K) — число сочетаний
из N элементов по K — с помощью рекуррентного соотношения:
            / 1                         if k == 0
C(n, k) =  <  1                         if k == n
            \ C(n-1, k) + C(n-1, k-1)   if 0 < k < n

При этом гарантируется, что входные значения n и k будут удовлетворять следующим условиям:

n > 0
0 ≤ k ≤ n

Ваша задача только написать определение функции get_combin

Sample Input 1:

6
3
Sample Output 1:

20
Sample Input 2:

10
7
Sample Output 2:

120
Sample Input 3:

5
2
Sample Output 3:

10
Sample Input 4:

7
3
Sample Output 4:

35
"""


# def get_combin(n: int, k: int) -> int:
#     """Находит C(N, K) — число сочетаний из N элементов по K"""
#     if k == 0 or k == n:
#         return 1
#     return get_combin(n - 1, k) + get_combin(n - 1, k - 1)


def get_combin(n: int, k: int, memo=None):
    """Находит C(N, K) — число сочетаний из N элементов по K с использованием мемоизации"""
    if memo is None:
        memo = {}

    if k == 0 or k == n:
        return 1

    if (n, k) in memo:
        return memo[(n, k)]

    result = get_combin(n - 1, k, memo) + get_combin(n - 1, k - 1, memo)
    memo[(n, k)] = result
    return result


assert get_combin(5, 5) == 1
assert get_combin(5, 2) == 10
assert get_combin(3, 1) == 3
assert get_combin(7, 0) == 1
print('Все проверки пройдены!')
