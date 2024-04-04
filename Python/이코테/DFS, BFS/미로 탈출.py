from collections import deque

n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input())))

# 상 하 좌 우. 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if data[nx][ny] == 0:
                continue
            # 처음 방문한 경우
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx, ny))
    return data[n-1][m-1]


print(bfs(0, 0))

