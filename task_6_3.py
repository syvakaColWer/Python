# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self, reverse=False):
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Уильям',
            'surname': 'Шекспир',
            'position': 'Юрист',
            'wage': 45000,
            'bonus': 1000
        },
        {
            'name': 'Лев',
            'surname': 'Толстой',
            'position': 'Директор',
            'wage': 55000,
            'bonus': 10000
        },
        {
            'name': 'Александр',
            'surname': 'Пушкин',
            'position': 'Главный инженер',
            'wage': 50000,
            'bonus': 5000
        },
        {
            'name': 'Бэлла',
            'surname': 'Ахмадулина',
            'position': 'Секретарь',
            'wage': 20000,
            'bonus': 1000
        },
    ]

    for item in position_data:
        position = Position(**item)
        print("Данные: ", item)
        print("Имя работника: ", position.name)
        print("Фамилия работника: ", position.surname)
        print("Фамилия/Имя работника: ", position.get_full_name(reverse=True))
        print("Должностиь работника: ", position.position)
        print("Заработная плата работника: ", position.get_total_income(), "\n")
