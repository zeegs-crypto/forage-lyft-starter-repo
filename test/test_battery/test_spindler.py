import unittest
from datetime import datetime

from battery.spindler import SpindlerBattery


class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        battery = SpindlerBattery(today, today.replace(year=today.year - 4))
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        battery = SpindlerBattery(today, today.replace(year=today.year - 2))
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
