from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    #print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited