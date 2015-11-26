__author__ = 'lol'
class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for x in range(n)]

    def find(self, v):
        if not v == self.parent[v]:
            return self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1

    def printParent(self):
        print("index: ",list(range(3)))
        print("parent: ", self.parent)

class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)

        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []

        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return [tuple(i) for i in edges]

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res




graph4 = { 0 : [1],
                  1 : [0, 2, 3, 5],    # edit: corrected from [0, 2] to [0, 2, 3, 5]
                  2 : [1],
                  3 : [1, 4],
                  4 : [3, 5],
                  5 : [1, 4] }

g = Graph(graph4)
edges = g.edges()
vertex = len(g.vertices())
uf = UnionFind(vertex)

for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    if uf.find(v1) == uf.find(v2):
        print "True"
        break
    uf.union(v1, v2)

# myDict = {}
# for node in range(vertex):
#     root = uf.find(node)
#     if not root in myDict:
#         myDict[root] = set([node])
#     else:
#         myDict[root].add(node)
# print("\nDisjoint sets: ")
# for mySet in myDict.values():
#     print(mySet)








