# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    _weight_sq_m: float = 0.05

    def __init__(self, length: [int, float], width: [int, float]):
        self._length = float(length)
        self._width = float(width)

    def weight_all(self, thickness: float) -> [float, None]:
        try:
            return (self._length * self._width * thickness * self._weight_sq_m)
        except TypeError:
            return None


if __name__ == '__main__':
    try:
        road = Road(1000, 30)
        print("Масса асфальта, необходимого для покрытия всей дороги, составит", road.weight_all(20), "тонн.")
    except TypeError:
        print("Не хватает аргументов.")
