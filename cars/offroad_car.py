from .base_car import Car


class OffroadCar(Car):
    def __init__(self, name=None):
        Car.__init__(self, name)

    def brakes(self):
        return "Offroad Car brakes"

    def speed(self):
        return 110

    def drive_wheel(self):
        return "ALL WHEEL DRIVE!"
