# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей
# структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
# (как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем
# можно было менять имена папок под конкретный проект; можно ли будет при этом
# расширять конфигурацию и хранить данные о вложенных папках и файлах
# (добавлять детали)?

import os
from shutil import copy2
import json

folder = r'D:\Работа\Data_Engineer\Python\Ponomarev_Marat_dz_7'

project = os.path.join(folder, 'my_project')
if not os.path.exists(project):
    os.makedirs(project)

dir_settings = os.path.join(project, 'settings')
if not os.path.exists(dir_settings):
    os.makedirs(dir_settings)
dir_mainapp = os.path.join(project, 'mainapp')
if not os.path.exists(dir_mainapp):
    os.makedirs(dir_mainapp)
dir_adminapp = os.path.join(project, 'adminapp')
if not os.path.exists(dir_adminapp):
    os.makedirs(dir_adminapp)
dir_authapp = os.path.join(project, 'authapp')
if not os.path.exists(dir_authapp):
    os.makedirs(dir_authapp)

# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи
# скрипта или «руками» в проводнике). Написать скрипт, который собирает все
# шаблоны в одну папку templates, например:

settings = ['__init__.py', 'dev.py', 'prod.py']
for i in settings:
    with open(os.path.join(dir_settings, i), 'w', encoding='UTF-8'):
        pass

mainapp = ['__init__.py', 'models.py', 'views.py']
for i in mainapp:
    with open(os.path.join(dir_mainapp, i), 'w', encoding='UTF-8'):
        pass

authapp = ['__init__.py', 'models.py', 'views.py']
for i in authapp:
    with open(os.path.join(dir_authapp, i), 'w', encoding='UTF-8'):
        pass

dir_temp_mainapp = os.path.join(dir_mainapp, r'templates\mainapp')
if not os.path.exists(dir_temp_mainapp):
    os.makedirs(dir_temp_mainapp)
dir_temp_authapp = os.path.join(dir_authapp, r'templates\authapp')
if not os.path.exists(dir_temp_authapp):
    os.makedirs(dir_temp_authapp)

templates = ['base.html', 'index.html']
for i in templates:
    with open(os.path.join(dir_temp_mainapp, i), 'w', encoding='UTF-8')\
            as temp_mainapp,\
            open(os.path.join(dir_temp_authapp, i), 'w', encoding='UTF-8')\
            as temp_authapp:
        temp_mainapp.write('Шаблон mainapp')
        print('Шаблон authapp', file=temp_authapp)

dir_templates = os.path.join(folder, 'templates')
if not os.path.exists(dir_templates):
    os.makedirs(dir_templates)

for root, dirs, files in os.walk(project):
    for file in files:
        if file.rsplit('.', maxsplit=1)[-1].lower() == 'html':
            dir_temp = os.path.join(dir_templates,
                                    root.rsplit('\\', maxsplit=1)[-1])
            if not os.path.exists(dir_temp):
                os.makedirs(dir_temp)
            copy2(os.path.join(root, file), os.path.join(
                os.path.join(
                    os.path.join(folder, 'templates'),
                    root.rsplit('\\', maxsplit=1)[-1]), file))

# 4. Написать скрипт, который выводит статистику для заданной папки в виде
# словаря, в котором ключи — верхняя граница размера файла
# (пусть будет кратна 10), а значения — общее количество файлов (в том
# числе и в подпапках), размер которых не превышает этой границы, но
# больше предыдущей (начинаем с 0).

homeworks = r'D:\Работа\Data_Engineer\Python'

# sizes = {}
# # extension = {}
# for root, dirs, files in os.walk(homeworks):
#     for file in files:
#         size = os.stat(os.path.join(root, file)).st_size
#         if size <= 100:
#             sizes[100] = (sizes.setdefault(100, 1) + 1)
#             # set[100] = sizes.setdefault(100, [])
#         elif 100 < size <= 1000:
#             sizes[1000] = sizes.setdefault(1000, 0) + 1
#         elif 1000 < size <= 10000:
#             sizes[10000] = sizes.setdefault(10000, 0) + 1
#         elif 10000 < size <= 100000:
#             sizes[100000] = sizes.setdefault(100000, 0) + 1
#
# sizes = {x: sizes[x] for x in sorted(sizes)}
# print(sizes)

# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной
# папки в виде словаря, в котором ключи те же, а значения — кортежи вида
# (<files_quantity>, [<files_extensions_list>]).
# Сохраните результаты в файл <folder_name>_summary.json в той же папке,
# где запустили скрипт.

sizes = {}
extension = {}
for root, dirs, files in os.walk(homeworks):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        if size <= 100:
            sizes[100] = (sizes.setdefault(100, 1) + 1)
            extension[100] = extension.setdefault(100, set())
            extension[100].add(file.rsplit('.', maxsplit=1)[-1])
        elif 100 < size <= 1000:
            sizes[1000] = sizes.setdefault(1000, 0) + 1
            extension[1000] = extension.setdefault(1000, set())
            extension[1000].add(file.rsplit('.', maxsplit=1)[-1])
        elif 1000 < size <= 10000:
            sizes[10000] = sizes.setdefault(10000, 0) + 1
            extension[10000] = extension.setdefault(10000, set())
            extension[10000].add(file.rsplit('.', maxsplit=1)[-1])
        elif 10000 < size <= 100000:
            sizes[100000] = sizes.setdefault(100000, 0) + 1
            extension[100000] = extension.setdefault(100000, set())
            extension[100000].add(file.rsplit('.', maxsplit=1)[-1])

statistic = {}

for i in sorted(sizes):
    statistic[i] = (sizes[i], list(extension[i]))

print(statistic)

# with open('Ponomarev_Marat_dz_7_summary.json', 'w', encoding='UTF-8') as f:
#     statistic_as_str = json.dumps(statistic)
#     f.write(statistic_as_str)

with open('Ponomarev_Marat_dz_7_summary.json', 'w', encoding='UTF-8') as f:
    json.dump(statistic, f)
