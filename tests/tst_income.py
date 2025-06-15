from unittest import TestCase as tc
from context import irpf # and now this should be the CLASS we want to test.

class test_income(tc):

    def test_register_income_I(self):
        self.assertEqual(irpf.register_income(800.00), float(800))

    def test_register_income_I(self):
        self.assertEqual(irpf.register_income(800.00), float(800))

