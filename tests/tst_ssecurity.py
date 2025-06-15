from unittest import TestCase as tc
from context import irpf
import irpf.irpf # and now this should be the CLASS we want to test.

class test_social_security(tc):

    def setUp(self):
        self.taxer = irpf.irpf.irpf()

    def test_social_security_I(self):
        #tests registering and getting
        self.taxer.register_pension(800.00)
        self.assertEqual(self.taxer.get_pension(), float(800))
    
    def test_social_security_II(self):
        #tests put and get, too
        self.taxer.register_pension(1200.00)
        self.assertEqual(self.taxer.get_pension(), float(1200))
    
    def test_social_security_III(self):
        #tests overwriting.
        self.taxer.register_pension(900)
        self.taxer.register_pension(800)
        self.taxer.register_pension(9000)
        self.assertEqual(self.taxer.get_pension(), float(9000)) 

        