import unittest
from calender_module.core.utils import *
import calendar


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input=calender_mod()
        expected_output="MONDAY"
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()
