n, m = map(int, input().split())
result = 0

## 1
# data = []
# for _ in range(n):
#     num = list(map(int, input().split()))
#     data.append(num)


# for i in range(n):
#     min_value = min(data[i])
#     result = max(result, min_value)

# print(result)


##  2

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(result, min_value)

print(result)
