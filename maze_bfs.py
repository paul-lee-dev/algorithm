import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    #큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        #현 위치로부터 4방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            #벽인 경우 무시
            if mp[nx][ny] == 0:
                continue 
            #해당 노드 처음 방문 시에만 최단거리 기록
            if mp[nx][ny] == 1:
                mp[nx][ny] = mp[x][y] + 1
                queue.append((nx, ny))
        #가장 오른쪽 아래까지의 최단거리 반환
    return mp[N-1][M-1]
N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, input())) for x in range(N)]
#상하좌우 방향 벡터 지정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))