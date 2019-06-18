import unittest

from questions_1_2 import *


class UnitTests(unittest.TestCase):
    def test_line_overlap(self):
        """
        Test for lines overlap, and the sample test should Pass
        """
        result = overlap_indicator([1, 5], [6, 8])
        self.assertFalse(result, False)

    def test_string_comparison(self):
        """
        Test for string comparison, and the sample test should Pass
        """
        result = string_comparison('3.9', '3.6')
        self.assertEqual(result, 'greater then', 'Should be greater then')


if __name__ == '__main__':
    unittest.main()
