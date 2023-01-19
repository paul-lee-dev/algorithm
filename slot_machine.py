n = int(input())
first = int(input())
second = int(input())
third = int(input())
cnt = 0

while n >= 1:

    first = first + 1
    if first % 35 == 0:
        n = n + 29
        cnt = cnt + 1
    elif n >= 1:
        n = n - 1
        cnt = cnt + 1

    second = second + 1
    if n >= 1 and second % 100 == 0:
        n = n + 59
        cnt = cnt + 1
    elif n >= 1:
        n = n - 1
        cnt = cnt + 1

    third = third + 1
    if n >= 1 and third % 10 == 0:
        n = n + 8
        cnt = cnt + 1
    elif n >= 1:
        n = n - 1
        cnt = cnt + 1


print(f'Martha plays {cnt} times before going broke.')
