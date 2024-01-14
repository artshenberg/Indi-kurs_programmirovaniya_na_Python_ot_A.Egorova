"""
Анализ продаж
К вам в руки попал файл 'manager_sales.json', в котором содержится информация одного автосалона о продажах менеджеров.
В файле указано для каждого менеджера список проданных им автомобилей, а также проставлена цена продажи каждого
автомобиля.

Ваша задача найти самого успешного менеджера по итоговой сумме продаж. В качестве ответа нужно через пробел указать
сперва его имя, затем фамилию и после общую сумму его продаж.
"""
import json


def analyze_it(file_name: str) -> tuple | str:
    """
    Находит самого успешного менеджера по итоговой сумме продаж.
    Выводит его имя, затем фамилию и после общую сумму его продаж.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

    except FileNotFoundError:
        return f'Файл "{file_name}" не найден'

    if not content:
        return f'Файл "{file_name}" пуст'

    json_data = json.loads(content)

    summary = {}
    for item in json_data:
        summary[(item['manager']['first_name'], item['manager']['last_name'])] = (
            summary.get((item['manager']['first_name'], item['manager']['last_name']), 0) +
            sum(car['price'] for car in item['cars'])
        )

    result = sorted(summary.items(), key=lambda x: (x[1], x[0][1], x[0][0])).pop()

    return f'{result[0][0]} {result[0][1]} {result[1]}'


print(analyze_it('manager_sales.json'))
