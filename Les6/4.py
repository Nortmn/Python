class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'New car: {self.name} (color {self.color}) car is police - {self.is_police}')

    def go(self):
        print(f'{self.name} car is go')

    def stop(self):
        print(f'{self.name} car is stop')

    def turn(self, direction):
        print(f'{self.name} car turn on the {"left" if direction == 0 else "right"}')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')


class TownCar(Car):

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}. Over speed' \
                  if self.speed > 60 else f'{self.name}: speed is {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}. Over speed' \
                  if self.speed > 40 else f'{self.name}: speed is {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('"Police"', 'blue', 80)
police_car.go()
police_car.show_speed()
police_car.turn(1)
police_car.stop()

print()
sport_car = SportCar('"Sport car"', 'green', 150)
sport_car.go()
sport_car.show_speed()
sport_car.turn(0)
sport_car.stop()

print()
work_car = WorkCar('"Work car"', 'black', 60)
work_car.go()
work_car.show_speed()
work_car.turn(1)
work_car.stop()

print()
town_car = TownCar('"Town car"', 'black', 59)
town_car.go()
town_car.show_speed()
town_car.turn(1)
town_car.stop()
