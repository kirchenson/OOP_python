"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
 (метод init()),
 который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
 двух объектов класса Matrix (двух матриц).
 Результатом сложения должна быть новая матрица.
."""


class Matrix:
    matrix = []

    def __init__(self, matrix: list):
        self.matrix = matrix

    def __add__(self, other: "Matrix"):
        rows = len(self.matrix)
        items = len(self.matrix[0])

        new_matrix = [
            [
                self.matrix[r][i] + other.matrix[r][i]
                for i in range(items)
            ]
            for r in range(rows)
        ]

        return Matrix(new_matrix)

    def __str__(self):
        return '\n'.join(str(r) for r in self.matrix)


m1 = Matrix([[11, 12, 13], [14, 15, 16]])
m2 = Matrix([[21, 22, 23], [24, 25, 26]])

print(m1 + m2)
