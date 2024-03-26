# n = int(input())
# plans = list(input().split())

# x, y = 1, 1

# # plans 에 있는 plan 을 하나씩 조회 하면서 (for 문), 해당 범위에 있을 때에만(if 문) 이동한다.
# # 만약 plan 이 'L' 일 경우에는, 왼쪽으로 한 칸 이동 즉. (1, 2) 에서는 (1, 1) 로 이동하는 것과 같다.


# directions = {
#     'L' : (0, -1),
#     'R' : (0, 1),
#     'U' : (-1, 0),
#     'D' : (1, 0)
# }

# for plan in plans:
#     nx, ny = x + directions[plan][0], y + directions[plan][1]
#     if 1 <= nx <= n and 1 <= ny <= n:
#         x, y = nx, ny
    
# print(x, y)

n = int(input())
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
directions = ['L', 'R', 'U', 'D']

x, y = 1, 1

for plan in plans:
    for i in range(len(directions)):
        if plan == directions[i]:
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n:
                x, y = nx, ny

print(x, y)