
n = int(input())
data = list(map(int, input().split()))


dp = [0] * 100

dp[0] = data[0]
dp[1] = max(data[0], data[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + data[i])

print(dp[n - 1])

# data 를 내림차순으로 '정렬' 하는 것은 안됨. 인접한 식량 창고에 접근 할 수 없기 때문.
# 그럼, 기존 data 를 순열로 하여, 조회하면서, 기존에 얻은 식량 값 보다, 큰 값으로 갱신