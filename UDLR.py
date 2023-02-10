import sys

N = int(sys.stdin.readline())
mov = sys.stdin.readline().split()
X = 1
Y = 1
#R, L, U, D
move_type = ['R', 'L', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for dir in mov:
    for i in range(4):
        if dir == move_type[i]:
            nx = X + dx[i]
            ny = Y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    X, Y = nx, ny
print(X, Y)