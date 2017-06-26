def square(num):
    return num*num


import unittest
class SquareTest(unittest.TestCase):

    def test_square_10(self):
        """ Is Square of 10 = 100 """
        self.assertTrue(square(10) == 100)


if __name__ == '__main__':
    unittest.main()
