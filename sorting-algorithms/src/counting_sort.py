"""
Counting sort algorithm
Counting table contain ASCII from 10 to 122
"""
import sys

min_ascii = 10      # "\n"
max_ascii = 122     # "z"


def sort(list_to_sort):
    sorted_list = []
    count_list = [0 for i in range(max_ascii-min_ascii+1)]

    for i in range(len(list_to_sort)):
        count_list[ord(list_to_sort[i])-min_ascii] += 1

    for i in range(len(count_list)):
        while count_list[i] > 0:
            sorted_list.append(chr(i+min_ascii))
            count_list[i] -= 1

    return sorted_list


if __name__ == '__main__':
    str_line = [i for i in open(sys.argv[1]).read()]
    sort_line = sort(str_line)


