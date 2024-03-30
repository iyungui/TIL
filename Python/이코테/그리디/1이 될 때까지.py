n, k = map(int, input().split())
result = 0

while True:
    # (n == k 로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    # 예를 들어, n이 10, k가 3인 경우. target은 (10 // 3) * 3 = 9 가 되며, 9는 k의 배수가 된다.
    target = (n // k) * k
    result += (n - target)
    n = target # n 이 k 로 나누어떨어지는 상태
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기 (더 이상 k로 나눌 수 없으므로)
result += (n - 1)
print(result)
