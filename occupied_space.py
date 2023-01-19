n = int(input())
yesterday = input()
today = input()

total = 0

for i in range(n):
    if yesterday[i] == 'C' and today[i] == 'C':
        total = total + 1

print(total)