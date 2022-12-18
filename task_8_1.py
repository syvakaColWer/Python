# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def extract(cls, d_m_y):
        set_date = []
        for i in d_m_y.split():
            if i != '-': set_date.append(i)
        return int(set_date[0]), int(set_date[1]), int(set_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f"Всё верно."
                else:
                    return f"Год введён не корректно."
            else:
                return f"Месяц введён не корректно."
        else:
            return f"День введён не корректно."

    def __str__(self):
        return f"Задана дата: {Data.extract(self.d_m_y)}"


set_day = Data("1 - 1 - 2022")
print(set_day)
print(Data.valid(12, 12, 2022))
print(set_day.valid(13, 13, 2022))
print(Data.extract("01 - 12 - 2022"))
print(set_day.extract("18 - 12 - 2022"))
print(Data.valid(1, 1, 2022))
