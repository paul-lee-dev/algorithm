#1002
import sys

T = int(sys.stdin.readline())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    distance = distance ** (0.5)

    D = r1 + r2
    if r1 > r2:
        S = r1 - r2
    else:
        S = r2 - r1

    if D > distance:
        if S == 0  and distance == 0:
            print('-1')
        elif S > distance:
            print('0')
        elif S == distance:
            print('1')
        else:
            print('2')
    elif D < distance:
        print('0')
    else:
        print('1')