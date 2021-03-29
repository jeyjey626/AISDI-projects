"""
Merge sort algorithm
"""
import sys


def merge(list_to_sort, start_idx, mid_idx, end_idx):
        L = list_to_sort[start_idx:mid_idx+1]   # Left array to merge
        R = list_to_sort[mid_idx+1:end_idx+1]   # Right array to merge

        i = 0
        j = 0
        k = start_idx
        while i < len(L) and j < len(R):    # sort elements in left and right array till one is empty
            if L[i] < R[j]:
                list_to_sort[k] = L[i]
                i += 1
            else:
                list_to_sort[k] = R[j]
                j += 1
            k += 1

        while i < len(L):                   # if left wasn't empty add remaining elements to list_to_sort
            list_to_sort[k] = L[i]
            i += 1
            k += 1

        while j < len(R):                   # if right wasn't empty add remaining elements to list_to_sort
            list_to_sort[k] = R[j]
            j += 1
            k += 1


def merge_sort(list_to_sort, start_idx,  end_idx):
    if start_idx != end_idx: #sort till true
    
        # dividing the list_to_sort into halves
        mid_idx = start_idx + (end_idx - start_idx) // 2  # find middle index
        merge_sort(list_to_sort, start_idx, mid_idx)      # sort firt half
        merge_sort(list_to_sort, mid_idx+1, end_idx)      # sort second half

        # merging arrays into sorted list_to_sort
        merge(list_to_sort, start_idx, mid_idx, end_idx)   
    return list_to_sort


def sort(array):
    list_to_sort = array.copy()
    return merge_sort(list_to_sort, 0, len(array)-1)


if __name__ == '__main__':
    str_line = [i for i in open(sys.argv[1]).read()]
    sort_line = sort(str_line)
