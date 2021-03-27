import timeit

import matplotlib.pyplot as plt

import bubble_sort
import merge_sort
import quick_sort
import counting_sort

update_number = 0


def plot(name, x, y, file_name):
    plt.plot(x, y)
    plt.title(name)
    plt.ylabel('Czas pracy algorytmu [s]')
    plt.xlabel('Liczba sortowanych znaków')
    plt.savefig('png-files/' + file_name + '.png')
    plt.clf()


def update_user():
    global update_number
    update_number += 1
    print('Ukończono ' + str(update_number) + ' z 4 pomiarów')


def measure_and_plot(array, function, title, file_name):
    x = []
    y = []
    for i in range(1000, len(array) - 1, 500):  # todo smaller steps?
        array_to_sort = array[0:i]
        t = timeit.Timer(lambda: function.sort(array_to_sort))
        x.append(i)
        y.append(t.timeit(1))  # todo increment repeat times after done testng
    plot(title, x, y, file_name)


if __name__ == '__main__':
    f = open('lorem_ipsum.txt')
    data = [ch for ch in f.read()]
    f.close()
    measure_and_plot(data, quick_sort, 'Sortowanie szybkie', 'quick_sort')
    update_user()
    measure_and_plot(data, merge_sort, 'Sortowanie przez scalanie', 'merge_sort')
    update_user()
    measure_and_plot(data, bubble_sort, 'Sortowanie bąbelkowe', 'bubble_sort')
    update_user()
    measure_and_plot(data, counting_sort, 'Sortowanie przez zliczanie', 'counting_sort')
    update_user()
    print('Pomiar zakończony, wykresy zapisane w folderze png-files')
