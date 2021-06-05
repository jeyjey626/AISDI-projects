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
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


def dijkstra(graph, start):
    # set start node distance to 0
    start.set_distance(0)
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

        # rebuild heap
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.get_distance(), v) for v in graph if not v.visited]
        heapq.heapify(unvisited_queue)
