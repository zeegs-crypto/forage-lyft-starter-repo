import unittest
from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        engine = WilloughbyEngine(60001, 0)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        engine = WilloughbyEngine(60000, 0)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
