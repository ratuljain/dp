__author__ = 'lol'
from collections import deque

board = {i: range(i + 1, i + 7) for i in range(1, 95)}

board[95] = [96, 97, 98, 99, 100]
board[96] = [97, 98, 99, 100]
board[97] = [98, 99, 100]
board[98] = [99, 100]
board[99] = [100]
board[100] = []
print board
# l = []
# s = []
#
#
# def replaceInt(l, v1, v2):
#     for n, i in enumerate(l):
#         if i == v1:
#             l[n] = v2
#     return l
#
# def addLadders(t, board):
#     if t[0] > 7:
#         r = t[0] - 6
#     else:
#         r = 1
#     for i in range(r, r + 6):
#         replaceInt(board[i], t[0], t[1])
#
# for i in l:
#     addLadders(i, board)
# for i in s:
#     addLadders(i, board)

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

print shortDist(board, 1, 100)
