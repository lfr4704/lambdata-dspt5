import unittest

def calc_area(l,w):
    """
    calculates area.
    """
    if l <=0 or w <=0:
        raise ValueError
    return l * w

class TestRectangles(unittest.TestCase):

    def test_calc_area(self):
        self.assertEqual(calc_area(5,3), 15)

        with self.assertRaises(ValueError):
            calc_area(-5, 3)

        with self.assertRaises(ValueError):
            calc_area(5,-3)

    def test_calc_area_positive(self):
        pass

if __name__ == '__main__':
    unittest.main()
