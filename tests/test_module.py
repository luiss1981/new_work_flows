import unittest
from app import sumar, restar, multiplicar



class TestModule(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 2), 4)


    def test_restar(self):
        self.assertEqual(restar(2, 2), 0)


    def  test_mutiplicar(self):
        self.assertEqual(multiplicar(2, 2), 4)


if __name__ == '__main__':
    unittest.main()