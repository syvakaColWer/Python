# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

count = int(input("Укажите количество элементов: "))
list_1 = []
i = 0

while i < count:
    list_1.append(input("Введите значение " + str(i + 1) + " элемента: "))
    i += 1

n = 0

while n < (len(list_1) // 2) * 2:
    list_1[n], list_1[n + 1] = list_1[n + 1], list_1[n]
    n += 2

print("Итоговый список: ", list_1)

