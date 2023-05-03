def solution(maps):
    nx = 0
    ny = 0
    n = len(maps) - 1
    m = len(maps[0]) - 1
    print(n ,m)
    #R, L, D, U
    answer = 0
    while nx != m or ny != n:
        if maps[ny+1][nx] == 1:
            ny += 1
            answer += 1
            print(ny, nx)
        elif maps[ny][nx+1] == 1:
            nx += 1
            answer += 1
            print(ny, nx)
        elif maps[ny][nx-1] == 1:
            nx -= 1
            answer += 1
            print(ny, nx)
        else:
            nx -= 1
            answer += 1
            print(ny, nx)
        if answer > m * n:
            answer = -1
            break
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])