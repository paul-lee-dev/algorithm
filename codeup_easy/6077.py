N = int(input())
total = 0
for i in range(1, N+1):
    if i % 2 == 0:
        total += i
print(total)