import Calculator

import unittest

class calculator_test(unittest.TestCase):
 def test_add(self):
    a=20
    b=45
    c=Calculator.add(a,b)
    self.assertEqual(a+b,c)

 def test_sub(self):
     a = 20
     b = 45
     c = Calculator.sub(a, b)
     self.assertEqual(a + b, c)

 def test_mul(self):
     a = 20
     b = 45
     c = Calculator.mul(a, b)
     self.assertEqual(a * b, c)

 def test_div(self):
     a = 20
     b = 45
     c = Calculator.div(a, b)
     self.assertEqual(a + b, c)

if __name__=="__main__":
    unittest.main();