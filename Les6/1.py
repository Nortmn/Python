from time import sleep


class TrafficLight:
    _color = "Чёрный"

    def runing(self):
        while True:
            print("Красный")
            sleep(7)
            print("Жёлтый")
            sleep(2)
            print("Зелёный")
            sleep(7)
            print("Жёлтый")
            sleep(2)


trafficLight = TrafficLight()
trafficLight.runing()
