"""
В файле 'group_people.json' содержится информация о нескольких группах людей, при этом у каждой группы есть свой
идентификатор.

Ваша задача найти идентификатор группы, в которой находится самое большое количество женщин, рожденных после 1977 года.

В качестве ответа необходимо указать через пробел идентификатор найденной группы и сколько в ней было женщин,
рожденных после 1977 года.
"""
import json


def find_group_id(file_name: str) -> str:
    """
    Найти в файле идентификатор группы, в которой находится самое большое количество женщин,
    рожденных после 1977 года.
    """

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

    except FileNotFoundError:
        return f'Файл "{file_name}" не найден'

    if not content:
        return f'Файл "{file_name}" пуст'

    json_data = json.loads(content)

    group_id_max = 0
    max_born = 0
    for item in json_data:
        group_id = item.get('id_group', 0)
        people = item.get('people', [])

        females_born_after_1977 = (
            sum(person.get('year', 0) > 1977 for person in people if person.get('gender', '') == 'Female'))

        if females_born_after_1977 > max_born:
            max_born = females_born_after_1977
            group_id_max = group_id

    if max_born == 0:
        return f'В файле "{file_name}" нет групп с женщинами, рожденными после 1977 года'

    return f'{group_id_max} {max_born}'


print(find_group_id('group_people.json'))
