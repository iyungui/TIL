# # 알파벳인 경우, 별도의 리스트에 저장. 숫자인 경우 따로 합계를 계산.

# s = input()
# result = []
# value = 0

# for i in s:
#     if i.isalpha():
#         result.append(i)
#     else:
#         value += int(i)

# # 알파벳을 오름차순으로 정렬
# result.sort()

# # 숫자가 0인 경우에는 더하지 않음. 숫자가 0이 아닌 경우, value 를 str 로 바꾼 후, result 뒤에 삽입
# if value != 0:
#     result.append(str(value))

# # result 는 리스트 이므로, join. 즉 하나의 문자열로 출력
# print(''.join(result))

## ==  다시,,

# 모든 알파벳을 먼저 출력 하고, 그 뒤에 숫자들의 합을 출력.(이 때, 0은 출력x)
S = input()
# 모든 알파벳을 별도의 리스트에 저장하고, 정렬하기. 숫자인경우는 더하기
data = []
value = 0

for i in S:
    if i.isalpha():
        data.append(i)
    else:
        value += int(i)

data.sort()

# data 는 문자로 이루어진 리스트, value 는 int 이므로, 우선 합치기
# 이때, 그냥 합치는 게 아닌, value 가 0이 아닌 경우에만 data 뒤에 append
if value != 0:
    data.append(str(value))

print(''.join(data))