# 큰 수의 법칙

# 가장 큰 수와, 두 번째로 큰 수를 번갈아간다. (가장 큰 수 k번 반복 후, 두 번째로 큰 수 1번. 이렇게 총 m번 반복)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

first = data[0]
second = data[1]
result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    
    if m == 0:
        break

    result += second
    m -= 1

print(result)

