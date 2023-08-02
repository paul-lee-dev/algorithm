import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(lst.count(v))