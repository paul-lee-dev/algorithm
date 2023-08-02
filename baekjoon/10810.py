import sys

N, M = map(int, sys.stdin.readline().split())
ball = [0] * N
for t in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for l in range(i-1, j):
        ball[l] = k
print(*ball, sep=' ')
