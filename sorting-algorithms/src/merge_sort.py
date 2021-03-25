"""
Merge sort algorithm
"""
import sys


def merge(list_to_sort, start_idx, mid_idx, end_idx):
        L = list_to_sort[start_idx:mid_idx+1]
        R = list_to_sort[mid_idx+1:end_idx+1]

        i = 0
        j = 0
        k = start_idx
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list_to_sort[k] = L[i]
                i += 1
            else:
                list_to_sort[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            list_to_sort[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            list_to_sort[k] = R[j]
            j += 1
            k += 1


def merge_sort(list_to_sort, start_idx,  end_idx):
    if start_idx != end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        merge_sort(list_to_sort, start_idx, mid_idx)
        merge_sort(list_to_sort, mid_idx+1, end_idx)
        merge(list_to_sort, start_idx, mid_idx, end_idx)
    return list_to_sort


def sort(array):
    return merge_sort(array, 0, len(array)-1)


if __name__ == '__main__':
    str_line = [i for i in open(sys.argv[1]).read()]
    sort_line = sort(str_line)
