import random as r

# 1. Выяснить тип результата выражений

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# 2. Дан список:

temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
        'была', '+5', 'градусов']

# Необходимо его обработать — обособить каждое целое число
# (вещественные не трогаем) кавычками (добавить кавычку до
# и кавычку после элемента списка, являющегося числом) и
# дополнить нулём до двух целочисленных разрядов

temp_2 = []

for i in range(len(temp)):
    elem = temp[i].strip('+').strip('-')
    if elem.isdigit() and len(elem) < 2:
        if temp[i][0] == '+':
            temp[i] = '+' + '0' + temp[i][1]
        elif temp[i][0] == '+':
            temp[i] = '-' + '0' + temp[i][1]
        else:
            temp[i] = '0' + temp[i][0]
    if elem.isdigit():
        temp_2.extend(['"', temp[i], '"'])
    else:
        temp_2.append(temp[i])

# Сформировать из обработанного списка строку:

quote = 1
for i in temp_2:
    if i.strip('+').strip('-').isdigit():
        print(i, end='')
    elif i != '"':
        print(i, end=' ')
    elif i == '"' and quote % 2:
        print('"', end='')
        quote += 1
    else:
        print('" ', end='')
        quote += 1
print()

# 3. * Решить задачу 2 не создавая новый список (in place).

temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
        'была', '+5', 'градусов']

len_temp = len(temp)

for i in range(len_temp):
    elem = temp[i].strip('+').strip('-')
    if elem.isdigit() and len(elem) < 2:
        if temp[i][0] == '+':
            temp[i] = '+' + '0' + temp[i][1]
        elif temp[i][0] == '+':
            temp[i] = '-' + '0' + temp[i][1]
        else:
            temp[i] = '0' + temp[i][0]
    if elem.isdigit():
        temp.extend(['"', '"'])

count = 0
for i in range(len_temp):
    if temp[i + count].strip('+').strip('-').isdigit():
        temp[i + 3 + count: len_temp + 2 + count] =\
            temp[i + 1 + count: len_temp + count]
        temp[i + count], temp[i + 1 + count], temp[i + 2 + count] =\
            '"', temp[i + count], '"'
        count += 2

quote = 1
for i in temp:
    if i.strip('+').strip('-').isdigit():
        print(i, end='')
    elif i != '"':
        print(i, end=' ')
    elif i == '"' and quote % 2:
        print('"', end='')
        quote += 1
    else:
        print('" ', end='')
        quote += 1

print()

# Дан список, содержащий искажённые данные с должностями и именами сотрудников:

employ = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
          'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на
# экран фразы вида: 'Привет, Игорь!'. Можно ли не создавать новый список?

[print(f'Привет, {i}!') for i in
 list(j[-1].title() for j in (i.split() for i in employ))]

[print(f'Привет, {i}!') for i in
 map(lambda x: x[-1].title(), [i.split() for i in employ])]

# 5 Создать список, содержащий цены на товары (10–20 товаров)
numbers = ([str(round(r.uniform(1, 100), 2)) for i in range(5)] +
           [str(r.randint(1, 100)) for i in range(5)] + ['45.6'])

# Вывести на экран эти цены через запятую в одну строку, цена должна
# отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).

rubles, pennies = [], []
for i in numbers:
    price = i.split('.')
    if len(price) == 2:
        rub, pen = price
    else:
        rub = price[0]
        pen = '00'
    rubles.append(rub)
    pennies.append((pen, '0' + pen)[len(pen) == 1])

prices = [(f'{rub} руб {pen} коп') for rub, pen in zip(rubles, pennies)]

# Вывести цены, отсортированные по возрастанию, новый список не создавать.

print(*sorted(prices, key=lambda x: (int(x.split()[0]),
                                     int(x.split()[2]))), sep=',')

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.

prices_low = sorted(prices, key=lambda x: (int(x.split()[0]),
                                           int(x.split()[2])), reverse=1)
print(*prices_low, sep=', ')

# Вывести цены пяти самых дорогих товаров(по возрастанию),
# написав минимум кода.

print(*prices_low[4::-1], sep=', ')
