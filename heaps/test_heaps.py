import unittest
from src import n_heap


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.array = [4, 3, 6, 8, 11, 1, 5, 14, 10, 7, 2, 12, 9, 13, 15]

    def test_heap_properties(self):
        heap = n_heap.NHeap(2)
        for i in self.array:
            heap.insert(i)
        # Testing if all elements were inserted
        self.assertCountEqual(self.array, heap.heap_list)

    def test_heap_delete_min_bin(self):
        heap = n_heap.NHeap(2)
        for i in self.array:
            heap.insert(i)
        heap.delete_min()
        b = self.array
        b.pop(5)
        self.assertCountEqual(b, heap.heap_list)

    def test_heap_delete_min_trip(self):
        heap = n_heap.NHeap(3)
        for i in self.array:
            heap.insert(i)
        heap.delete_min()
        b = self.array
        b.pop(5)
        self.assertCountEqual(b, heap.heap_list)

    def test_heap_delete_min_quad(self):
        heap = n_heap.NHeap(4)
        for i in self.array:
            heap.insert(i)
        heap.delete_min()
        b = self.array
        b.pop(5)
        self.assertCountEqual(b, heap.heap_list)


if __name__ == '__main__':
    unittest.main()
