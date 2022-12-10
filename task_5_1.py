# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

my_f = open("text_1.txt", "w")
line_1 = input("Введите строку текста: ")
while line_1:
    my_f.writelines(line_1)
    line_1 = input("Введите следующую строку текста (ENTER сразу - закончить ввод): ")
    if not line_1:
        break

my_f.close()
my_f = open('text_1.txt', 'r')
content = my_f.readlines()
print("Результат ввода: ", content)
my_f.close()