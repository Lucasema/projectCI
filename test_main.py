import unittest
import main


class TestClass(unittest.TestCase):

    def test_add(self):
        result = main.add(10, 5)
        self.assertEquals(result, 11)


if __name__ == '__main__':
    unittest.main()