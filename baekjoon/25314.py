import sys

N = int(sys.stdin.readline())
T = int(N/4)
s = ''
for i in range(T):
    s = s + "long "

print(s + "int")
