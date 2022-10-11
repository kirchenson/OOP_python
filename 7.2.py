""" Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм.
  У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
 для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
 Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property."""

import abc


class Clothes(abc.ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @property
    @abc.abstractmethod
    def calculate(self):
        pass


class Suit(Clothes):
    length: float

    def __init__(self, name: str, length: float):
        super().__init__(name)
        self.length = length

    @property
    def calculate(self):
        return f'{round(2 * self.length + 0.3, 3)} расход ткани - костюм {self.name}'


class Coat(Clothes):
    size: float

    def __init__(self, name: str, size: float):
        super().__init__(name)
        self.size = size

    @property
    def calculate(self):
        return f'{round(self.size / 6.5 + 0.5, 3)} расход ткани - пальто {self.name}'


coat = Coat('Burberry', 3.5)
print(coat.calculate)

suit = Suit('Сударь', 2.8)
print(suit.calculate)
