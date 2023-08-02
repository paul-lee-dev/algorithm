import sys

N, M = map(int, sys.stdin.readline().split())
ball = list(range(1,N+1))

for t in range(M):
    i, j= map(int, sys.stdin.readline().split())
    temp = ball[i-1]
    ball[i-1] = ball[j-1]
    ball[j-1] = temp

print(*ball, sep=' ')
