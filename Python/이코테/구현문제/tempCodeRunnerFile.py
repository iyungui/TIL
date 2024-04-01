# 맵의 세로, 가로 크기 각각 n, m
n, m = map(int, input().split())

# 캐릭터 위치좌표(x, y) 그리고 보고 있는 방향 d
x, y, d = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵 정보
visited = [[0] * m for _ in range(n)]

# 현재 캐릭터가 위치하고 있는 좌표는 방문 처리
visited[x][y] = 1

# 육지/바다 맵 정보
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 순서대로 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 시뮬레이션 시작
count = 1  # 방문한 칸의 수(현재 좌표 포함하여 시작)
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    # nx, ny 를 사용하여, 그 위치에 미리 가보고, 각각 회전시킨 후, 이동시킨 후의 위치를 저장
    nx, ny = x + dx[d], y + dy[d]

    # 회전한 이후의 정면에 아직 가보지 않은 칸이 존재한다면(회전하고 이동시킨 후의 위치(nx, ny) 가 아직 방문하지 않은 곳이라면), 그리고 동시에 그 칸이 육지라면
    if visited[nx][ny] == 0 and data[nx][ny] == 0:
        # 이동한 좌표를 방문 처리
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        # 한 칸 앞으로 간 위치에서, 네 방향을 다시 돌아야 하므로
        turn_time = 0
        # turn_left() 부터 다시시작
        continue

    # 회전, 이동 후의 위치가 방문한 곳이거나, 바다인 경우
    else:
        # 회전만 수행
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 미리 가 본 위치(nx, ny) 를 다시 이전 위치로 이동
        nx, ny = x - dx[d], y - dy[d]
        # 뒤 쪽이 육지인 경우 뒤로 가기
        if data[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        # 뒤로 갈 수 없는 경우
        else:
            break

print(count)