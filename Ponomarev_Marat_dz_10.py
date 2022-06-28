from abc import ABC, abstractmethod

# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
# конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(str(j) for j in i)
                         for i in self.matrix)

    def __add__(self, other):
        sum_mat = [[int(self.matrix[i][j]) + int(other.matrix[i][j])
                   for j in range(len(self.matrix[i]))]
                   for i in range(len(self.matrix))]
        return '\n'.join('\t'.join(str(j) for j in i)
                         for i in sum_mat)


a = Matrix([[5, 18, 11, 2], [6, 17, 23, 1], [41, 50, 9, 43]])
b = Matrix([[45, 8, 2, 1], [6, 7, 93, 189], [24, 5, 97, 22]])

print(a)
print()
print(b)
print()
print(a+b)

# 2. Реализовать проект расчёта суммарного расхода ткани на
# производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам
# одежды в этом проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост (для костюма). Это
# могут быть обычные числа: V и H, соответственно.


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить
# работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Реализовать абстрактные классы для основных классов проекта и
# проверить работу декоратора @property.


class Coat(Clothes):
    @property
    def consumption(self):
        return (f'Для изготовления пальто требуется '
                f'{round(self.param/6.5 + 0.5, 2)} метров ткани')


class Suit(Clothes):
    @property
    def consumption(self):
        return (f'Для изготовления костюма требуется '
                f'{round(2*self.param + 0.3, 2)} метров ткани')


coat = Coat(50)
print(coat.consumption)

suit = Suit(5)
print(suit.consumption)

print(f'Общий расход ткани: '
      f'{round(coat.param/6.5 + 2*suit.param + 0.8, 2)} метров')

# 3. Осуществить программу работы с органическими клетками, состоящими
# из ячеек. Необходимо создать класс «Клетка». В его конструкторе
# инициализировать параметр, соответствующий количеству ячеек клетки
# (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов: сложение (__add__()), вычитание
# (__sub__()), умножение (__mul__()), деление
# (__floordiv__, __truediv__()). Эти методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и округление
# до целого числа деления клеток, соответственно.


class cell():
    def __init__(self, count):
        self.count = count

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки
# должно равняться сумме ячеек исходных двух клеток.

    def __add__(self, other):
        return self.count + other.count

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять,
# только если разность количества ячеек двух клеток больше нуля, иначе
# выводить соответствующее сообщение.

    def __sub__(self, other):
        if self.count - other.count > 0:
            return self.count - other.count
        else:
            return (f'Количество ячеек второй клетки ({self.count}) '
                    f'больше или равно количеству ячеек первой '
                    f'({other.count})')

# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки —
# произведение количества ячеек этих двух клеток.

    def __mul__(self, other):
        return self.count * other.count

# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки
# определяется как целочисленное деление количества ячеек этих двух
# клеток.

    def __floordiv__(self, other):
        return self.count // other.count

    def __truediv__(self, other):
        return round(self.count / other.count)

# В классе необходимо реализовать метод make_order(), принимающий
# экземпляр класса и количество ячеек в ряду. Этот метод позволяет
# организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где
# количество ячеек между \n равно переданному аргументу. Если ячеек на
# формирование ряда не хватает, то в последний ряд записываются все
# оставшиеся.

    def make_order(self, row):
        return (self.count // row * ('*' * row + '\n')
                + self.count % row * '*').rstrip()

        # order = []
        # while self.count > row:
        #     order.append('*' * row)
        #     self.count -= row
        # order.append('*' * self.count)
        # return '\n'.join(order)


first = cell(50)
second = cell(19)

print(first + second)
print(first - second)
print(second - first)
print(first * second)
print(first // second)
print(first / second)
print(first.make_order(10))
print(second.make_order(5))
