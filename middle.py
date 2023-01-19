a = int(input())
b = int(input())
c = int(input())

if (a <= b) and (b <= c) and (a <= c):
    print(b)
elif (c <= b) and (b <= a) and (c <= a):
    print(b)
elif (b <= a) and (a <= c) and (b <= c):
    print(a)
elif (c <= a) and (a <= b) and (c <= b):
    print(a)
else:
    print(c)
