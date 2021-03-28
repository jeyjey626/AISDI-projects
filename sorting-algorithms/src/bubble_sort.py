# Bubble sorting algorithm
import sys


def sort(array):
    list_to_sort = array.copy()
    swap_occurred = True  # algorithm should finish when no swap was made

    while swap_occurred:
        swap_occurred = False  # new iteration, reset swap flag
        for i in range(len(list_to_sort) - 1):  # 1 less than elements because we are always checking a i, i+1 pair
            if list_to_sort[i] > list_to_sort[i + 1]:
                # Swap elements and flag swap
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swap_occurred = True
    return list_to_sort


if __name__ == '__main__':
    sort_array = [ch for ch in open(sys.argv[1]).read()]
    sort_array = sort(sort_array)
