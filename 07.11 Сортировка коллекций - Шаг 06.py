"""
Напишите программу, которая отсортирует список subject_marks по убыванию оценок. Предметы, имеющие одинаковые оценки,
должны быть отсортированы в алфавитном порядке

Затем распечатайте предметы и оценки, каждую пару на новой строке через пробел

Sample Input:

Sample Output:

Physics 93
Programming 91
Science 90
Chemistry 88
English 88
Maths 88
Art 78
French 78
History 78
"""


subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]

subject_marks = sorted(subject_marks, key=lambda x: (-int(x[1]), x[0]))
for item in subject_marks:
    print(*item)
