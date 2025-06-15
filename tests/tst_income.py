from unittest import TestCase as tc
from context import irpf
import irpf.irpf # and now this should be the CLASS we want to test.

class test_income(tc):

    def setUp(self):
        self.taxer = irpf.irpf.irpf()

    def test_register_income_I(self):
        self.taxer.register_income(800.00)
        self.assertEqual(irpf.get_income(), float(800))

    def test_register_income_II(self):
        self.taxer.register_income(900.00)
        self.assertEqual(irpf.get_income(), float(900))

    def test_register_income_III(self):
        self.taxer.register_income(900.00)
        self.taxer.register_income(800.00)
        self.assertEqual(irpf.get_income(), float(1700))

