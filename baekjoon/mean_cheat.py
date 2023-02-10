import sys

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
M = max(S)
total = sum(S)
cheat_score = total * 100 / M / N
print(cheat_score)