# 2309
import sys

def fun(A):
    total = sum(A)
    A.sort()

    for j in range(8):
        temp = total - A[j]
        for k in range(j+1, 9):
            if temp - A[k] == 100:
                del A[k]
                del A[j]
                return A

dwalf = [0]*9

for i in range(9):
    dwalf[i] = int(sys.stdin.readline())

real = fun(dwalf)

for x in range(7):
    print(real[x], sep='\n')