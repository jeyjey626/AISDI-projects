# Binary Heap
from basic_heap import Heap


class BinaryHeap(Heap):
    def __init__(self):
        super().__init__()

    def _get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def _heapify(self, index, size):
        children = self.get_children(index)
        if not children:
            return
        min_child_index = children.index(min(children))
        # get actual index of min child
        min_child_index = (2 * index) + (min_child_index + 1)
        if self.heap_list[min_child_index] < self.heap_list[index]:
            self.heap_list[index], self.heap_list[min_child_index] = self.heap_list[min_child_index], self.heap_list[index]
            if min_child_index <= size // 2:
                self._heapify(min_child_index, size)

    def get_children(self, index):
        children = []
        for i in range(2):
            child_index = (index * 2) + i + 1
            if child_index < self.curr_size():
                children.append(self.heap_list[child_index])
            else:
                break
        return children


if __name__ == '__main__':
    bin_heap = BinaryHeap()
    for i in range(10):
        bin_heap.insert(i)
    print(bin_heap.delete_min())
    print(bin_heap.heap_list)
