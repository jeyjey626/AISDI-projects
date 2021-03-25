# Bubble sorting algorithm
import sys


def sort(array):

    swap_occurred = True  # algorithm should finish when no swap was made

    while swap_occurred:
        swap_occurred = False  # new iteration, reset swap flag
        for i in range(len(array) - 1):  # 1 less than elements because we are always checking a i, i+1 pair
            if array[i] > array[i + 1]:
                # Swap elements and flag swap
                array[i], array[i + 1] = array[i + 1], array[i]
                swap_occurred = True

    return array


if __name__ == '__main__':
    sort_array = [ch for ch in open(sys.argv[1]).read()]
    sort_array = sort(sort_array)
