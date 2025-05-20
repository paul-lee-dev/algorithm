import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

def solve(n, board):
    rd = [0] * (2*n - 1)  # 우하향 대각선
    ans = 0

    def in_range(y, x):
        return 0 <= y < n and 0 <= x < n

    def upper_bound(diag):
        able_rus = 0
        for d in range(diag, 2*n - 1):
            for y in range(d + 1):
                x = d - y
                if in_range(y, x) and board[y][x] and not rd[x - y + n - 1]:
                    able_rus += 1
                    break
        return able_rus

    def dfs(diag, cnt):
        nonlocal ans
        if diag == 2*n - 1:
            ans = max(ans, cnt)
            return

        ub = upper_bound(diag)
        if ub + cnt <= ans:
            return

        for y in range(diag + 1):
            x = diag - y
            if in_range(y, x) and board[y][x] and not rd[x - y + n - 1]:
                rd[x - y + n - 1] = 1
                dfs(diag + 1, cnt + 1)
                rd[x - y + n - 1] = 0

        dfs(diag + 1, cnt)

    dfs(0, 0)
    return ans

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, board))