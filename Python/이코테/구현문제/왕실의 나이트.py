# import sys

# data = sys.stdin.readline().rstrip()

# row = int(data[1])
# column = int(ord(data[0])) - int(ord('a')) + 1

# # 이동 후의 좌표 nx, ny 가 범위 안에 있다면, count += 1


# # 나이트의 이동방법
# steps = [
#     (-2, -1),
#     (-2, 1),
#     (2, -1),
#     (2, 1),
#     (-1, -2),
#     (-1, 2),
#     (1, -2),
#     (1, 2)
# ]

# count = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if 1 <= next_row <= 8 and 1 <= next_column <= 8:
#         count += 1

# print(count)

# import sys
# # 현재 나이트가 위치한 곳의 좌표
# data = sys.stdin.readline().rstrip()
# column = int(ord(data[0])) - int(ord('a')) + 1
# row = int(data[1])

# steps = [
#     (-1, -2),
#     (1, -2),
#     (-1, 2),
#     (1, 2),
#     (-2, -1),
#     (-2, 1),
#     (2, -1),
#     (2, 1)
# ]

# count = 0 

# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if 1 <= next_row <= 8 and 1 <= next_column <= 8:
#         count += 1

# print(count)



# 현재 나이트가 위치한 곳의 좌표
data = input()
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 경우의 수
answer = 0

# 전형적인 완전 탐색 구현 문제. 나이트의 현재 좌표에서 모든 방향으로 하나씩 이동하여, 이동 가능하다면. answer += 1 을 한다.
# 방향은 문제에서 나온 대로, 수평 한칸. 수직 두칸 이거나, 수평 두칸, 수직 한칸이다.
steps = [
    (-1, -2),
    (1, -2),
    (-1, 2),
    (1, 2),
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1)
]


for step in steps:
    next_row, next_column = row + step[0], column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        answer += 1

print(answer)
