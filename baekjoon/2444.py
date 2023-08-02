import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    star = '*' * ((2*i) + 1)
    blank = ' ' * (N-i-1)
    print(blank + star, end='\n')

for j in range(N-1):
    star = '*' * (2*N - 2*j - 3)
    blank = ' ' * (j+1)
    print(blank + star, end='\n')