__author__ = 'lol'
class unionFind:
    def __init__(self, n):
        self.parent = range(len(n))
        self.aux = n
        self.rank = [0 for x in range(len(n))]

    def find(self, key):
        k = self.aux.index(key)
        def findutil(k):
            if k != self.parent[k]:
                self.parent[k] = findutil(self.parent[k])
            return self.parent[k]
        return findutil(k)


    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root < y_root:
            x_root, y_root = y_root, x_root
        if x_root == y_root:
            return
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] = self.rank[y_root] + 1

def kruskal(graph):
    uf = unionFind(graph['vertices'])

    mst = set()
    edges = list(graph['edges'])
    edges.sort()

    for edge in edges:
        weight, vertice1, vertice2 = edge
        if uf.find(vertice1) != uf.find(vertice2):
            uf.union(vertice1, vertice2)
            mst.add(edge)
    return mst



graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': [
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ]
        }

print kruskal(graph)


# x = ['A', 'B', 'C', 'D', 'E']
# uf = unionFind(x)
# uf.union('A', 'B')
# uf.union('B', 'C')
# uf.union('C', 'D')
# print uf.parent
#
# myDict = {}
# for node in x:
#     root = uf.find(node)
#     if not root in myDict:
#         myDict[root] = set([node])
#     else:
#         myDict[root].add(node)
# print("\nDisjoint sets: ")
# for mySet in myDict.values():
#     print(mySet)
