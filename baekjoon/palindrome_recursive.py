#25501
import sys

def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]: 
        return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(sys.stdin.readline())

for i in range(T):
    count = 0
    S = input()
    print(isPalindrome(S), count)
