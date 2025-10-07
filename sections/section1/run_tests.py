# sections/section1/run_tests.py
import os, sys, unittest
sys.path.insert(0, os.path.dirname(__file__))
loader = unittest.TestLoader()
suite = loader.discover(start_dir=os.path.join(os.path.dirname(__file__), 'tests'))
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
print("\n✅ TEST RESULTS SUMMARY:")
print(f"Ran {result.testsRun} tests")
print(f"Failures: {len(result.failures)}")
print(f"Errors: {len(result.errors)}")
if not result.failures and not result.errors:
    print("✅ ALL TESTS PASSED SUCCESSFULLY!")
else:
    print("❌ SOME TESTS FAILED — CHECK ABOVE OUTPUT.")
