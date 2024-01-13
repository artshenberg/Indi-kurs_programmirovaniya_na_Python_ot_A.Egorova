import os

path = r"c:\My Games"


def print_path_tree(path: str, level: int = 1) -> None:
    """"Обходит все папки, включая вложенные, по указанному пути и выводит их содержимое"""
    if not os.listdir(path):
        print('-' * 7 + ' Пустая папка ' + '-' * 7)
    else:
        print('--→', 'Level', level, 'Content: ')
        print('', '...' * level, '', end='')
        print(*os.listdir(path), sep='\n' + ' ' + '...' * level + ' ')
    for item in os.listdir(path):
        if os.path.isdir(rf'{path}\{item}'):
            print('↓', rf'{path}\{item}')
            print_path_tree(rf'{path}\{item}', level+1)
            print('↑')


print_path_tree(path)
