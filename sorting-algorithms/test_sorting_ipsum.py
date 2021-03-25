from unittest import TestCase
from src import quick_sort, bubble_sort, merge_sort, counting_sort


class Test(TestCase):

    def setUp(self):
        f = open('src/lorem_ipsum.txt')
        self.data = [ch for ch in f.read()]
        self.sorted_data = sorted(self.data)
        f.close()

    def test_quick_sort(self):
        self.assertListEqual(self.sorted_data, quick_sort.sort(self.data))

    def test_quick_lim_chars(self):
        self.assertListEqual(sorted(self.data[0:2000]), quick_sort.sort(self.data[0:2000]))

    def test_bubble_sort(self):
        self.assertListEqual(self.sorted_data, bubble_sort.sort(self.data))

    def test_merge_sort(self):
        self.assertListEqual(self.sorted_data, merge_sort.sort(self.data))

    def test_counting_sort(self):
        self.assertListEqual(self.sorted_data, counting_sort.sort(self.data))
