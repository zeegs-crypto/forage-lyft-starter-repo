import unittest

from tires.carrigan import CarriganTires


class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensors = [0, 0.9, 0, 0]
        tires = CarriganTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        sensors = [0, 0.8, 0, 0]
        tires = CarriganTires(sensors)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
