from src import KMP_algorithm
from src import naive_algorithm
from src import RK_algorithm
import re
import timeit
import matplotlib.pyplot as plt

update_number = 0


def plot(x, y):
    plt.plot(x, y)
    plt.ylabel('Średni czas pracy algorytmu [s]')
    plt.xlabel('Liczba wyszukiwanych słów')
    plt.grid()


def save_fig(title, file_name):
    plt.title(title)
    plt.gca().legend(('Algorytm KMP', 'Algorytm KR', 'Algorytm naiwny'))
    plt.savefig('png-files/' + file_name + '.png')
    plt.clf()


def update_user():
    global update_number
    update_number += 1
    print('Ukończono ' + str(update_number) + ' z 3 pomiarów')


def search_words(function, text, words):
    for word in words:
        function.find(word, text)


def measure_search(function, text):
    x = []
    y = []
    list_of_words = re.sub(r'[^\w\s]', '',  text).split()  # removing punctuation and splitting words

    for i in range(100, 1100, 100):
        print(i)
        x.append(i)
        words_to_search = list_of_words[:i]
        t = timeit.Timer(lambda: search_words(function, text, words_to_search))
        y.append(t.timeit(1))
    plot(x, y)
    update_user()


if __name__ == '__main__':
    print('Rozpoczęto pomiary')
    search_in = open('pan-tadeusz.txt', encoding='utf-8').read()
    measure_search(KMP_algorithm, search_in)
    measure_search(RK_algorithm, search_in)
    measure_search(naive_algorithm, search_in)
    save_fig('Wyszukiwanie słów w tekście', 'measure_search')
    print('Zakończono pomiary, wyniki znajdują się w folderze png-files')
