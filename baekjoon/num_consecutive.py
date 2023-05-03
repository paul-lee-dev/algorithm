#1748
import sys

N = int(sys.stdin.readline())
n = len(str(N))

total = 0

if n == 1:
    total = N
else:
    for i in range(n - 1):
        total += 9 * (10 ** i) * (i + 1)
    total += (N - 10 ** (n - 1) + 1) * n
print(total)
