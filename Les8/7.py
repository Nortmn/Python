class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} {"+" if (self.b * other.a + self.a * other.b) >= 0 else "-"}\
{abs(self.b * other.a + self.a * other.b)} * i'

    def __str__(self):
        return f'z = {self.a} {"+" if self.b >= 0 else "-"} {abs(self.b)} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
