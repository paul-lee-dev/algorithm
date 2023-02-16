# 1253
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
count = 0

for i in range(N):
    j, k = 0, N - 1
    while j < k:
        if A[j] + A[k] == A[i]:
            if j != i and k != i:
                count += 1
                break
            elif j == i:
                j += 1
            elif k == i:
                k -= 1
        elif A[j] + A[k] < A[i]:
            j += 1
        else:
            k -= 1

print(count)