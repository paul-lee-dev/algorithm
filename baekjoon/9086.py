import sys

N = int(sys.stdin.readline())
for _ in range(N):
    S = sys.stdin.readline().rstrip()
    print(S[0] + S[-1])