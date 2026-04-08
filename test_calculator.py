#https://github.com/Dsung0107/lab11-DS-YJ.git
#Partner 1: Derek Sung
#Partner 2: Yoonho Ji
import math
import unittest
from calculator import add, subtract, mul, div, logarithm, exp, square_root, hypotenuse

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(1,1),2)
        self.assertEqual(add(0,0),0)
        self.assertAlmostEqual(add(1.5,2.5),4)


    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,3),2)
        self.assertEqual(subtract(0,0),0)
        self.assertEqual(subtract(-2, -3), 1)
        self.assertAlmostEqual(subtract(3.5,1.5),2.0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,2), 4)
        self.assertEqual(mul(1,500), 500)
        self.assertEqual(mul(0,0), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,2), 1)
        self.assertEqual(div(2,1), 0.5)
        self.assertAlmostEqual(div(3,1), 0.33333333333)
    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10,100),2.0)
        self.assertAlmostEqual(logarithm(2,8),3)
        self.assertAlmostEqual(logarithm(math.e,math.e),1)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1,10)
        with self.assertRaises(ValueError):
            logarithm(-2,10)
        with self.assertRaises(ValueError):
            logarithm(2,-5)


    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -1)
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertAlmostEqual(hypotenuse(1,1), 1.4142136 )
        self.assertAlmostEqual(hypotenuse(2,2), 2.8284271)
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)


# Do not touch this
if __name__ == "__main__":
    unittest.main()