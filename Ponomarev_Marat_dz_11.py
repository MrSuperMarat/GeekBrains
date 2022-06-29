# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках
# класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен
# проводить валидацию числа, месяца и года (например, месяц — от 1 до
# 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract(cls, date):
        return tuple(map(int, date.split('-')))

    @staticmethod
    def is_date_valid(date):
        day, month, year = map(int, date.split('-'))
        return day < 32 and 0 < month < 13 and year < 2100


print(*Date.extract('24-12-2018'))
print(Date.is_date_valid('25-04-2021'))
print(Date.is_date_valid('3-13-2000'))


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на ноль. Проверьте его работу на данных, вводимых
# пользователем. При вводе нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a, b = int(input()), int(input())
    if b == 0:
        raise OwnError('Деление на ноль')
    res = a / b
except OwnError as err:
    print(err)
else:
    print(res)

# try:
#     a, b = int(input()), int(input())
#     res = a / b
# except:
#     print('Деление на ноль')
# else:
#     print(res)

# 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу
# исключения на реальном примере. Запрашивать у пользователя данные и
# заполнять список необходимо только числами. Класс-исключение должен
# контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются
# бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду «stop». При этом скрипт завершается,
# сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить
# только числа и строки. Во время ввода пользователем очередного
# элемента необходимо реализовать проверку типа элемента. Вносить его
# в список, только если введено число. Класс-исключение должен не
# позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна
# завершаться.


class ListError(Exception):
    def __init__(self, txt):
        self.txt = txt


numbers = []
x = input()
while x != 'stop':
    try:
        if type(int(x)) == int:
            numbers.append(x)
        x = input()
    except ValueError:
        print('Введите число')
        x = input()
print(numbers)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определите параметры,
# общие для приведённых типов. В классах-наследниках реализуйте
# параметры, уникальные для каждого типа оргтехники.


class OffEquip:
    def __init__(self, length, width, height, company):
        self.length = length
        self.width = width
        self.height = height
        self.company = company


class Printer(OffEquip):
    def __init__(self, length, width, height, company, is_color, count):
        super().__init__(length, width, height, company)
        self.is_color = is_color
        self.count = count


class Scanner(OffEquip):
    def __init__(self, length, width, height, company, quality):
        super().__init__(length, width, height, company)
        self.quality = quality


class Xerox(OffEquip):
    def __init__(self, length, width, height, company, is_color, count):
        super().__init__(length, width, height, company)
        self.is_color = is_color
        self.count = count


# 5. Продолжить работу над предыдущим заданием. Разработайте методы,
# которые отвечают за приём оргтехники на склад и передачу в
# определённое подразделение компании. Для хранения данных о
# наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над предыдущим заданием. Реализуйте механизм
# валидации вводимых пользователем данных. Например, для указания
# количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.


class Stock:
    def __init__(self, name, address, products={}):
        self.name = name
        self.width = address
        self.products = products

    def reception(self):
        product = input('Введите название товара: ')
        flag = True
        while flag is True:
            try:
                price = int(input('Введите цену за единицу товара: '))
                if price > 0:
                    flag = False
                else:
                    print('Пожалуйста, введите положительное число')
            except ValueError:
                print('Пожалуйста, введите число')
        while flag is False:
            try:
                count = int(input('Введите количество товаров данного типа: '))
                if count > 0:
                    flag = True
                else:
                    print('Пожалуйста, введите положительное число')
            except ValueError:
                print('Пожалуйста, введите число')
        self.products[product] =\
            self.products.setdefault(product, {'price': 0, 'count': 0})
        self.products[product]['price'] = price
        self.products[product]['count'] =\
            self.products[product]['count'] + count
        return (f'Товар {product} в количестве {count} ценой {price} рублей '
                f'прибыл на склад')

    def transfer(self, subdivision):
        product = input('Введите название товара: ')
        flag = True
        while flag is True:
            try:
                count = int(input('Введите количество товаров данного типа: '))
                if count > 0:
                    flag = False
                else:
                    print('Пожалуйста, введите положительное число')
            except ValueError:
                print('Пожалуйста, введите число')
        self.products[product]['count'] =\
            self.products[product]['count'] - count
        return (f'Товар {product} в количестве {count} отправлен в '
                f'подразделение {subdivision}')


stock = Stock('Ikea', 'Moscow')
print(stock.reception())
print(stock.products)
print(stock.transfer(2))
print(stock.products)

# 7. Реализовать проект «Операции с комплексными числами». Создайте
# класс «Комплексное число». Реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта. Для этого
# создаёте экземпляры класса (комплексные числа), выполните сложение и
# умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class Complex:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


first = Complex(5 + 5j)
second = Complex(1 - 6j)
print(f'Первое число: {first.num}, второе число: {second.num}')
print(f'Сумма: {first + second}')
print(f'Произведение: {first * second}')
