#12427
import sys

# def Divisor(n):

#     divisorsList = []

#     for i in range(1, int(n**(1/2)) + 1):
#         if (n % i == 0):
#             divisorsList.append(i)
#             if ((i**2) != n):
#                 divisorsList.append(n // i)

#     divisorsList.sort()

#     return divisorsList

N = int(sys.stdin.readline())
total = 0

for i in range(1, N+1):
    for j in range(1, int(i**(1/2)) + 1):
        if (i % j == 0):
            total += j
            if ((j**2) != i):
                total += i // j

print(total)