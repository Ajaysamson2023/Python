import unittest
from second_max_number.core.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input=second_max([2,3,5,4])
        expected_output=4
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()

