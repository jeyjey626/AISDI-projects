# Bubble sorting algorithm
import sys


def bubble_sort(sort_array):

    swap_occurred = True  # algorithm should finish when no swap was made

    while swap_occurred:
        swap_occurred = False  # new iteration, reset swap flag
        for i in range(len(sort_array) - 1):  # 1 less than elements because we are always checking a i, i+1 pair
            if sort_array[i] > sort_array[i+1]:
                # Swap elements and flag swap
                sort_array[i], sort_array[i+1] = sort_array[i+1], sort_array[i]
                swap_occurred = True

    return sort_array


if __name__ == '__main__':
    sort_array = [ch for ch in open(sys.argv[1]).read()]
    sort_array = bubble_sort(sort_array)
