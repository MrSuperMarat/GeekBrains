# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код
# валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по
# отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация:
# выполнить предварительно запрос к API в обычном браузере, посмотреть
# содержимое ответа. Можно ли, используя только методы класса str, решить
# поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами
# использовать вместо float тип Decimal? Сильно ли усложняется код функции
# при этом? Если в качестве аргумента передали код валюты, которого нет в
# ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы
# доллара и евро.

# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна
# возвращать кроме курса дату, которая передаётся в ответе сервера. Дата
# должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

import requests
import datetime as dt

# print(requests.__version__)

path = 'http://www.cbr.ru/scripts/XML_daily.asp'
result = requests.get(path)

# print(dt.datetime.strptime(a, '%d %B %Y %H:%M:%S').date())

dattim = result.headers['Date'][6:-13]
dat = dt.datetime.strptime(dattim, '%d %B %Y').date()
tex = result.text
rate = {}
while tex.find(',') != -1:
    rate.setdefault(tex[tex.find('</CharCode><Nominal>') - 3:
                        tex.find('</CharCode><Nominal>')],
                    tex[tex.find(',') - 2: tex.find(',') + 5])
    tex = tex[tex.find(',') + 5:]


def currency_rates(x):
    if x.upper() in rate:
        return rate[x.upper()], str(dat)


if __name__ == '__main__':
    print(*currency_rates('USD'), sep=', ')
    print(*currency_rates('eur'), sep=', ')

# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен
# работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05
