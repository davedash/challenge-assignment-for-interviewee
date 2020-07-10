import unittest

from challenge import average_without_extremes


class TestAverage(unittest.TestCase):

    def test_basic(self):
        assert 3.0 == average_without_extremes([1, 2, 3, 4, 99])


if __name__ == '__main__':
    unittest.main()
