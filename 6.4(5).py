"""4.Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
 turn(direction), которые должны сообщать, что машина поехала, остановилась,
 повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
  PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
   текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
   show_speed. При значении скорости свыше 60 (TownCar)
 и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed: int, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Мащина {self.name} поехала')

    def stop(self):
        print(f'Мащина {self.name} остановилась')

    def turn(self, direction):
        print(f'Мащина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины равна {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Cкорость превышена({self.speed}км/ч)')
        else:
            print(f'Скорость машины равна {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Cкорость превышена')
        else:
            print(f'Скорость машины равна {self.speed} км/ч')


class PoliceCar(Car):
    pass


town = TownCar(70, 'черная', 'Toyota', False)
town.go()
town.turn('налево')
town.show_speed()
town.stop()
print(f'Данные о машине {town.name}: цвет - {town.color}, полицеская - {town.is_police}')

police = PoliceCar(90, 'белая', 'BMW', True)
police.go()
police.turn('направо')
police.show_speed()
police.stop()
print(f'Данные о машине {police.name}: цвет - {police.color}, полицеская - {police.is_police}')
