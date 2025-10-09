import unittest
from code.my_calculations import Calculations

class TestCalculations(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Calculations(8, 2).get_sum(), 10, 'The sum is wrong.')

if __name__ == '__main__':
    result = unittest.main(exit=False)
    print("\n TEST RESULTS SUMMARY:")
    print(f"Ran {result.result.testsRun} tests")
    print(f"Failures: {len(result.result.failures)}")
    print(f"Errors: {len(result.result.errors)}")
    if not result.result.failures and not result.result.errors:
        print("ALL TESTS PASSED SUCCESSFULLY!")
    else:
        print("SOME TESTS FAILED — CHECK ABOVE OUTPUT.")
