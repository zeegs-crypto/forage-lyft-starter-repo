import unittest

from tires.octoprime import OctoprimeTires


class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensors = [1, 1, 1, 0]
        tires = OctoprimeTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        sensors = [1, 0.9, 1, 0]
        tires = OctoprimeTires(sensors)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
