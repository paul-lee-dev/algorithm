import sys
from typing import List


MAX_N = 10
INF = 1000000000

n, k = 0, 0  # n: 체스판 크기의 절반, k: 허용된 이동 횟수
board = [[0] * (2 * MAX_N) for _ in range(2 * MAX_N)]  # 체스판
steps = [[0] * (2 * MAX_N) for _ in range(2 * MAX_N)]  # 각 위치에서의 점수
row_size, row_sum = [0] * (2 * MAX_N), [0] * (2 * MAX_N)  # 각 행의 크기와 합
col_size, col_sum = [0] * (2 * MAX_N), [0] * (2 * MAX_N)  # 각 열의 크기와 합
start_row, start_col = 0, 0  # 시작 위치
opt1, opt2 = [], []  # 각 비숍의 최적 점수

def horizontal_flip():
    """체스판을 수평으로 뒤집는 함수"""
    global board
    for row in range(2 * n):
        board[row] = board[row][::-1]

def finish(moves: int, score: int, max_row: int, min_row: int):
    """
    현재 상태에서의 최종 점수를 계산하고 업데이트하는 함수
    
    :param moves: 현재까지의 이동 횟수
    :param score: 현재까지의 점수
    :param max_row: 고려해야 할 최대 행
    :param min_row: 고려해야 할 최소 행
    """
    global opt1
    # 최적의 행 선택 (시작 행 또는 가장 높은 점수를 가진 행)
    best_row = start_row
    if min_row <= start_row:
        best_row = max(range(min_row), key=lambda row: row_sum[row])

    tmp = []
    for row in range(max_row):
        if row == start_row or row == best_row:
            score += row_sum[row]
            moves += row != start_row
        else:
            tmp.append(row_sum[row])

    # 남은 행들의 점수를 내림차순으로 정렬
    tmp.sort(reverse=True)
    
    # 가능한 모든 이동에 대해 최대 점수 갱신
    if moves <= k:
        opt1[moves] = max(opt1[moves], score)
    for val in tmp:
        score += val
        moves += 1
        if moves <= k:
            opt1[moves] = max(opt1[moves], score)

def rec(col: int, moves: int, score: int, max_row: int, min_row: int):
    """
    재귀적으로 최적의 점수를 계산하는 함수
    
    :param col: 현재 열
    :param moves: 현재까지의 이동 횟수
    :param score: 현재까지의 점수
    :param max_row: 고려해야 할 최대 행
    :param min_row: 고려해야 할 최소 행
    """
    if col == 2 * (n - 1):
        # 끝에 도달하면 최종 점수 계산
        finish(moves, score, max_row, min_row)
    else:
        # 현재 열을 선택하지 않는 경우
        if col != start_col:
            rec(col + 1, moves, score, max_row, min_row)
        
        # 현재 열에서 비숍을 제거
        for row in range(col_size[col]):
            row_sum[row] -= steps[row][col]

        # 현재 열을 선택하는 경우
        rec(col + 1, moves + (col != start_col), score + col_sum[col],
            max(max_row, col_size[col]), col_size[col])

        # 비숍을 원래 위치로 복구
        for row in range(col_size[col]):
            row_sum[row] += steps[row][col]

# 입력 처리
n, k = map(int, input().split())
for row in range(2 * n):
    board[row] = list(map(int, input().split()))

result = -INF  # 최종 결과 초기화

# 두 비숍에 대해 각각 계산
for player in range(2):
    # 변수 초기화
    for i in range(2*n):
        row_size[i] = col_size[i] = row_sum[i] = col_sum[i] = 0

    # 비숍의 이동 경로 계산
    rows = 0
    for i in range(n):
        for sgn_i in [-1, 1]:
            if i == 0 and sgn_i == 1:
                continue
            for j in range(n):
                for sgn_j in [-1, 1]:
                    # 대각선 위치 계산
                    d1 = sgn_i * (2 * i)
                    d2 = 2 * n - 1 + sgn_j * (2 * j + 1)
                    r, c = (d1 + d2) // 2, (d2 - d1) // 2
                    if 0 <= r < 2*n and 0 <= c < 2*n:
                        # 유효한 위치인 경우 정보 저장
                        steps[rows][row_size[rows]] = board[r][c]
                        row_sum[rows] += board[r][c]
                        col_sum[row_size[rows]] += board[r][c]
                        col_size[row_size[rows]] += 1
                        row_size[rows] += 1
            rows += 1

    # 시작 위치 설정
    start_row = 2 * (n // 2) - 1
    start_col = 2 * ((n - 1) // 2)

    # 최적 점수 배열 초기화
    opt1 = [-INF] * (k + 1)

    # 재귀 함수 호출로 최적 점수 계산
    rec(0, 0, 0, 0, 2 * n)

    # 시작 위치의 점수 제거 (중복 계산 방지)
    opt1[0] -= steps[start_row][start_col]
    
    # 누적 최대값 계산
    for i in range(2, k + 1):
        opt1[i] = max(opt1[i], opt1[i-1])

    # 체스판 뒤집기 및 결과 저장
    horizontal_flip()
    opt1, opt2 = opt2, opt1

# 두 비숍의 점수 합 최대화
for i in range(k + 1):
    result = max(result, opt1[i] + opt2[k-i])

print(result)