from unittest import TestCase
from src import quick_sort
from src import bubble_sort
from src import merge_sort


class Test(TestCase):

    def setUp(self):
        f = open('src/lorem_ipsum.txt')
        self.data = [ch for ch in f.read()]
        self.sorted_data = sorted(self.data)
        f.close()

    def test_quick_sort(self):
        self.assertListEqual(self.sorted_data, quick_sort.quick_sort(self.data, 0, len(self.data)-1))

    def test_bubble_sort(self):
        self.assertListEqual(self.sorted_data, bubble_sort.bubble_sort(self.data))

    def test_merge_sort(self):
        self.assertListEqual(self.sorted_data, merge_sort.merge_sort(self.data, 0, len(self.data)))
