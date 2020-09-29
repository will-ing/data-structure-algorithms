

class Node:

    def __init__(self, data=None):
        """
        Node class
        """
        self.data = data

    def __repr__(self):
        return f'{self.data}'


class Edge:

    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight


class Graph:
    """
    Graph Class
    """

    def __init__(self):
        self.adjacency = {}

    def add_node(self, val):
        """
        Adds a node to the graph
        """
        new_node = Node(val)
        self.adjacency[new_node] = []

    def add_edge(self, a, b, weight=0):
        """
        Adds a new edge between two nodes in the graph
        """
        if a not in self.adjacency:
            raise KeyError('Not in list')
        if b not in self.adjacency:
            raise KeyError('Not in list')
        edge = Edge(b, weight)

        self.adjacency[a].append(edge)

    def get_nodes(self):
        """
        Returns all of the nodes in the graph as a collection
        """
        return self.adjacency.keys()

    def get_neighbors(self, node):
        """
        Returns a collection of edges connected to the given node
        """
        return self.adjacency.get(node, [])

    def size(self):
        """
        Returns the total number of nodes in the graph
        """
        return len(self.adjacency)

    def breadth(self):
        from challenges.stack_and_queues.stack_and_queues import Queue
        queue = Queue()
        node_list = set()
        node_name = ""

        queue.enqueue(self.adjacency)
        node_name += self.adjacency[0].data

        while not queue.is_empty():
            front = queue.dequeue()
            node_list.add(front)

            #  get the edges of the current vector
            neighbors = self.get_neighbors(front)
            for edge in neighbors:
                if not edge.vertex in node_list:
                    node_list.add(edge.vertex)
                    node_name += edge.vertex.data
                    queue.enqueue(edge.vertex)

        return node_name
