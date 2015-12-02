from collections import deque

g = {'A': ['B', 'D', 'G'],
     'B': ['A', 'E', 'F'],
     'C': ['F', 'H'],
     'D': ['A', 'F'],
     'E': ['B', 'G'],
     'F': ['B', 'C', 'D'],
     'G': ['A', 'E'],
     'H': ['C']
     }
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
graph2 = { 0 : [],
           1 : [2],
           2 : [],
           3 : [4],
           4 : [5],
           5 : [3] }
def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
        l = [x for x in graph[vertex] if x not in visited]
        stack.extend(l[::-1])
    return visited

print dfs(g, 'A')

# def dfs_paths(graph, start, goal):
#     res = []
#     stack = [(start, [start])]
#     while stack:
#         (vertex, path) = stack.pop()
#         l = graph[vertex] - set(path)
#         for next in graph[vertex] - set(path):
#             if next == goal:
#                 res.append(path + [next])
#             else:
#                 stack.append((next, path + [next]))
#     return res
# def cycle_exists(G):                     # - G is a directed graph
#     color = { u : "white" for u in G  }  # - All nodes are initially white
#     found_cycle = [False]                # - Define found_cycle as a list so we can change
#                                          # its value per reference, see:
#                                          # http://stackoverflow.com/questions/11222440/python-variable-reference-assignment
#     for u in G:                          # - Visit all nodes.
#         if color[u] == "white":
#             dfs_visit(G, u, color, found_cycle)
#         if found_cycle[0]:
#             break
#     return found_cycle[0]
#
# #-------
#
# def dfs_visit(G, u, color, found_cycle):
#     if found_cycle[0]:                          # - Stop dfs if cycle is found.
#         return
#     color[u] = "gray"                           # - Gray nodes are in the current path
#     for v in G[u]:                              # - Check neighbors, where G[u] is the adjacency list of u.
#         if color[v] == "gray":                  # - Case where a loop in the current path is present.
#             found_cycle[0] = True
#             return
#         if color[v] == "white":                 # - Call dfs_visit recursively.
#             dfs_visit(G, v, color, found_cycle)
#     color[u] = "black"                          # - Mark node as done.
#
#
# print(dfs(cycle_exists(graph2)))
# # print (dfs_paths(graph2, 1,2))
#
#
# # print [i for i in paths(g, 'A', 'H')]
def shortDist(graph, start, goal):
    visited = []
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()
        if node == goal:
            return dist
        visited.append(node)
        for vertex in [i for i in graph[node] if i not in visited]:
            queue.append((vertex, dist + 1))
    return None

print shortDist(g, 'A', 'H')