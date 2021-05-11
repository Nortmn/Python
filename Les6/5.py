class Stationery:

    def __init__(self, title='Something that can be draw'):
        self.title = title

    def draw(self):
        print(f'Start drawing {self.title}')


class Pen(Stationery):

    def draw(self):
        print(f'Drawing with {self.title} pen')


class Pencil(Stationery):

    def draw(self):
        print(f'Drawing with {self.title} pencil')


class Marker(Stationery):

    def draw(self):
        print(f'Drawing with {self.title} marker')


stat_1 = Stationery()
stat_1.draw()
pen_1 = Pen("Pilot")
pen_1.draw()
pencil_1 = Pencil('VENTE')
pencil_1.draw()
marker_1 = Marker('COPIC')
marker_1.draw()
