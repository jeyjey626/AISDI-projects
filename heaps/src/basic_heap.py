# Heap class
from abc import abstractmethod


class Heap:
    def __init__(self):
        self.heap_list = []

    def curr_size(self):
        return len(self.heap_list)

    def insert(self, value):
        self.heap_list.append(value)
        self._go_up(self.curr_size()-1)

    def delete_min(self):
        self.heap_list[0], self.heap_list[self.curr_size()-1] = self.heap_list[self.curr_size()-1], self.heap_list[0]
        root = self.heap_list.pop()
        self._heapify(0, self.curr_size())
        return root

    def heapify(self):
        for index in reversed(range(self._get_parent_index(self.curr_size() - 1) + 1)):
            self._heapify(index, self.curr_size())

    def _go_up(self, index):
        if index == 0:
            return
        parent = self._get_parent_index(index)
        if self.heap_list[parent] < self.heap_list[index]:
            return
        self.heap_list[index],  self.heap_list[parent] = self.heap_list[parent],  self.heap_list[index]
        self._go_up(parent)

    @abstractmethod
    def _get_parent_index(self, child_index):
        pass

    @abstractmethod
    def _heapify(self, index, size):
        pass



