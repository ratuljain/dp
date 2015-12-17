graph2 = { 0 : [1, 3],
           1 : [0, 2],
           2 : [0, 1],
           3 : [0, 4],
           4 : []
           }
res = []
count = 1
def dfs_rec(graph, visited, start, pred, time):

    global res, count

    visited[start] = 1
    res.append(start)

    for v in [i for i in graph[start] if i not in res]:
        pred[v] = start
        count += 1
        time[v] = count
        dfs_rec(graph, visited, v, pred, time)

    return res, pred, time

visited = {i : 0 for i in graph2}
pred = {i : None for i in graph2}
time = {i : 0 for i in graph2}
time[1] = count

print dfs_rec(graph2, visited, 1, pred, time)[1]