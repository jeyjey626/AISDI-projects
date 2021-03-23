from unittest import TestCase
from src import bubble


class Test(TestCase):
    def test_bubble_sort(self):
        data = ['o', 'z', 'f']
        self.assertListEqual(['f', 'o', 'z'], bubble.bubble_sort(data))
