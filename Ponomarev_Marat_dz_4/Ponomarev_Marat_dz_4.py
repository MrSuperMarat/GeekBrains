# 4. Написать свой модуль utils и перенести в него функцию currency_rates()
# из предыдущего задания. Создать скрипт, в котором импортировать этот модуль
# и выполнить несколько вызовов функции currency_rates(). Убедиться, что
# ничего лишнего не происходит.

import utils as u

print(*u.currency_rates('USD'), sep=', ')
print(*u.currency_rates('eur'), sep=', ')
