import sys

w, n = map(int, sys.stdin.readline().split())
mp = [list(map(int, sys.stdin.readline().split())) for x in range(n)]
cnt = [0] * (n + 1)

# 리스트 변수에 금속의 무게를 무게당 가격의 크기순으로 넣는다.
for i in range(n):
    cnt[mp[i][1]] += mp[i][0]

result = 0
# 무게당 가격이 큰 것부터 비교하기위해 reversed로 비교한다.
for i in reversed(range(n + 1)):
    if w < cnt[i]:
        result += w * i
        # 배낭의 무게를 꽉 채웠기때문에 break로 반복문을 빠져나온다.
        break

    result += i * cnt[i]
    # 배낭의 무게를 금속의 무게만큼 빼준다.
    w -= cnt[i]

print(result)