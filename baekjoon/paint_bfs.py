#1926
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    mp[x][y] = 0
    count = 1
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
            #해당 노드 처음 방문 시에만 기록
            if mp[nx][ny] == 1:
                mp[nx][ny] = 0
                count += 1
                queue.append((nx, ny))
    return count

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for x in range(N)]

pic_size =[0]
count_pic = 0
#상하좌우 방향 벡터 지정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if mp[i][j] == 1:
            count_pic += 1
            pic_size.append(bfs(i, j))

print(count_pic)
print(max(pic_size))