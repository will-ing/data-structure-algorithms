

class Node():

    def __init__(self, data=None, _next=None):
        """
        Node class
        """
        self.data = data
        self._next = _next

    def __repr__(self):
        return f'{self.data} -> {self._next}'


class Graph():
    """
    Graph Class
    """

    def __init__(self):
        pass

    def add_node(self, val):
        """
        Adds a node to the graph
        """
        pass

    def add_edge(self, edge):
        """
        Adds a new edge between two nodes in the graph
        """
        pass

    def get_nodes(self):
        """
        Returns all of the nodes in the graph as a collection
        """
        pass

    def get_neighbors(self, node):
        """
        Returns a collection of edges connected to the given node
        """
        pass

    def size(self):
        """
        Returns the total number of nodes in the graph
        """
        pass
