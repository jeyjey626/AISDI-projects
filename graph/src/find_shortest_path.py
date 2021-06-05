import sys
import numpy as np
from dijkstra import Graph, dijkstra, shortest


def load_board(filename):
    file = open(filename)
    Lines = file.readlines()
    data = []
    for line in Lines:
        tmp = []
        for char in line:
            if char is not '\n':
                tmp.append(int(char))
        data.append(tmp)
    data = np.array(data)
    up_low = -1 * np.ones(data.shape[1]).astype(int)
    right_left = -1 * np.ones(data.shape[0]+2).reshape(-1, 1).astype(int)
    data = np.vstack((up_low, data, up_low))
    data = np.hstack((right_left, data, right_left))
    return data


def prepare_graph(data):
    g = Graph()
    start = ()
    end = ()
    for row in range(1, data.shape[0]-1):
        for col in range(1, data.shape[1]-1):
            g.add_edge((row, col), (row, col+1), data[row, col+1])
            g.add_edge((row, col), (row+1, col), data[row+1, col])
            if data[row, col] == 0:
                if not start:
                    start = (row, col)
                else:
                    end = (row, col)

    return g, start, end


def save_shortest_path(filename, data, path):
    board = np.array([[" " for col in range(data.shape[1]-2)]for row in range(data.shape[0]-2)])
    for i in path:
        board[i[0]-1, i[1]-1] = data[i]
    file = open(filename, 'a')
    file.write("\n The shortest path from 0 to 0 for upper board is \n")
    for i in range(board.shape[0]):
        string = ''
        for j in range(board.shape[1]):
            string += board[i, j]
        string += '\n'
        print(string)
        file.write(string)
    file.close()


if __name__ == '__main__':
    filename = sys.argv[1]
    data = load_board(filename)
    g, start, end = prepare_graph(data)
    dijkstra(g, g.get_vertex(start))
    target = g.get_vertex(end)
    path = [target.get_id()]
    shortest(target, path)
    save_shortest_path(filename, data, path)