import unittest
from app import sumar, restar



class TestModule(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 2), 4)


    def test_restar(self):
        self.assertEqual(restar(2, 1), 0)


if __name__ == '__main__':
    unittest.main()