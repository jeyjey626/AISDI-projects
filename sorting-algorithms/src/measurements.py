import bubble_sort, merge_sort, quick_sort
import timeit
import matplotlib.pyplot as plt
# todo add setup to install automatically with pip ?


def plot(name, x, y):
    plt.plot(x, y)
    plt.title(name)
    plt.ylabel('Czas pracy algorytmu [s]')
    plt.xlabel('Liczba sortowanych znaków')
    plt.show()
    # todo save plot as file


def measure_and_plot(array, function, title):
    x = []
    y = []
    for i in range(1000, 6000, 1000):  # todo smaller steps?
        array_to_sort = array[0:i]
        t = timeit.Timer(lambda: function.sort(array_to_sort))
        x.append(i)
        y.append(t.timeit(10))  # todo increment repeat times after done testng
    plot(title, x, y)


if __name__ == '__main__':
    f = open('lorem_ipsum.txt')
    data = [ch for ch in f.read()]
    f.close()
    measure_and_plot(data, bubble_sort, 'Sortowanie bąbelkowe')
    measure_and_plot(data, merge_sort, 'Sortowanie przez scalanie')
    # measure_and_plot(data, quick_sort, 'Sortowanie szybkie')
    # todo solve exceeded comparison dept - works in tests tho ? ? ?
