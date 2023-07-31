""" Задание 1
Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.
"""

lst = [1, 1, 3, 4, 2, 3, 8, 3, 5]
duplicates = list(set(i for i in lst if lst.count(i) > 1))
print(duplicates)


""" Задание 2
В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку.
"""

import requests

wiki_url = 'https://ru.wikipedia.org/wiki/Python'
res = requests.get(wiki_url)
text = res.text.replace(',', '').replace('.', '')

# делаем выборку из HTML страницы, отсекая слова с лишними символами
# также отсек возможные союзы и предлоги условием длины слова > 2 букв
wiki_words_list = [word.lower() for word in res.text.split() if word.isalpha() and len(word) > 2]

# строим словарь, где ключ - слово, значение - количество этого слова в тексте
words_counts = {word: wiki_words_list.count(word) for word in set(wiki_words_list)}

index = 1
for word, count in reversed(sorted(words_counts.items(), key=lambda x: x[1])):
    print(f'{index:>2}) {word:<20}: {count}')
    index += 1
    if index > 10:
        break


""" Задание 3
Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
"""

# список вещей с весом в граммах
hiking_items = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
                'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
                'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'жвачка': 10}
print(hiking_items)
print(f'Всего вещей: {len(hiking_items)}')
print(f'Общий вес: {sum(hiking_items.values())} гр')

backpack_capacity = int(input('Максимальная грузоподъёмность рюкзака (кг): ')) * 1000
take_items = {}
total_weight = 0
while True:
    for item, weight in hiking_items.items():
        if total_weight + weight <= backpack_capacity:
            hiking_items.pop(item)
            take_items.update({item: weight})
            total_weight += weight
            break
    else:
        break
print(take_items)
print(f'Всего взятых вещей: {len(take_items)}')
print(f'Общий вес: {total_weight} гр')
