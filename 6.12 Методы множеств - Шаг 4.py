"""
Перед вами располагается множество  my_set

Ваша задача удалить из него 3 строковых элемента:

government
national
tease
Выводить ничего не нужно, только удалить элементы выше
"""

my_set = {
    'mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
    'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
    'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
    'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
    'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention',
    'tradition', 'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal',
    'government', 'control', 'value', 'few', 'generation', 'service', 'national',
    'tradition', 'government', 'mention', 'proposal'
}

#print(len(my_set))

to_remove = ('government', 'national', 'tease')

for item in to_remove:
    my_set.remove(item)

#print(len(my_set))
