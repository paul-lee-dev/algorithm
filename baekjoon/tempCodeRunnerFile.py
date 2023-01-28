import sys
N = int(sys.stdin.readline())

count = 1
start = 1
end = 1
sum = 1
while end != N:
    if sum < N:
        end += 1
        sum += end
    elif sum == N:
        end += 1
        count += 1
        sum += end
    else:
        sum -= start
        start += 1

print(count)