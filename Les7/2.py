from abc import ABC, abstractmethod


class Clothe(ABC):

    def __init__(self):
        pass

    @property
    @abstractmethod
    def ras(self):
        pass

    def __add__(self, other):
        return self.ras + other.ras


class Coat(Clothe):

    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('Размеры начинаются с 40')
            self.__size = 40
        elif size > 58:
            print('Максимальный размер: 58')
            self.__size = 58
        else:
            self.__size = size

    @property
    def ras(self):
        return self.__size / 6.5 + 0.5

class Cost(Clothe):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('Не меньше 100')
            self.__height = 100
        elif height > 240:
            print('Максимум 240')
            self.__height = 240
        else:
            self.__height = height

    @property
    def ras(self):
        return 2 * (self.__height / 100) + 0.3


coat_1 = Coat(int(input('Введите размер пальто :')))
print(f'Потребуется {coat_1.ras: .2f} метров ткани на пальто размера {coat_1.size}')
cost_1 = Cost(int(input('Введите рост (в сантиметрах) :')))
print(f'Потребуется {cost_1.ras: .2f} метров ткани на костюм {cost_1.height} роста')
print(f'Всего потребуется {coat_1 + cost_1: .2f} метров ткани')
