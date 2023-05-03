import sys

N = int(sys.stdin.readline())
total = 0
for i in range(1, 1001):
    total += i
    if total >= N:
        print(i)
        break