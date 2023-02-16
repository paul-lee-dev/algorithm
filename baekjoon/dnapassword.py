#12891
import sys

S, P = map(int, sys.stdin.readline().split())
DNA = list(sys.stdin.readline())
secret = list(map(int, sys.stdin.readline().split())) #ACGT
check = [0]*4
count = 0

#init
for i in range(P):
    if DNA[i] == 'A':
        check[0] += 1
    elif DNA[i] == 'C':
        check[1] += 1
    elif DNA[i] == 'G':
        check[2] += 1
    else:
        check[3] += 1
        
if (check[0] >= secret[0]) and (check[1] >= secret[1]) and (check[2] >= secret[2]) and (check[3] >= secret[3]):
    count += 1

for i in range(P, S):

    if DNA[i] == 'A':
        check[0] += 1
    elif DNA[i] == 'C':
        check[1] += 1
    elif DNA[i] == 'G':
        check[2] += 1
    else:
        check[3] += 1

    if DNA[i-P] == 'A':
        check[0] -= 1
    elif DNA[i-P] == 'C':
        check[1] -= 1
    elif DNA[i-P] == 'G':
        check[2] -= 1
    else:
        check[3] -= 1

    if (check[0] >= secret[0]) and (check[1] >= secret[1]) and (check[2] >= secret[2]) and (check[3] >= secret[3]):
        count += 1

print(count)