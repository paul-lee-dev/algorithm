#2566
import sys

mp = [list(map(int, sys.stdin.readline().split())) for x in range(9)]
max = 0
max_x, max_y = 1, 1

for i in range(9):
    for j in range(9):
        if max < mp[i][j]:
            max = mp[i][j]
            max_x, max_y = i+1, j+1
print(max)
print(max_x, max_y)