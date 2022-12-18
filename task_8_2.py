# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class CantDevideByZero(Exception):
    text = "Делить на ноль нельзя!"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise CantDevideByZero
        return Number(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(Number, input(
                "Введите делимое и делитель через пробел (ENTER - завершение работы программы): \n").split())
            print(dividend / divider)
        except CantDevideByZero as e:
            print(e)
        except ValueError as e:
            print(e)
            break
