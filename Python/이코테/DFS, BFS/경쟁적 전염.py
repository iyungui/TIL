from collections import deque

n, k = map(int, input().split())

# 전체 보드 정보를 담는 리스트
graph = []
# 바이러스 정보를 담는 리스트
data = []

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간(0), 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x, y = q.popleft()
    # 정확히 s 초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break

    # 현재 노드에서 주변 상하좌우 위치를 각각 확인하며, 바이러스 전파
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # 해당 위치로 바이러스가 이동할 수 있는 경우
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
            