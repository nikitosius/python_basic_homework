'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
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
        self.middle_profit = 0
        self.bonus = bonus

    @property
    def middle_profit_calc(self):
        self.middle_profit = (self._income["profit"]*self.percent)/100 + self._income["profit"]
        #return self.middle_profit

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_full_profit(self):
        full_profit = self.middle_profit + self.bonus
        return full_profit

position1 = Position("Иван", "Иванов", "Сварщик", 50000, 5000, 10)
print(position1.middle_profit_calc)
print(position1.get_full_profit())