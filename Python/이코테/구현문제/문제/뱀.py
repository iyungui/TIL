# 보드의 크기 n
n = int(input())

# 사과의 개수 k
k = int(input())

# 맵 정보 초기화
data = [[0] * (n + 1) for _ in range(n + 1)]

info = []   # 방향 회전 정보

# 맵 정보 data 에 사과의 위치 정보 입력
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 뱀의 방향 변환 횟수 l
l = int(input())

# 뱀의 방향 변환 정보
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    # 뱀의 처음 머리 위치
    x, y = 1, 1
    # 뱀이 존재하는 위치는 2로 표시, 사과가 있는 곳은 1로 표시, 아무것도 없다면 0
    data[x][y] = 2
    # 뱀이 처음에는 동쪽을 보고 있으므로,
    direction = 0
    # 시작한 뒤에 지난 '초' 시간을 반환 해야 하므로, 0으로 초기화
    time = 0
    # 다음에 회전할 정보를 담을 index
    index = 0
    # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    q = [(x, y)]
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            # 사과가 없다면, 꼬리 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면, 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 뱀이 벽이나 몸통과 부딪혔다면
        else:
            time += 1
            break

        # 다음 위치로 머리를 이동
        x, y = nx, ny
        time += 1

        # 회전할 시간인 경우 회전
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())