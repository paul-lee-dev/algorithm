# 10808

s = input()
alpha = [0] * 26

for x in s:
    index = ord(x) - ord('a')
    alpha[index] += 1

print(*alpha)