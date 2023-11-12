import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        rectangle = Rectangle(3, 3, 1, 1)
        self.assertNotEqual(rectangle.area(), 12)

if __name__ == '__main__':
    unittest.main()
