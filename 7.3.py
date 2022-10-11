""" Реализовать программу работы с органическими клетками, состоящими из ячеек.
 Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
 соответствующий количеству ячеек клетки (целое число).
  В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление
клеток, соответственно."""


class Sector:
    _number: int

    def __init__(self, number: int):
        if number > 0:
            self._number = number
        else:
            print('Количество клеток это положительное число')

    def is_sector(self, other):
        assert isinstance(other, self.__class__)

    def __str__(self):
        return str(self._number)

    def __add__(self, other: 'Sector'):
        self.is_sector(other)
        summ = self._number + other._number
        return summ

    def __sub__(self, other: 'Sector'):
        self.is_sector(other)
        sub = self._number - other._number
        if sub > 0:
            return sub
        else:
            return 'Разность меньше нуля'

    def __mul__(self, other: 'Sector'):
        self.is_sector(other)
        mul = self._number * other._number
        return mul

    def __truediv__(self, other: 'Sector'):
        self.is_sector(other)
        truediv = self._number / other._number
        return truediv

    @property
    def number(self):
        return int(self._number)

    @staticmethod
    def make_order(obj: 'Sector', step: int) -> str:
        stars = '*' * obj.number
        parts = [stars[i:i + step] for i in range(0, len(stars), step)]

        return '\n'.join(parts)

sector_1 = Sector(5)
sector_2 = Sector(7)

print(f'{sector_1 + sector_2} - сложение, {sector_2 - sector_1} - вычитание , {sector_2 * sector_1} - умножение, {sector_2 / sector_1} - деление')
print(Sector.make_order(sector_2, 3))