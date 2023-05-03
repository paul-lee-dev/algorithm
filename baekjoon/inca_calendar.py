#6064
import sys
import math

T = int(sys.stdin.readline())

for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    max = math.lcm(M, N)
    a = 0
    ans = -1
    check = 0
    while(check < max):
        check = M * a + x
        if (check - y) % N == 0:
            ans = check
            break
        a += 1
    print(ans)