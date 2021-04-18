import timeit
import numpy as np
import matplotlib.pyplot as plt
import AVL
import BST
import generate_tree

update_number = 0


def plot(x, y):
    plt.plot(x, y)
    plt.ylabel('Średni czas pracy pracy algorytmu [s]')
    plt.xlabel('Liczba elementów')
    plt.grid()


def save_fig(title, file_name):
    plt.title(title)
    plt.gca().legend(('AVL', 'BST'))
    plt.savefig('png-files/' + file_name + '.png')
    plt.clf()


def update_user():
    global update_number
    update_number += 1
    print('Ukończono ' + str(update_number) + ' z 6 pomiarów')


def measure_create(array, function):
    x = []
    y = []

    for i in range(1000, len(array) - 1, 300):
        elements_to_insert = array[0:i]
        x.append(i)
        t = timeit.Timer(lambda: function.create_tree(elements_to_insert))
        y.append(t.timeit(10)/10)
    plot(x, y)
    update_user()


def measure_search(array, function):
    x = []
    y = []
    root = function.create_tree(array)
    for i in range(1000, len(array) - 1, 300):
        elements_to_search = array[0:i]
        x.append(i)
        t = timeit.Timer(lambda: function.search_tree(root, elements_to_search))
        y.append(t.timeit(10)/10)
    plot(x, y)
    update_user()


def measure_delete(array, function):
    x = []
    y = []
    root = function.create_tree(array)
    for i in range(1000, len(array) - 1, 300):
        elements_to_delete = array[0:i]
        x.append(i)
        t = timeit.Timer(lambda: function.delete_tree(root, elements_to_delete))
        y.append(t.timeit(10) / 10)
    plot(x, y)
    update_user()


if __name__ == '__main__':
    data = [np.random.randint(0, 30000) for i in range(10000)]
    measure_create(data, AVL)
    measure_create(data, BST)
    save_fig('Tworzenie drzewa', 'creating_measurements')
    measure_search(data, AVL)
    measure_search(data, BST)
    save_fig('Wyszukiwanie w drzewie', 'searching_measurements')
    measure_delete(data, AVL)
    measure_delete(data, BST)
    save_fig('Usuwanie z drzewa', 'deleting_measurements')

    print('Pomiar zakończony, wykresy zapisane w folderze png-files')
