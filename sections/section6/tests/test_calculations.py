import unittest
from code.my_calculations import Calculations
class TestCalculations(unittest.TestCase):
    def test_sum(self): self.assertEqual(Calculations(8,2).get_sum(), 10)
    def test_diff(self): self.assertEqual(Calculations(8,2).get_difference(), 6)
    def test_product(self): self.assertEqual(Calculations(8,2).get_product(), 16)
    def test_quotient(self): self.assertEqual(Calculations(8,2).get_quotient(), 4)
if __name__=='__main__': unittest.main()
