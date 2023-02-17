#2738
import sys

N, M = map(int, sys.stdin.readline().split())
mp1 = [list(map(int, sys.stdin.readline().split())) for x in range(N)]
mp2 = [list(map(int, sys.stdin.readline().split())) for x in range(N)]

for i in range(N):
    for j in range(M):
        mp1[i][j] += mp2[i][j]

for i in range(N):
    for j in range(M):
        print(mp1[i][j], end =' ')
    print('')