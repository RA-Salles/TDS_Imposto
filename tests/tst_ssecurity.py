from unittest import TestCase as tc
from context import irpf
import irpf.irpf # and now this should be the CLASS we want to test.

class test_social_security(tc):

    def setUp(self):
        self.taxer = irpf.irpf.irpf()

    def test_social_security_I(self):
        self.taxer.register_pension(800.00)
        self.assertEqual(self.taxer.get_pension(), float(800))
