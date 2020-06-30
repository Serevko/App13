from cars.adapter import SpeedAdapter
from cars.racing_car import RacingCar
from cars.offroad_car import OffroadCar
import unittest

class TestCars(unittest.TestCase):

    def test_RacingCar_class(self):
        racing_car_instance = RacingCar(name="Some Racing Car")

        self.assertEqual(racing_car_instance.brakes(), 'Racing Car brakes')
        self.assertTrue(racing_car_instance.speed() is 220)
        self.assertEqual(racing_car_instance.drive_wheel(), 'FRONT WHEEL DRIVE')

    def test_OffroadCar_class(self):
        offroad_car_instance = OffroadCar(name="Some Offroad Car")

        self.assertEqual(offroad_car_instance.brakes(), 'Offroad Car brakes')
        self.assertTrue(offroad_car_instance.speed() is 110)
        self.assertEqual(offroad_car_instance.drive_wheel(), 'ALL WHEEL DRIVE!')

    def test_Adapter(self):
        racing_car_instance = RacingCar(name="Some Racing Car")
        offroad_car_instance = OffroadCar(name="Some Offroad Car")

        racing_car_in_city = SpeedAdapter(racing_car_instance)
        offroad_car_in_city = SpeedAdapter(offroad_car_instance)

        # Adapted method speed() in RacingCar[220] and Offroad[110] classes
        # to 50 through SpeedAdapter class(Adapter)
        self.assertTrue(racing_car_in_city.speed() is 50)
        self.assertTrue(offroad_car_in_city.speed() is 50)

if __name__ == '__main__':
    unittest.main()
