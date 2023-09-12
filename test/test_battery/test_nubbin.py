import unittest
from datetime import datetime

from battery.nubbin import NubbinBattery


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        battery = NubbinBattery(today, today.replace(year=today.year - 5))
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        battery = NubbinBattery(today, today.replace(year=today.year - 3))
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
