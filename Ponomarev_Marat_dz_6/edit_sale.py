# 7. * (вместо 6) Добавить возможность редактирования данных при помощи
# отдельного скрипта: передаём ему номер записи и новое значение. При этом
# файл не должен читаться целиком — обязательное требование. Предусмотреть
# ситуацию, когда пользователь вводит номер записи, которой не существует.

import sys


def edit_file(argv):
    program, *args = argv
    with open('bakery.csv', 'r+', encoding='UTF-8') as amount:
        sales = []
        for i in amount:
            sales.append(i)
        sales[int(args[0]) - 1] = f'{args[1]}\n'
        amount.seek(0)
        amount.writelines(sales)


edit_file(sys.argv)
