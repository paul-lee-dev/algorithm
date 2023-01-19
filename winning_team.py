a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

a_total = a1 + (a2 * 2) + (a3 * 3)
b_total = b1 + (b2 * 2) + (b3 * 3)

if a_total > b_total:
    print('A')
elif a_total < b_total:
    print('B')
else:
    print('T')
