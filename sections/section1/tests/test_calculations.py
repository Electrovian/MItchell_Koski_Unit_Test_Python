import unittest
from code.my_calculations import Calculations
class TestCalculations(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Calculations(8,2).get_sum(), 10, 'The sum is wrong.')
if __name__=='__main__':
    unittest.main()
