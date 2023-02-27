# 2015
import sys
N, K = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
count = 0
S = [0] * N
S[0] = A[0]

if S[0] == K:
    count += 1

for i in range(1, N):
    S[i] += S[i-1] + A[i]
    if S[i] == K:
        count += 1

# for j in range(N-1, 0, -1):
#     for k in range(j):
#         if S[j] - S[k] == K:
#             count += 1

# print(count)

S.sort()

start, end = 0, 1
print(S)
while start < N - 1 and end < N:
    check = S[end] - S[start]
    if check == K: 
        count += 1
        start += 1
    elif check < K:
        end += 1
    else:
        start += 1
print(count)
