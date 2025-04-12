while True:
    ary = list(map(int, input().split()))
    if ary[0] == 0 and ary[1] == 0 and ary[2] == 0:
        break
    
    ary.sort()
    
    if ary[0]**2 + ary[1]**2 == ary[2]**2:
        print("right")
    else:
        print("wrong")