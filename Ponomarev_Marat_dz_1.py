# 1. Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах

duration = int(input())
if duration < 60:
    print(duration, 'cек')
elif 60 <= duration < 3600:
    print(duration // 60, 'мин', duration % 60, 'cек')
elif 3600 <= duration < 216000:
    print(duration // 3600, 'час', duration % 3600 // 60, 'мин',
          duration % 60, 'сек')
else:
    print(duration // 86400, 'дн', duration % 86400 // 3600, 'час',
          duration % 3600 // 60, 'мин', duration % 60, 'сек')

# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):

cubes = [i**3 for i in range(1, 1000, 2)]

# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых
# делится нацело на 7.

sum_cub = 0
for i in cubes:
    sum_num = 0
    for j in str(i):
        sum_num += int(j)
    if sum_num % 7 == 0:
        sum_cub += sum_num
print(sum_cub)

# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел
# из этого списка, сумма цифр которых делится нацело на 7.

cubes_new = [cubes[i] + 17 for i in range(len(cubes))]
sum_cub = 0
for i in cubes_new:
    sum_num = 0
    for j in str(i):
        sum_num += int(j)
    if sum_num % 7 == 0:
        sum_cub += sum_num
print(sum_cub)


# c. * Решить задачу под пунктом b, не создавая новый список.

sum_cub = 0
for i in range(len(cubes)):
    sum_num = 0
    for j in str(cubes[i] + 17):
        sum_num += int(j)
    if sum_num % 7 == 0:
        sum_cub += sum_num
print(sum_cub)

# 3. Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из
# чисел в интервале от 1 до 100:

for i in range(1, 101):
    if i == 1:
        print(i, 'процент')
    elif i < 5:
        print(i, 'процента')
    else:
        print(i, 'процентов')
