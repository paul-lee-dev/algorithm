import sys

def polygon_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
    return abs(area) / 2

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

area = polygon_area(points)

print(f"{area:.1f}\n")