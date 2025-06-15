from unittest import TestCase as tc
from context import irpf
import irpf.irpf # and now this should be the CLASS we want to test.

class test_dependant(tc):

    def setUp(self):
        self.taxer = irpf.irpf.irpf()

    def test_dependant_I(self):
        self.taxer.register_dependant("John")
        self.assertEqual(self.taxer.get_deduction(), float(150))

    def test_dependant_I(self):
        self.taxer.register_dependant("John")
        self.taxer.register_dependant("Snake")
        self.assertEqual(self.taxer.get_deduction(), float(300))