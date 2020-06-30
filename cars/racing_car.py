from .base_car import Car


class RacingCar(Car):
    def __init__(self, name=None):
        Car.__init__(self, name)

    def brakes(self):
        return "Racing Car brakes"

    def speed(self):
        return 220

    def drive_wheel(self):
        return "FRONT WHEEL DRIVE"
