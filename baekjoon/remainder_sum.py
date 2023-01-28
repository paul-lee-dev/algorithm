#10986
import sys

N, M = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
count = 0
C = [0] * M
for i in range(1, N):
    S[i] +=S[i-1]
for i in range(N):
    S[i] = S[i] % M
    if S[i] == 0:
        count += 1
    C[S[i]] += 1
#count += S.count(0)

for i in range(M):
    if C[i] > 1:
        count += C[i] * (C[i]-1) // 2
print(count)