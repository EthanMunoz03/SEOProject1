import unittest
from project.py import getInput


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(getInput(), )

if __name__ == '__main__':
    unittest.main()