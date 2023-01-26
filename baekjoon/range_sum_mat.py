# 11660
import sys

N, M = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for x in range(N)]

# init
for i in range(N-1):
    mp[0][i+1] += mp[0][i]
    mp[i+1][0] += mp[i][0]

mp.append([0]*(N+1))

for i in range(1, N):
    for j in range(1, N):
        mp[i][j] = mp[i-1][j] + mp[i][j-1] - mp[i-1][j-1] + mp[i][j]

for i in range(N):
    mp[i].append(int(0))

for i in range(M):
    X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
    print(mp[X2-1][Y2-1] - mp[X1-2][Y2-1] - mp[X2-1][Y1-2] + mp[X1-2][Y1-2])
