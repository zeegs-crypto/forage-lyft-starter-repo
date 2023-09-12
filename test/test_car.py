import unittest
from datetime import datetime

from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_calliope(today, today.replace(year=today.year - 3), 0, 0)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_calliope(today, today.replace(year=today.year - 1), 0, 0)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_calliope(today, today, 30001, 0)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_calliope(today, today, 30000, 0)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_glissade(today, today.replace(year=today.year - 3), 0, 0)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_glissade(today, today.replace(year=today.year - 1), 0, 0)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_glissade(today, today, 60001, 0)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_glissade(today, today, 60000, 0)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_palindrome(today, today.replace(year=today.year - 3), False)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_palindrome(today, today.replace(year=today.year - 1), False)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_palindrome(today, today, True)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_palindrome(today, today, False)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_rorschach(today, today.replace(year=today.year - 5), 0, 0)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_rorschach(today, today.replace(year=today.year - 3), 0, 0)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_rorschach(today, today, 60001, 0)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_rorschach(today, today, 60000, 0)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_thovex(today, today.replace(year=today.year - 5), 0, 0)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_thovex(today, today.replace(year=today.year - 3), 0, 0)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_thovex(today, today, 30001, 0)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_thovex(today, today, 30000, 0)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
