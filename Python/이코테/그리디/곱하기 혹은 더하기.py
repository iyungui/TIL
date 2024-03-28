# # 가장 큰 수로 만드려면
# # 0과 1은 더하고, 그 이상(2부터 9까지)는 곱하기. -> 이전의 숫자가 0이나 1인 경우에는 더하고, 이전의 숫자가 그 이상인 경우에는 곱하기

# S = input()
# # result = 0

# # result 를 처음에 0 으로 두는 것이 아닌, 첫 번째 문자로 초기화.
# result = int(S[0])

# for i in range(1, len(S)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1' 인 경우, 곱하기 보다는 더하기 수행
#     num = int(S[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num

# print(result)


data = input()
# 두 수를 연산할 때, 1이하는 더하고, 나머지는 곱하기.

# 처음 수를 result 로 초기화 
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
print(result)

