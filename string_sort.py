import sys

S = input()
result = []
sum = 0
for i in range(len(S)):
    if S[i].isnumeric():
        sum += int(S[i])
    else:
        result.append(S[i])
result.sort()
result.append(str(sum))
print(''.join(result))