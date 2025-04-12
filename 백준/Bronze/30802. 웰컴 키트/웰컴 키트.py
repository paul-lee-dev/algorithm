import math
N = int(input())
ary = list(map(float, input().split()))
T, P = map(int, input().split())
totalT = 0
for i in ary:
    totalT += math.ceil(i/T)
print(totalT)
print(N//P, end=" ")
print(N%P)