#1202
import sys

N, K = map(int, sys.stdin.readline().split())
mv = [list(map(int, sys.stdin.readline().split())) for x in range(N)]
c = []
for i in range(K):
    c.append(int(sys.stdin.readline()))

print(mv)

print(c)