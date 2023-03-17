import unittest
from PiTPM import Factorial
class FactorialTestCase(unittest.TestCase):
    def testing1(self):
        fact = Factorial()
        result = fact.factorial(2)
        self.assertEqual(result, 2)

    def testing2(self):
        fact = Factorial()
        result = fact.factorial(3)
        self.assertEqual(result, 6)

    def testing3(self):
        fact = Factorial()
        result = fact.factorial(4)
        self.assertEqual(result, 24)

    def testing4(self):
        fact = Factorial()
        result = fact.factorial(5)
        self.assertEqual(result, 120)

