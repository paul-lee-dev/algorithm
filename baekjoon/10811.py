import sys

N, M = map(int, sys.stdin.readline().split())
ball = list(range(1, N+1))

for t in range(M):
    i, j = map(int, sys.stdin.readline().split())
    for l in range((j-i)//2+1):
        temp = ball[i-1+l]
        ball[i-1+l] = ball[j-1-l]
        ball[j-1-l] = temp

print(*ball, sep=' ')
