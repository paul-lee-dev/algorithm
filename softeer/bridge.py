import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
count = [1] * N

for i in range(N):
    for j in range(i-1,-1,-1):
        if A[j] < A[i]:
            count[i] = max(count[:j+1]) + 1
            break
print(max(count))
