# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начинает движение'

    def stop(self):
        return f'{self.name} останавливается'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} - {self.speed}')
        if self.speed > 40:
            return f'Скорость {self.name} превышает порог для движения по городу'
        else:
            return f'Скорость {self.name} нормальная для движения по городу'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} - {self.speed}')
        if self.speed > 60:
            return f'Скорость {self.name} выше, чем это необходимо для рабочего автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - это полицейская машина'
        else:
            return f'{self.name} - это не полицейский автомобиль'


ferrari = SportCar(100, 'чёрного', 'Феррари', False)
lada = TownCar(80, 'оранжевого', 'Лада', False)
sobol = WorkCar(60, 'белого', 'Соболь', True)
toyota = PoliceCar(90, 'синего', 'Камри', True)
print(sobol.turn_left())
print(f'Когда {lada.turn_right()}, тогда {ferrari.stop()}')
print(f'{sobol.go()} со скоростью {sobol.show_speed()}')
print(f'{sobol.name} {sobol.color} цвета.')
print(f'{ferrari.name} - это полицейская машина? {ferrari.is_police}')
print(f'{toyota.name} - это полицейская машина? {toyota.is_police}')
print(ferrari.show_speed())
print(lada.show_speed())
print(toyota.police())
print(toyota.show_speed())
