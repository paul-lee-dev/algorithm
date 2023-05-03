# 16935
import sys

def cmd1():
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        temp[i] = A[N - i - 1]
    return temp


def cmd2():
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i][j] = A[i][M - j - 1]
    return temp

def cmd3(A, N, M):
    temp = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            temp[i][j] = A[N - 1 - j][i]
    return temp

def cmd4(A, N, M):
    temp = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            temp[i][j] = A[j][M - 1 - i]
    return temp

def cmd5():
    temp = [[0] * M for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            temp[i][M//2 + j] = A[i][j]
    for i in range(N//2):
        for j in range(M//2, M):
            temp[N//2 + i][j] = A[i][j]
    for i in range(N//2, N):
        for j in range(M//2, M):
            temp[i][j - M//2] = A[i][j]
    for i in range(N//2, N):
        for j in range(M//2):
            temp[i - N//2][j] = A[i][j]
    return temp


def cmd6():
    temp = [[0] * M for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            temp[N//2 + i][j] = A[i][j]
    for i in range(N//2):
        for j in range(M//2, M):
            temp[i][j - M//2] = A[i][j]
    for i in range(N//2, N):
        for j in range(M//2, M):
            temp[i - N//2][j] = A[i][j]
    for i in range(N//2, N):
        for j in range(M//2):
            temp[i][j + M//2] = A[i][j]
    return temp

N, M, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for x in range(N)]

commands = list(map(int, sys.stdin.readline().split()))

for cmd in commands:
    if cmd == 1:
        A = cmd1()
    elif cmd == 2:
        A = cmd2()
    elif cmd == 3:
        A = cmd3(A, N, M)
        N, M = M, N
    elif cmd == 4:
        A = cmd4(A, N, M)
        N, M = M, N
    elif cmd == 5:
        A = cmd5()
    else:
        A = cmd6()

for i in A:
    print(*i)
