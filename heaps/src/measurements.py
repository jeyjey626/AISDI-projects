import numpy as np
import timeit
import n_heap
import matplotlib.pyplot as plt

update_number = 0


def plot(x, y):
    plt.plot(x, y)
    plt.ylabel('Średni czas pracy pracy [s]')
    plt.xlabel('Liczba elementów')
    plt.grid()


def save_fig(title, file_name):
    plt.title(title)
    plt.gca().legend(('kopiec 2-arny', 'kopiec 3-arny', 'kopiec 4-arny'))
    plt.savefig('png-files/' + file_name + '.png')
    plt.clf()


def update_user():
    global update_number
    update_number += 1
    print('Ukończono ' + str(update_number) + ' z 6 pomiarów')


def measure_insert(n, start_array):
    x = []
    y = []

    for i in range(10000, len(start_array), 10000):
        elements_to_insert = start_array[0:i]
        x.append(i)
        heap = n_heap.NHeap(n)
        t = timeit.Timer(lambda: heap.insert_elements(elements_to_insert))
        y.append(t.timeit(10)/10)
    plot(x, y)
    update_user()


def measure_delete(n, start_array):
    x = []
    y = []

    for i in range(10000, len(start_array), 10000):
        heap = n_heap.NHeap(n)
        heap.insert_elements(start_array)
        x.append(i)
        t = timeit.Timer(lambda: heap.delete_elements(i))
        y.append(t.timeit(10)/10)
    plot(x, y)
    update_user()


if __name__ == '__main__':
    data = [np.random.randint(1, 300000) for i in range(100000)]
    for i in range(2, 5):
        measure_insert(i, data)
    save_fig('Wstawianie elementów do kopca', 'insert_measurements')
    for i in range(2, 5):
        measure_delete(i, data)
    save_fig('Usuwanie szczytu kopca', 'delete_measurements')
