def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

N, M = map(int, input().split())

graph = []
graph = [list(map(int, input())) for x in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count += 1

print(count)
