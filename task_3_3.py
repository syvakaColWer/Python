# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму
# наибольших двух аргументов.

def summ(ch_1 , ch_2, ch_3):
    if ch_1 >= ch_3 and ch_2 >= ch_3:
        return ch_1 + ch_2
    elif ch_1 >= ch_2:
        return ch_1 + ch_3
    else:
        return ch_2 + ch_3

print(f'Сумма больших чисел: {summ(int(input("Первое число: ")), int(input("Второе число: ")), int(input("Третье число: ")))}')