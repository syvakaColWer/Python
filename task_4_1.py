# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта
# для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    if len(argv) > 1:
        name_script, prodact, bid, premium = argv
        prodact = int(prodact)
        bid = int(bid)
        premium = int(premium)
        print((prodact * bid) + premium)
    else:
        prodact = int(input("Выработка в часах: "))
        bid = int(input("Ставка в час: "))
        premium = int(input("Премия: "))
        print((prodact * bid) + premium)
except ValueError:
    print("Не корректный ввод!")
