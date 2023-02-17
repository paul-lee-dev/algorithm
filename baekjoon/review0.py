import sys
#baekjum probs

#1546
# N = int(sys.stdin.readline())
# score = list(map(int, sys.stdin.readline().split()))
# sum = 0
# max = 0
# for i in range(N):
#     sum += score[i]
#     if max < score[i]:
#         max = score[i]
# result = (sum / max) * 100 / N
# print(result)

#11659
# N, M = map(int, sys.stdin.readline().split())
# S = list(map(int, sys.stdin.readline().split()))
# S.insert(0, 0)

# for i in range(1, N+1):
#     S[i] += S[i-1]


# for j in range(M):
#     start, end = map(int, sys.stdin.readline().split())
#     print(S[end] - S[start-1])

#11660
N, M = map(int, sys.stdin.readline().split())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


S.append([0]*(N+1))
for i in range(N):
    S[i].insert(0, 0)
