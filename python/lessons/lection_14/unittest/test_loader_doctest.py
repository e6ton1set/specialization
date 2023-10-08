import doctest
import unittest
import prime


#  тестирование doctest через unittest
def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(prime))
    tests.addTests(doctest.DocFileSuite('../doctest/prime.md'))
    return tests


if __name__ == '__main__':
    unittest.main()