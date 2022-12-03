# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа
# запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(*args):
    try:
        numb_1 = int(input("Введите делимое: "))
        numb_2 = int(input("Введите делитель: "))
        result = numb_1 / numb_2
    except ValueError:
        return "Ошибка при делении!"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return result


print(f'Результат деления: {division()}')