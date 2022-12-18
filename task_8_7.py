# **7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_num:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = "a + b * i"

    def __add__(self, other):
        print(f"Сумма: ")
        return f"z = {self.a + other.a} + ({self.b + other.b} * i)"

    def __mul__(self, other):
        print(f"Произведение: ")
        return f"z = {self.a * other.a - (self.b * other.b)} + ({self.b * other.a} * i)"

    def __str__(self):
        return f"z = {self.a} + ({self.b} * i)"


num_1 = Complex_num(5, -1)
num_2 = Complex_num(5, -1)
print(num_1)
print(num_1 + num_2)
print(num_1 * num_2)
