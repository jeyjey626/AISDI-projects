import heapq


class Vertex:
    def __init__(self, node):
        self.id = node
        self.neighbours_dict = {}
        # Big distance for all nodes
        self.distance = 10000
        # All nodes set to unvisited
        self.visited = False
        self.previous = None

    def add_neighbour(self, neighbour, weight=0):
        self.neighbours_dict[neighbour] = weight

    def get_connections(self):
        return self.neighbours_dict.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbour):
        return self.neighbours_dict[neighbour]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + 'neighbour: ' + str([x.id for x in self.neighbours_dict])

    def __lt__(self, other):
        return self.distance < other.distance


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):

        if node in self.vert_dict:
            return self.vert_dict[node]
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, start, end, cost=0):
        if cost < 0:
            return
        if start not in self.vert_dict:
            self.add_vertex(start)
        if end not in self.vert_dict:
            self.add_vertex(end)

        self.vert_dict[start].add_neighbour(self.vert_dict[end], cost)
        self.vert_dict[end].add_neighbour(self.vert_dict[start], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self):
        return self.previous


def shortest(v, path):
    # make shortest path from v.previous
    if v.previous:
        path.append(v.previous.get_id)
        shortest(v.previous, path)
    return


def dijkstra(graph, start):
    # set start node distance to 0
    start.set_distance = 0
    print(start)
    unvisited_queue = [(v.get_distance(), v) for v in graph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # pop vertex with smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        for next in current.neighbours_dict:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print('updated : current = %s next = %s new_dist = %s' \
                % (current.get_id(), next.get_id(), next.get_distance()))
            else:
                print('not updated : current = %s next = %s new_dist = %s' \
                % (current.get_id(), next.get_id(), next.get_distance()))

        # rebuild heap
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.get_distance(), v) for v in graph if not v.visited]
        heapq.heapify(unvisited_queue)


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    print('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    dijkstra(g, g.get_vertex('a'))

    target = g.get_vertex('e')
    path = [target.get_id()]
    shortest(target, path)
    print('The shortest path : %s' %(path[::-1]))