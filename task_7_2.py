# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
from typing import Any


class AClothes(ABC):
    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def dimensions(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AClothes):
    _clothes = []

    def __init__(self, name: str, dimensions: Any):
        self.name = name
        self._dimensions = dimensions
        self._tissue_required = None
        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:
        if not self._tissue_required:
            self._calc_tissue_required()
        return self._tissue_required

    @property
    def dimensions(self) -> Any:
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions: Any):
        self._dimensions = dimensions
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(self.dimensions / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        return self.dimensions

    @V.setter
    def V(self, size: Any):
        self.dimensions = size

    def __str__(self):
        return f"Для изготовления пальто {self.dimensions} размера требуется {self.tissue_required} кв.м. ткани."


class Suit(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.dimensions * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        return self.dimensions

    @H.setter
    def H(self, height: Any):
        self.dimensions = height

    def __str__(self):
        return f"Для изготовления костюма на рост {self.dimensions} см. требуется {self.tissue_required} кв.м. ткани."


if __name__ == '__main__':
    coat = Coat("Пальто", 7)
    print(coat)
    suit = Suit("Костюм", 185)
    print(suit)
    all = coat.total_tissue_required
    all = float('{:.2f}'.format(all))
    print("Всего требуется ткани: ", all)
    coat.V = 8
    print(coat)
    suit.H = 192
    print(suit)
    all = coat.total_tissue_required
    all = float('{:.2f}'.format(all))
    print("Всего требуется ткани: ", all)
