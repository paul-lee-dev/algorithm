#1107
import sys

N = list(sys.stdin.readline())
M = sys.stdin.readline()
broken = list(map(int, sys.stdin.readline().split()))
target = int(N)
# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - target)

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(i[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(i) - 1:
            min_count = min(min_count, abs(int(i) - target) + len(i))

print(min_count)
