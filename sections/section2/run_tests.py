# sections/section2/run_tests.py
import os
import sys
import unittest

# make sure current folder is on sys.path
sys.path.insert(0, os.path.dirname(__file__))

# import the actual test case
from tests.test_calculations import TestCalculations

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCalculations)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n DETAILED TEST SUMMARY:")
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

    # list failures and errors explicitly
    print("\n Individual Test Results:")
    for test, tb in result.failures:
        print(f" FAIL: {test}")
    for test, tb in result.errors:
        print(f"  ERROR: {test}")

    # show passes
    all_tests = set(str(t) for t in suite)
    failed = {str(f[0]) for f in result.failures + result.errors}
    for test_name in all_tests - failed:
        print(f" Failed: {test_name}")

    if not result.failures and not result.errors:
        print("\n ALL TESTS PASSED SUCCESSFULLY!")
    else:
        print("\n SOME TESTS FAILED — CHECK ABOVE OUTPUT.")
