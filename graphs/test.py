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

unvisited = {node : None for node in nodes}
visited = {}
curr = 0
curDist = 0
unvisited[curr] = curDist

while True:
     for neigh, distance in distances[curr].items():
          if neigh not in unvisited:
               continue
          newDist = curDist + distance
          if unvisited[neigh] is None or unvisited[neigh] > newDist:
               unvisited[neigh] = newDist
     visited[curr] = curDist
     del unvisited[curr]
     if not unvisited:
          break
     candidates = [node for node in unvisited.items() if node[1]]
     curr, curDist = sorted(candidates, key = lambda x: x[1])[0]
print(visited)
