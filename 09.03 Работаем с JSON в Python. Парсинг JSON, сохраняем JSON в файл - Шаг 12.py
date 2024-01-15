"""
В этой задаче вам необходимо раскодировать текст, находящийся в текстовом файле 'Abracadabra__1_.txt'. Ключ для
декодирования располагается в файле 'Alphabet.json'. В качестве ответа нужно просто отправить получившийся текст.
И обратите внимание, что раскодировать нужно только лишь буквы, все остальные символы(цифры, знаки пунктуации и т.д.)
необходимо выводить как есть.
"""
import json


def decode_text_via_key(file_name: str, key_file: str) -> str:
    """
    Декодирует текст из файла file_name с помощью ключа из файла key_file
    :param file_name:
    :param key_file:
    :return:
    """

    try:
        with open(file_name, 'r', encoding='utf-8') as file, open(key_file, 'r', encoding='utf-8') as key:
            text = file.read()
            key_string = key.read()

    except FileNotFoundError as error:
        if file_name in error.filename:
            return f'Файл "{file_name}" не найден'
        if key_file in error.filename:
            return f'Файл "{key_file}" не найден'

    if not text:
        return f'Файл "{file_name}" пуст'
    if not key_string:
        return f'Файл "{key_file}" пуст'

    json_key = json.loads(key_string)

    translation_table = str.maketrans(json_key)
    result = text.translate(translation_table)

    return result


print(decode_text_via_key('Abracadabra__1_.txt', 'Alphabet.json'))
