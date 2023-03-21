#2609
import sys

def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    return gcd(r, a)

a, b = map(int, sys.stdin.readline().split())

print(gcd(a, b))
print(int(a*b/gcd(a, b)))