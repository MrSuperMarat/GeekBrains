# 6. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и
# для вывода на экран записанных данных. Для чтения данных реализовать в
# командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера,
# равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного
# первому числу, по номер, равный второму числу, включительно.

import sys


def read_file(argv):
    program, *args = argv
    with open('bakery.csv', 'r', encoding='UTF-8') as amount:
        if len(args) < 1:
            for i in amount:
                print(i)
        elif len(args) == 1:
            for i in range(int(args[0]) - 1):
                amount.readline()
            for i in amount:
                print(i)
        else:
            for i in range(int(args[0]) - 1):
                amount.readline()
            for i in range(int(args[1]) - int(args[0]) + 1):
                print(amount.readline())


read_file(sys.argv)
