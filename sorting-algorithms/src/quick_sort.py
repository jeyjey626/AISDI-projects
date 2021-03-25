# Quick Sort

# Function that partitions given list and sorts smaller elements to the left, bigger to the right of pivot point
import sys
import random


def divide(array, start, end):
    pivot_id = random.randint(start, end)  # randomizing pivot point
    array[pivot_id], array[end] = array[end], array[pivot_id]
    pivot = array[end]
    i = (start - 1)  # last smaller element index

    for j in range(start, end):

        if array[j] <= pivot:
            # increment index (and count at the same time) of smaller elements
            i = i + 1
            # swap elements array[i] and array [j], moving all smaller elements to the left
            # index i keeps track of where the last found smaller element is
            array[i], array[j] = array[j], array[i]

    # since i kept track of the last smaller element index, we know where our pivot should be -> i+1
    array[i+1], array[end] = array[end], array[i+1]
    return i + 1


# Quick sort algorithm
def quick_sort(array, start, end):
    if start >= end:
        return array  # finish sorting

    # divide_index marks the index of correctly placed element with divide()
    divide_index = divide(array, start, end)

    # Sort elements before and after the placed element
    quick_sort(array, start, divide_index-1)
    quick_sort(array, divide_index+1, end)

    return array


def sort(array):
    return quick_sort(array, 0, len(array)-1)


if __name__ == '__main__':
    sort_array = [ch for ch in open(sys.argv[1]).read()]
    sort_array = quick_sort(sort_array, 0, len(sort_array)-1)
