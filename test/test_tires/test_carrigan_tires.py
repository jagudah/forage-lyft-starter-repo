import unittest
from car_factory.tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires = CarriganTires([0.9, 0, 0, 0])
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires = CarriganTires([0.8, 0.1, 0.2, 0.5])
        self.assertFalse(tires.needs_service())