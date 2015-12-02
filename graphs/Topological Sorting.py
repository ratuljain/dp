from collections import deque
g = {'A': ['C'],
     'B': ['C', 'D'],
     'C': ['E'],
     'D': ['F'],
     'E': ['H', 'F'],
     'F': ['G'],
     'G': [],
     'H': []
     }

graph_tasks = { "wash the dishes" : ["have lunch"],
                "cook food" : ["have lunch"],
                "have lunch" : [],
                "wash laundry" : ["dry laundry"],
                "dry laundry" : ["fold laundry"],
                "fold laundry" : [] }

graph4 = { 0 : [1],
           1 : [2],
           2 : [3],
           3 : [4],
           4 : []
           }


def inDegree(graph):
    degree = {i : 0 for i in graph}
    for vertex in graph:
        for vertices in graph[vertex]:
            degree[vertices] += 1
    return degree

# print inDegree(graph_tasks)

def kahn_topsort(graph):
    queue = deque()
    l = []
    in_degree = inDegree(graph)

    for vertex in in_degree:
        if in_degree[vertex] == 0:
            queue.appendleft(vertex)

    while queue:
        vertex = queue.pop()
        l.append(vertex)
        for v in graph[vertex]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.appendleft(v)

    if len(l) == len(graph):
        return l
    else:
        return []


def dfs_topsort(graph):         # recursive dfs with
    color = { u : "white" for u in graph }
    L = []
    found_cycle = [False]
    for u in graph:
        if color[u] == 'white':
            dfs_visit(graph, u, color, L, found_cycle)
        if found_cycle[0]:
            return []
    return L[::-1]

def dfs_visit(graph, u, color, L, found_cycle):

    color[u] = 'gray'
    for v in graph[u]:
        if color[v] == 'gray':
            found_cycle[0] = True
            return
        if color[v] == 'white':
            dfs_visit(graph, v, color, L, found_cycle)
    color[u] = 'black'
    L.append(u)

order = dfs_topsort(g)
print order
