from unittest import TestCase
from src import quick_sort, bubble_sort, merge_sort, counting_sort


class Test(TestCase):

    # Bubble sorting tests

    def test_bubble_sort(self):
        data = ['o', 'z', 'f']
        self.assertListEqual(sorted(data), bubble_sort.sort(data))

    # Quick sorting tests

    def test_divide(self):
        data = [5, 1, 7, 6]
        self.assertEqual(2, quick_sort.divide(data, 0, 3))

    def test_divide_chars(self):
        data = [',', 'z', 'a']
        self.assertEqual(1, quick_sort.divide(data, 0, 2))

    def test_quick_sort(self):
        data = [29, 3, 92, 2, 4]
        self.assertListEqual(sorted(data), quick_sort.sort(data))

    def test_quick_sort_chars(self):
        data = ['z', '2', ',', ' ', 'o']
        self.assertListEqual(sorted(data), quick_sort.sort(data))

    # Merge sorting tests

    def test_merge_sort(self):
        data = [29, 3, 92, 2, 4]
        self.assertListEqual(sorted(data), merge_sort.sort(data))

    def test_merge_sort_chars(self):
        data = ['a', ',', 'K']
        self.assertListEqual([',', 'K', 'a'], merge_sort.sort(data))

    # Counting sort tests

    def test_counting_sort(self):
        data = ['a', ',', 'K']
        self.assertListEqual([',', 'K', 'a'], counting_sort.sort(data))