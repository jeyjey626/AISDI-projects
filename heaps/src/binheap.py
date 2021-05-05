# Binary Heap
from basic_heap import Heap


class BinaryHeap(Heap):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        self.heapList.append(value)
        self.currentSize += 1
        self.heapify_up(self.currentSize - 1)

    def delete_min(self):
        if len(self.heapList) == 0:
            return "Empty heap"

        root = self.heapList[0]
        self.heapList[0] = self.heapList[self.currentSize - 1]
        self.heapList.pop()
        self.currentSize -= 1

        self.heapify_down()

        return root

    def heapify_up(self, x):
        while x // 2 > 0:
            if self.heapList[x] < self.heapList[x // 2]:
                self.heapList[x], self.heapList[x // 2] = self.heapList[x // 2], self.heapList[x]
            x = x // 2

    def heapify_down(self):
        x = 0
        while x * 2 <= self.currentSize:
            min_child = self.min_child(x)
            if self.heapList[x] > self.heapList[min_child]:
                self.heapList[x], self.heapList[min_child] = self.heapList[min_child], self.heapList[x]

            x = min_child

    def min_child(self, x):
        if x * 2 + 1 > self.currentSize - 1:
            return x * 2
        else:
            if self.heapList[x * 2] < self.heapList[x * 2 + 1]:
                return x * 2
            else:
                return x * 2 + 1


if __name__ == '__main__':
    bin_heap = BinaryHeap()
    for i in range(10):
        bin_heap.insert(i)
    print(bin_heap.delete_min())
    print(bin_heap.heapList)
