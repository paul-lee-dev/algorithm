import sys
N, K = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(K):
    a, b = map(int, sys.stdin.readline().split())
    for j in range(a-1, b):
        result += S[j]
    result = result/(b-a+1)
    result = round(result, 2)
    print(result)
    result = 0
