import unittest

from algorithms.heapsort import heapsort
from algorithms.mergesort import mergesort


class TestSort(unittest.TestCase):
    def test_heapsort(self):
        arr = [10, 1, 4, 3, 8, 2, 7, 9, 5, 6]

        arr = heapsort(arr)

        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_mergesort(self):
        arr = [10, 1, 4, 3, 8, 2, 7, 9, 5, 6]

        arr = mergesort(arr)

        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
