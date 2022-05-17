import random as r

# 1. Написать функцию num_translate(), переводящую числительные
# от 0 до 10 c английского на русский язык.
# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися
# с заглавной буквы — результат тоже должен быть с заглавной.


def num_translate(eng):
    trans = {'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',
             'ten': 'десять'}
    if eng in trans:
        print(trans[eng])
    elif eng.lower() in trans:
        print(trans[eng.lower()].capitalize())


num_translate('one')
num_translate('One')

# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел

# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена
# сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


def thesaurus(*names):
    names_dict = {}
    for i in names:
        names_dict.setdefault(i[0], []).append(i)
    return names_dict


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))

# Как поступить, если потребуется сортировка по ключам?

print(dict(sorted(tuple(thesaurus('Иван', 'Мария', 'Петр', 'Илья').items()))))

# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в
# качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия
# начинается с соответствующей буквы.


def thesaurus_adv(*names):
    last = []
    for i in names:
        first_last = i[i.find(' ') + 1]
        if first_last not in last:
            last.append(first_last)
    for i in range(len(last)):
        last_dict = {}
        for j in names:
            first_last = j[j.find(' ') + 1]
            if first_last == last[i][0]:
                last_dict.setdefault(j[0], []).append(j)
        last[i] = (last[i], last_dict)
    return dict(last)

# def thesaurus_adv(*names_surnames):
# out_dict = {}
# for name_surname in names_surnames:
#     name, surname = name_surname.split()
#     out_dict.setdefault(surname[0], {})
#     out_dict[surname[0]].setdefault(name[0], [])
#     out_dict[surname[0]][name[0]].append(name_surname)

print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев',
                    'Илья Иванов', 'Анна Савельева'))

# Как поступить, если потребуется сортировка по ключам?

print(dict(sorted(tuple(thesaurus_adv('Иван Сергеев', 'Инна Серова',
                                      'Петр Алексеев', 'Илья Иванов',
                                      'Анна Савельева').items()))))

# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных
# из трех случайных слов, взятых из трёх списков (по одному из каждого).
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или
# запрещающий повторы слов в шутках (когда каждое слово можно использовать
# только в одной шутке)? Сможете ли вы сделать аргументы именованными?


def get_jokes(n, repeat=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    if repeat:
        for i in range(n):
            jokes.append(f'{r.choice(nouns)} {r.choice(adverbs)} '
                         f'{r.choice(adjectives)}')
    else:
        nouns_new = r.sample(nouns, n)
        adverbs_new = r.sample(adverbs, n)
        adjectives_new = r.sample(adjectives, n)
        for i in range(n):
            jokes.append(f'{nouns_new[i]} {adverbs_new[i]} '
                         f'{adjectives_new[i]}')
    return jokes


print(get_jokes(n=3))
print(get_jokes(n=3, repeat=False))
