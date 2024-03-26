# # 내 풀이
# n = input()
# tmp_l = 0
# tmp_r = 0
# for i in range(1, len(n) + 1):
#     if i <= len(n) // 2:
#         tmp_l += int(n[i - 1])
#     else:
#         tmp_r += int(n[i - 1])

# if tmp_l == tmp_r:
#     print("LUCKY")
# else:
#     print("READY")


## 정답지 풀이
n = input()
length = len(n)
summary = 0

# 왼쪽 부분
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분
for i in range(length // 2, length):
    summary -= int(n[i])

# +왼쪽 부분 + (-오른쪽 부분) = 0 이면, 럭키
if summary == 0:
    print("LUCKY")
else:
    print("READY")
