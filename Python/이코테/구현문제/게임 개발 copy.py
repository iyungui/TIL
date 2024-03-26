# 맵의 세로, 가로 크기 각각 n, m
n, m = map(int, input().split())
# 캐릭터 위치좌표(x, y) 그리고 보고 있는 방향 d
x, y, direction = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성. 0으로 초기화.
d = [[0] * m for _ in range(n)]

# 현재 캐릭터가 위치하고 있는 좌표는 방문 처리
d[x][y] = 1

# 전체 맵 정보 (육지/바다 정보) 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 정의하기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1   # 현재 좌표 포함하여 시작
turn_time = 0   # 네 방향을 다 돌았는지 확인하기 위한 변수 turn_time 0으로 초기화(돌 때마다 +1 씩 증가. 4가 되면 다 돈 것으로.)

# 무한 반복문으로 시작. 안 가본 곳은 다 가보고, 문제 메뉴얼 중 3번 조건(움직임을 멈추는 조건) 에 해당하는 경우 break.
while True:
    # 왼쪽으로 회전
    turn_left()
    # nx, ny 에 먼저, 미리 가보는 것임.  각각 회전 후 이동시킨 후의 위치를 저장.
    nx, ny = x + dx[direction], y + dy[direction]

    # 회전한 이후에 정면에 아직 가보지 않은 칸이 존재한다면(회전하고 이동시킨 후의 위치가 아직 가보지 않은 곳), 그리고 그 칸이 육지라면
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 이동한 좌표(nx, ny) 를 방문 처리
        d[nx][ny] = 1
        # 그리고 이제 이 때, 실제 위치 x, y 이동
        x, y = nx, ny
        # 방문한 칸의 수도 세주고
        count += 1
        # 한 칸 앞으로 간 위치에서의, 네 방향을 다시 돌아야 하므로
        turn_time = 0
        continue    # 다시 시작. turn_left() 부터 시작하기

    # 회전, 이동시킨 위치가 가본 곳이거나, 바다인 경우
    else:
        # 회전만 수행
        turn_time += 1
    
    # turn_time 이 4가 된 경우, 즉 네 방향 모두 갈 수 없는 경우.
    if turn_time == 4:
        # nx, ny (미리 본 위치) 를 다시 이전 위치로 이동
        nx, ny = x - dx[direction], y - dy[direction]
        # (뒤 쪽이 육지인 경우) 한 칸 뒤로 갈 수 있다면, 뒤로 가기
        if array[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        # 뒤로 갈 수 없는 경우
        else:
            break

print(count)