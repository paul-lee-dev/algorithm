x = int(input())
n = int(input())
total = 0

for i in range(n):
    data = int(input())
    total = total + data

print(x * (n + 1) - total)
