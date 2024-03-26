n, m = map(int, input().split())
currency = [int(input()) for _ in range(n)]

dp = [10001] * (m + 1) # 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않다. 10001.
dp[0] = 0   # 0 원을 만들기 위한 최소한의 화폐 개수는 0

for c in currency:
    for i in range(c, m + 1):
        if dp[i - c] != 10001:   # i - c 원을 만드는 방법이 존재하는 경우
            dp[i] = min(dp[i], dp[i - c] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])