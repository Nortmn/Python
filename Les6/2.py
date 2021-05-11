class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def full_prof(self, weight=25, thickness=5):
        return f'{self._length} m * {self._width} m * {weight} kg * {thickness} cm = ' \
               f'{(self._length * self._width * weight * thickness) / 1000} t'


road_1 = Road(5000, 20)
print(road_1.full_prof())
