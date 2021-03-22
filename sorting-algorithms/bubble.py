# Bubble sorting algorithm
import sys


def bubble_sort(list_to_sort):

    swap_occurred = True  # algorithm should finish when no swap was made

    while swap_occurred:
        swap_occurred = False  # new iteration, reset swap flag
        for i in range(len(list_to_sort) - 1):  # 1 less than elements because we are always checking a i, i+1 pair
            if list_to_sort[i] > list_to_sort[i+1]:
                # Swap elements and flag swap
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
                swap_occurred = True

    return list_to_sort


if __name__ == '__main__':
    character_list = [ch for ch in open(sys.argv[1]).read()]
    # word_list = open(sys.argv[1]).read().split() or with re.split if sorting words
    bubble_sort(character_list)
