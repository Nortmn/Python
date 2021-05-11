class Worker:

    def __init__(self, name, last_name, position, wage, bonus):
        self.name = name
        self.last_name = last_name
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):

    def full_name(self):
        return f'{self.name} {self.last_name}'

    def full_profit(self):
        return f'{sum(self._income.values())}'


worker_1 = Position('Sam', 'Smith', 'Meneger', 160000, 45000)
print(worker_1.full_name())
print(worker_1.full_profit())
print(worker_1.position)
