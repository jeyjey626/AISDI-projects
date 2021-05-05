# Heap class
from abc import abstractmethod


class Heap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def delete_min(self):
        pass

    @abstractmethod
    def heapify_up(self):
        pass

    @abstractmethod
    def heapify_down(self):
        pass




