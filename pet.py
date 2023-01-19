total = [0, 0, 0, 0, 0]
for i in range(5):
    a1, a2, a3, a4= map(int, input().split())
    total[i] = a1 + a2 + a3 + a4
winner = 0
for i in range(4):
    if total[i+1] > total[winner]:
        winner = i + 1

print(winner + 1, total[winner])