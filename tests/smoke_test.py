import unittest
from signin_test import SignInTest
from dashboard_test import DashboardTest

sign_in_tests = unittest.defaultTestLoader.loadTestsFromTestCase(SignInTest)
dashboard_tests = unittest.defaultTestLoader.loadTestsFromTestCase(DashboardTest)

smoke_tests = unittest.TestSuite([dashboard_tests, sign_in_tests])

unittest.TextTestRunner(verbosity=2).run(smoke_tests)
