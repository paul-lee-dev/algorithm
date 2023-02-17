#2563
import sys

N = int(sys.stdin.readline())
mp = [list(map(int, sys.stdin.readline().split())) for x in range(N)]
area = [[0]*100 for _ in range(100)]
for i in range(N):
    for j in range(10):
        for k in range(10):
            area[mp[i][0] + j][mp[i][1] + k] = 1
area = sum(area, [])
print(sum(area))