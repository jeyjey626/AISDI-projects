from unittest import TestCase
from src import bubble
from src import merge_sort

class Test(TestCase):
    def test_bubble_sort(self):
        data = ['o', 'z', 'f']
        self.assertListEqual(['f', 'o', 'z'], bubble.bubble_sort(data))


    def test_merge_sort(self):
        data = ['a', ',', 'K']
        self.assertListEqual([',', 'K', 'a'], merge_sort.merge_sort(data, 0, len(data)))
