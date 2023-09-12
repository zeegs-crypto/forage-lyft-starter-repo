import unittest
from datetime import datetime

from engine.sternman_engine import SternmanEngine


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
