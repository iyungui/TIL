n, m = map(int, input().split())    # 맵의 세로, 가로 크기 n, m
a, b, direction = map(int, input().split())     # 캐릭터 위치 a,b 그리고 방향 d

# 방문한 위치를 저장하기 위한 맵을 생성, 0으로 초기화
game_map = [[0] * m for _ in range(n)]

# 현재 캐릭터가 위치하고 있는 좌표는 방문 처리
game_map[a][b] = 1

# 전체 맵 정보 (육지, 바다) 입력
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# solution 1
def turn_left():
    global direction
    direction -= 1  # 왼쪽 방향으로 회전
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # solution 1 
    turn_left()
    # solution 2
    nx, ny = a + dx[direction], b + dy[direction]
    # 아직 방문하지 않았고, 육지라면
    if game_map[nx][ny] == 0 and data[nx][ny] == 0:
        game_map[nx][ny] = 1
        a, b = nx, ny
        count += 1
        turn_time = 0
        continue

    # 회전 후, 이동시켜본 위치가 가본 곳이너가, 바다인 경우
    else:
        # 원래 자리(a, b) 에서 회전만 수행
        turn_time += 1
    
    # turn_time 이 4 인 경우, 즉 (a, b) 에서 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx, ny = a - dx[direction], b - dy[direction]
        # 뒤쪽이 육지인 경우
        if data[nx][ny] == 0:
            a, b = nx, ny
            turn_time = 0
        # 뒤로 갈 수 없는 경우
        else:
            break

print(count)

                

