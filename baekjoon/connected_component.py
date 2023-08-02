# 11724
import sys
sys.setrecursionlimit(10000)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

T = int(sys.stdin.readline())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = [[] for _ in range(N+1)]
    count = 0

    visited = [False] * (N+1)
    for _ in range(M):
        s, e = map(int, sys.stdin.readline().split())
        A[s].append(e)
        A[e].append(s)

    for i in range(1, N+1):
        if not visited[i]:
            count += 1
            DFS(i)

    print("#"+ str(tc+1) + " " + str(count))