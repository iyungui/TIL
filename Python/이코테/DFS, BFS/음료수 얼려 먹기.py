n, m = map(int, input().split())  # n x m 크기 입력 받기
ice_frame = []  # 얼음 틀 형태를 저장할 리스트
for _ in range(n):
    ice_frame.append(list(map(int, input())))  # 얼음 틀 형태 입력 받기

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if ice_frame[x][y] == 0:
        ice_frame[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True # 연결된 모든 지점을 다 호출하고 True 처리
    return False    # x, y 지점이 이미 방문했거나, 벽 즉 1인 경우.


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
        