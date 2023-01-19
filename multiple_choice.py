n = int(input())
C = 0
char = ''

for i in range(n*2):
    char = char + input()

for i in range(n):
    if char[i] == char[i+n]:
        C = C + 1

print(C)