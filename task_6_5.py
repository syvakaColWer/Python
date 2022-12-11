# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки:")
        print("**********************")


class Pen(Stationery):
    title = "- ручка"

    def draw(self):
        print(f"{self.title} пишет.")


class Pencil(Stationery):
    title = "- карандаш"

    def draw(self):
        print(f"{self.title} рисует.")


class Handle(Stationery):
    title = "- маркер"

    def draw(self):
        print(f"{self.title} подчёркивает.")


if __name__ == '__main__':
    stationery = Stationery()
    stationery.draw()
    pen = Pen()
    pen.draw()
    pencil = Pencil()
    pencil.draw()
    handle = Handle()
    handle.draw()
