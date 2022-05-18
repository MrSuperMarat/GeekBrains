# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя
# ключевое слово yield


def odd_nums(n):
    for i in range(1, 15 + 1, 2):
        yield i


odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))

# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n
# (включительно), не используя ключевое слово yield.

# n = int(input())
# odd_num = (i for i in range(1, n + 1, 2))
#
# print(next(odd_num))
# print(next(odd_num))

# 3. Есть два списка:

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# Необходимо реализовать генератор, возвращающий кортежи вида
# (<tutor>, <klass>).


def tutor_klass():
    if len(klasses) < len(tutors):
        for i in range(len(klasses)):
            yield tutors[i], klasses[i]
        for i in range(len(klasses), len(tutors)):
            yield tutors[i], None
    else:
        for i in range(len(tutors)):
            yield tutors[i], klasses[i]


ttr_kls = tutor_klass()

print(next(ttr_kls))
print(next(ttr_kls))
print(next(ttr_kls))
print(next(ttr_kls))
print(next(ttr_kls))
print(next(ttr_kls))
print(next(ttr_kls))
# print(next(ttr_kls))

# 4. Представлен список чисел. Необходимо вывести те его элементы, значения
# которых больше предыдущего.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([src[i] for i in range(1, len(src)) if src[i] > src[i - 1]])

# 5. Представлен список чисел. Определить элементы списка, не имеющие
# повторений. Сформировать из этих элементов список с сохранением порядка их
# следования в исходном списке.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_low = []
count_num = {}

for i in range(len(src)):
    count_num[src[i]] = count_num.setdefault((src[i]), 0) + 1
    if src[i] not in src_low:
        src_low.append(src[i])

result = [i for i in src_low if count_num[i] == 1]

print(result)
