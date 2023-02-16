# 11003
import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

now = deque()

for i in range(N):
    while now and now[-1][0] > A[i]:
        now.pop()
    now.append((A[i], i))
    if now[0][1] <= i - L:
        now.popleft()
    print(now[0][0], end=' ')