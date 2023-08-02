import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N+1):
    if i%10==3 :
        print("X", end=' ')
    elif i%10==6 :
        print("X", end=' ')    
    elif i%10==9 :
        print("X", end=' ')
    else:
        print(i, end=' ')