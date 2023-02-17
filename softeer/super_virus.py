import sys

K, P, N = map(int, sys.stdin.readline().split())
K = K * (P**(10*N))
print(K % 1000000007)
