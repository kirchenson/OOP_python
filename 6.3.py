"""3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
 содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
 Создать класс Position (должность) на базе класса Worker. В классе Position
 реализовать методы получения полного имени сотрудника (get_full_name) и дохода
 с учетом премии (get_total_income). Проверить работу примера на реальных данных
  (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    name: str
    surname: str
    position: str
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя {self.name} {self.surname}')

    def get_total_income(self):
        total = self._income['wage'] + self._income['bonus']
        print(f'Оклад с премией: {total}')


kira = Position('Кира', 'Бабаева', 'Директор', 50000, 15000)
print(kira.name, kira.surname, kira.position, kira._income)
kira.get_full_name()
kira.get_total_income()
