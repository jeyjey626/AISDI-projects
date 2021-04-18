import timeit
import numpy as np
import matplotlib.pyplot as plt
import AVL
import BST

update_number = 0


def plot(name, x, y, file_name):
    plt.plot(x, y)
    plt.title(name)
    plt.ylabel('Średni czas pracy pracy algorytmu [s]')
    plt.xlabel('Liczba elementów')
    plt.grid()
    plt.savefig('src/png-files/' + file_name + '.png')
    plt.clf()


def update_user():
    global update_number
    update_number += 1
    print('Ukończono ' + str(update_number) + ' z 6 pomiarów')


def measure_create(array, function, title, file_name):
    x = []
    y = []

    for i in range(1000, len(array) - 1, 300):
        elements_to_insert = array[0:i]
        x.append(i)
        t = timeit.Timer(lambda: function.create_tree(elements_to_insert))
        y.append(t.timeit(10)/10)
    plot(title, x, y, file_name)
    update_user()


def measure_search(array, function, title, file_name):
    x = []
    y = []
    root = function.create_tree(array)
    for i in range(1000, len(array) - 1, 300):
        elements_to_search = array[0:i]
        x.append(i)
        t = timeit.Timer(lambda: function.search_tree(root, elements_to_search))
        y.append(t.timeit(10)/10)
    plot(title, x, y, file_name)
    update_user()


def measure_delete(array, function, title, file_name):
    x = []
    y = []
    root = function.create_tree(array)
    for i in range(1000, len(array) - 1, 300):
        elements_to_delete = array[0:i]
        x.append(i)
        t = timeit.Timer(lambda: function.delete_tree(root, elements_to_delete))
        y.append(t.timeit(10) / 10)
    plot(title, x, y, file_name)
    update_user()


if __name__ == '__main__':
    data = [np.random.randint(0, 30000) for i in range(10000)]
    measure_create(data, AVL, 'Tworzenie drzewa AVL', 'create_avl_tree')
    #measure_create(data, BST, 'Tworzenie drzewa BST', 'create_bst_tree')
    measure_search(data, AVL, 'Wyszukiwanie w drzewie AVL', 'search_avl_tree')
    #measure_search(data, BST, 'Wyszukiwanie w drzewie BST', 'search_bst_tree')
    measure_delete(data, AVL, 'Usuwanie z drzewa AVL', 'del_avl_tree')
    #measure_delete(data, BST, 'Usuwanie z drzewa BST', 'del_bst_tree')

    print('Pomiar zakończony, wykresy zapisane w folderze png-files')
