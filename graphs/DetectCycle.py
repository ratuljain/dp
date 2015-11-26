def dfs(graph, start):
    color = {i : 'white' for i in graph}
    stack = [start]
    visited = []

    while stack:
        vertex = stack.pop()
        if color[vertex] == 'grey':
            return True
            break
        color[vertex] = 'grey'
        visited.append(vertex)
        stack.extend((graph[vertex]))
        if  len(graph[vertex]) == 0:
            color[vertex] = 'black'
    return False

def cycle_exists(graph):
    for vertex in graph:
         if(dfs(graph, vertex)):
             return True
    return False


#
# # connected graph with cycle
# graph1 = { 0 : [1, 2],
#            1 : [],
#            2 : [3],
#            3 : [4],
#            4 : [2] }
# assert(cycle_exists(graph1) == True)
# print("Graph1 has a cycle.")
#
# #----------------------------------------------------
#
# # disconnected graph with cycle
# graph2 = { 0 : [],
#            1 : [2],
#            2 : [],
#            3 : [4],
#            4 : [5],
#            5 : [3] }
# assert(cycle_exists(graph2) == True)
# print("Graph2 has a cycle.")
#
# #----------------------------------------------------
#
# # disconnected graph without a cycle
# graph3 = { 0 : [],
#            1 : [],
#            2 : [],
#            3 : [] }
# assert(cycle_exists(graph3) == False)
# print("Graph3 has no cycle.")
#
# #----------------------------------------------------
#
# # disconnected graph without a cycle
# graph4 = { 0 : [1, 2],
#            1 : [3, 4],
#            2 : [],
#            3 : [],
#            4 : [],
#            5 : [6, 7],
#            6 : [],
#            7 : [] }
# assert(cycle_exists(graph4) == False)
# print("Graph4 has no cycle.")
#
# #----------------------------------------------------
#
# # If assert raises an error, then a test case was not passed.
# print("\nAlgorithm passed all test cases")


graph3 = { 0 : [1, 2],
           1 : [0],
           2 : [0] }

assert(cycle_exists(graph3) == False)
print("Graph3 has no cycle.")