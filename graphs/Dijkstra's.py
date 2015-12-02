__author__ = 'lol'


distances = {
     0: {1: 4, 7: 8},
     1: {0: 4, 2: 8, 7: 11},
     2: {8: 2, 1: 8, 3: 7, 5: 4},
     3: {2: 7, 4: 9, 5: 14},
     4: {3: 9, 5: 10},
     5: {2: 4, 4: 10, 6: 2},
     6: {8: 6, 3: 14, 5: 2, 7: 1},
     7: {0: 8, 1: 11, 6: 1, 8: 7},
     8: {2: 2, 6: 6, 7: 7}
    }
nodes = tuple(distances.keys())

unvisited = {node: None for node in nodes}
visited = {}
current = 1
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)