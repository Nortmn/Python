class Cell:
    def __init__(self, num):
        self.num = num

    def make_ord(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.num // rows)]) + '\n' + '*' * (self.num % rows)

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        print('Сумма клеток :')
        return Cell(self.num + other.num)

    def __sub__(self, other):
        print('Разность :')
        return Cell(self.num - other.num) if self.num - other.num > 0 \
            else 'В первой клетке ячеек меньше чем во второй'

    def __mul__(self, other):
        print('Произведение :')
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        print('Частное :')
        return Cell(self.num // other.num)


cel_1 = Cell(10)
cel_2 = Cell(30)
print(cel_1 + cel_2)
print(cel_1 - cel_2)
print(cel_1 * cel_2)
print(cel_1 // cel_2)
print(cel_2.make_ord(7))
