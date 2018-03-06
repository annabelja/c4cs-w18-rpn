import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
#    def test_sum(self):
 #       rpn.calculate('1 1 -')
  #      result = rpn.calculate('1 s')
   #     self.assertEqual(1, result)
    def test_adds(self):
        result = rpn.calculate('1 1 + 2 +')
        self.assertEqual(4, result)
    def test_subtract(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)
    def test_toomany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 2 3 + ')
    def test_multiply(self):
        result = rpn.calculate('4 3 *')
        self.assertEqual(12, result)
    def test_divide(self):
        result = rpn.calculate('10 5 /')
        self.assertEqual(2, result)
    def test_truedivide(self):
        result = rpn.calculate('5 2 /')
        self.assertEqual(2.5, result)
    def test_mixofoperators(self):
        result = rpn.calculate('10 5 / 2 +')
        self.assertEqual(4, result)
    def test_power(self):
        result = rpn.calculate('2 1 ^')
        self.assertEqual(2, result)
#    def test_intDivision(self):
 #       result = rpn.calculate('5 2 .')
  #      self.assertEqual(2, result)
    def test_bitwiseAnd(self):
        result = rpn.calculate('1 1 &')
        self.assertEqual(1, result)
    def test_bitwiseOr(self):
        result = rpn.calculate('1 0 |')
        self.assertEqual(1, result)
#    def test_bitwiseNot(self):
 #       result = rpn.calculate('1 !')
  #      self.assertEqual(0, result)
   # def test_copy(self):
    #    rpn.calculate('1 1 +')
     #   self.assertEqual(2, 2)
