# Enter your code here. Read input from STDIN. Print output to STDOUT
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
    return -1

def replaceInt(l, v1, v2):
    for n, i in enumerate(l):
        if i == v1:
            l[n] = v2
    return l

def addLadders(t, board):
    if t[0] > 7:
        r = t[0] - 6
    else:
        r = 1
    for i in xrange(r, r + 6):
        replaceInt(board[i], t[0], t[1])

from collections import deque

testcases = int(raw_input())

def lol():
    board = {i: range(i + 1, i + 7) for i in xrange(1, 95)}

    board[95] = [96, 97, 98, 99, 100]
    board[96] = [97, 98, 99, 100]
    board[97] = [98, 99, 100]
    board[98] = [99, 100]
    board[99] = [100]
    board[100] = []

    ladders = []
    snakes = []
    
    l = int(raw_input())
    for i in xrange(l):
        ladders.append(tuple([int(i) for i in raw_input().split(" ")]))
    
    s = int(raw_input())
    for i in xrange(s):
        snakes.append(tuple([int(i) for i in raw_input().split(" ")]))

    for i in ladders:
        addLadders(i, board)
    for i in snakes:
        addLadders(i, board)

    print shortDist(board, 1, 100)

for i in xrange(testcases):
    lol()
