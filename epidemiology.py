P = int(input())
N = int(input())
R = int(input())
day = 0
total = 0

while total <= P:
    total = total + N
    day = day + 1
    N = N * R

print(day - 1)