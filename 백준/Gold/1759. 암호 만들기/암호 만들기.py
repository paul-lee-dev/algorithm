from itertools import combinations


L, C = map(int, input().split())
line = sorted(list(input().split()))

for comb in combinations(line, L):
    vowelCnt = 0
    for e in comb:
        if e in 'aeiou':
            vowelCnt += 1
    if (vowelCnt > 0 and (L - vowelCnt > 1)):
        print(''.join(comb))