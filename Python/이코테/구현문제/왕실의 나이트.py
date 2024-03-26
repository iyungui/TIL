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

import sys
# 현재 나이트가 위치한 곳의 좌표
data = sys.stdin.readline().rstrip()
column = int(ord(data[0])) - int(ord('a')) + 1
row = int(data[1])

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

count = 0 

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        count += 1

print(count)

