# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

income = int(input('Укажите вашу выручку за прошедший расчётный период: '))
cons = int(input('Укажите понесённые издержки за прошедший расчётный период: '))

if income > cons:
    print("Всё хорошо! Продолжайте работать в том же темпе!")
elif income == cons:
    print("Пора что-то менять!")
else:
    print("По-моему вам стоит подумать о смене рода деятельности!")