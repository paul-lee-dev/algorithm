#1940
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
start = 0
end = N - 1
count = 0
S.sort()

while start < end:
    check = S[start] + S[end]
    if check == M:
        count += 1
        end -= 1
        start += 1
    elif check < M:
        start += 1
    else:
        end -= 1
print(count)