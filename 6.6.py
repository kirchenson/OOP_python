"""6. Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.”
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
  В каждом из классов реализовать переопределение метода draw.
  Для каждого из классов метод должен выводить уникальное сообщение.
   Создать экземпляры классов и проверить,
 что выведет описанный метод для каждого экземпляра."""


class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки рисунка "{self.title}"!')


class Pen(Stationery):
    def draw(self):
        print(f'Рисунок "{self.title}" будет выполнен ручкой!')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисунок "{self.title}" будет выполнен карандашом!')


class Handle(Stationery):
    def draw(self):
        print(f'Рисунок "{self.title}" будет выполнен маркером!')


view = Stationery('Пейзаж')
view.draw()
face = Pen('Портрет')
face.draw()
