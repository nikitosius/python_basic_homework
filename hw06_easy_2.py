'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
class Worker:
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus, percent):
        Worker.__init__(self, name, surname, position, profit, bonus)
        self.percent = percent

    @property
    def middle_profit_calc(self):
        middle_profit = (self._income["profit"]*self.percent)/100 + self._income["profit"]
        return middle_profit

position1 = Position("Иван", "Иванов", "Сварщик", 50000, 5000, 10)
print(position1.middle_profit_calc)