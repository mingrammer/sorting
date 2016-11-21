import random
import unittest

from algorithms.heapsort import heapsort
from algorithms.mergesort import mergesort


class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [random.randint(1, 1000) for _ in range(100)]

    def test_heapsort(self):
        heapsorted_arr = heapsort(self.arr)

        self.assertEqual(heapsorted_arr, sorted(self.arr))

    def test_mergesort(self):
        mergesorted_arr = mergesort(self.arr)

        self.assertEqual(mergesorted_arr, sorted(self.arr))


if __name__ == '__main__':
    unittest.main()
