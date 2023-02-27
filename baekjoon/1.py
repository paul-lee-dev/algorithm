#4375
import sys

while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break
    K = 0
    count = 0
    
    while True:
        K = 10 * K + 1
        count += 1
        if K % n == 0:
            print(count)
            break