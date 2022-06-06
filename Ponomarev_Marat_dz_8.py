# 1. Написать функцию email_parse(<email_address>), которая при помощи
# регулярного выражения извлекает имя пользователя и почтовый домен из email
# адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.

import re

RE_EMAIL = re.compile(r'^[a-zA-Z0-9_\.-][a-zA-Z0-9_-]+[a-zA-Z0-9_\.-]'
                      r'@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+$')

# RE_GET_PARSER = re.compile(r'(?P<username>[^@]+)@(?P<domain>[^@]+)')
#
# print(*map(lambda x: x.groupdict(), RE_GET_PARSER.finditer(email)))


def email_parse(email):
    if RE_EMAIL.match(email) is None:
        return ValueError
    else:
        return dict(zip(('username', 'domain'), re.split('@', email)))


print(email_parse('apagey2009@yandex.ru'))

# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов
# web-сервера из ДЗ 6 урока nginx_logs.txt.

RE_PARSED_RAW = re.compile(r'((?:\d+\.){3}\d+) - - '
                           r'\[(\d{2}/[A-Z][a-z]+/\d{4}(?::\d{2}){3}'
                           r'\+\d{4})\] "([A-Z]+) '
                           r'(/[a-z]+/[a-z1-9_]+) [A-Z]{4}/\d{1}\.\d{1}" '
                           r'(\d{3}) '
                           r'(\d+)')

parsed_raws = []
with open(r'Ponomarev_Marat_dz_6\nginx_logs.txt', 'r') as file:
    for i in file:
        parsed_raws.append(RE_PARSED_RAW.findall(i))

[print(*i) for i in parsed_raws[0:100]]

# 3. Написать декоратор для логирования типов позиционных аргументов функции.


def type_logger(func):

    def type_function(*args):
        for i in args:
            print(f'{i}: {type(i)}', end=', ')

    return type_function


@type_logger
def function(*args):
    pass


function('ab', 5, [4, 5])
print()

# 4. Написать декоратор с аргументом-функцией (callback), позволяющий
# валидировать входные значения функции и выбрасывать исключение ValueError,
# если что-то не так.


def val_checker(func):

    def callback(args):
        if args > 0:
            return func(args)
        else:
            return ValueError

    return callback


@val_checker
def calc_cube(x):
    return x ** 3


print(calc_cube(-5))
