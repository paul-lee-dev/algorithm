elder = input()
n = int(input())
cnt = 1

for i in range(n):
    winner, loser = input().split()

    if loser == elder[-1]:
        if not winner in elder:
            cnt = cnt + 1
        elder = elder + winner

print(elder[-1])
print(cnt)
