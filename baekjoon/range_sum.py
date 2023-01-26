# 11659
import sys
N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L.append(0)
for i in range(N-1):
    L[i+1] += L[i]

for i in range(N):
    print(i, L[i])
for j in range(K):
    A, B = map(int, sys.stdin.readline().split())
    print(L[B-1] - L[A-2])
