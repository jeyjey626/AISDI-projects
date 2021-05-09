# N-ary heap class

class NHeap:
    def __init__(self, n):
        self.heap_list = []
        self.n = n

    def _go_up(self, index):
        if index == 0:
            return
        parent = self._get_parent_index(index)
        if self.heap_list[parent] < self.heap_list[index]:
            return
        self.heap_list[index],  self.heap_list[parent] = self.heap_list[parent],  self.heap_list[index]
        self._go_up(parent)

    def _get_parent_index(self, child_index):
        return (child_index - 1) // self.n

    def _heapify(self, index, size):
        children = self.get_children(index)
        if not children:
            return
        min_child_index = children.index(min(children))
        # get actual index of min child
        min_child_index = (self.n * index) + (min_child_index + 1)
        if self.heap_list[min_child_index] < self.heap_list[index]:
            self.heap_list[index], self.heap_list[min_child_index] = self.heap_list[min_child_index], self.heap_list[index]
            if min_child_index <= size // self.n:
                self._heapify(min_child_index, size)

    def get_children(self, index):
        children = []
        for i in range(self.n):
            child_index = (index * self.n) + i + 1
            if child_index < self.curr_size():
                children.append(self.heap_list[child_index])
            else:
                break
        return children

    def curr_size(self):
        return len(self.heap_list)

    def insert(self, value):
        self.heap_list.append(value)
        self._go_up(self.curr_size()-1)

    def delete_min(self):
        if self.curr_size() == 1:
            return []
        self.heap_list[0], self.heap_list[self.curr_size()-1] = self.heap_list[self.curr_size()-1], self.heap_list[0]
        root = self.heap_list.pop()
        self._heapify(0, self.curr_size())
        return root

    def heapify(self):
        for index in reversed(range(self._get_parent_index(self.curr_size() - 1) + 1)):
            self._heapify(index, self.curr_size())

    def insert_elements(self, array):
        for element in array:
            self.insert(element)

    def delete_elements(self, count):
        for e in range(count):
            self.delete_min()


if __name__ == '__main__':
    bin_heap = NHeap(4)
    for i in range(10):
        bin_heap.insert(i)
    print(bin_heap.delete_min())
    print(bin_heap.heap_list)




