# N = input()
# result = int(N[0])

# for i in range(1, len(N)):
#     num = int(N[i])
#     if ((result <= 1) or (num <= 1)):
#         result += num
#     else:
#         result *= num
# print(result)

# import sys

# N = int(sys.stdin.readline())
# adven = list(map(int, sys.stdin.readline().split()))
# adven.sort(reverse=1)
# result = 0
# i = 0
# while i <= (N-1):
#     if N - adven[i] > 0:
#         result += 1
#         i += adven[i]
#     else:
#         break
# print(result)


