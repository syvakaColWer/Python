# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления
# произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def func_1(el_mult, el):
    return el_mult * el


print(
    f"Результат вычисления произведения чётных чисел от 100 до 1000 (включительно): {reduce(func_1, [el for el in range(99, 1001) if el % 2 == 0])}")
