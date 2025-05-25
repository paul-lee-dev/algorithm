import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    com1, com2 = map(int, input().split())
    graph[com2].append(com1)

def bfs(start):
    visited = [False] * (N+1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                count += 1

    return count

res = [0] * (N+1)
max_res = 0

for i in range(1, N+1):
    res[i] = bfs(i)
    max_res = max(res[i], max_res)

for i in range(1, N+1):
    if res[i] == max_res:
        print(i, end=' ')