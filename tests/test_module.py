import unittest
from app import sumar, restar, multiplicar, calcular_media



class TestModule(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 2), 4)


    def test_restar(self):
        self.assertEqual(restar(2, 2), 0)


    def  test_mutiplicar(self):
        self.assertEqual(multiplicar(2, 2), 4)


    def test_calcular_media(self):
        self.assertEqual(calcular_media([1, 2, 3, 4, 5]), 3)


if __name__ == '__main__':
    unittest.main()