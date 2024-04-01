# n, m = map(int, input().split())  # n x m 크기 입력 받기
# ice_frame = []  # 얼음 틀 형태를 저장할 리스트
# for _ in range(n):
#     ice_frame.append(list(map(int, input())))  # 얼음 틀 형태 입력 받기

# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False
#     if ice_frame[x][y] == 0:
#         ice_frame[x][y] = 1
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#         return True # 연결된 모든 지점을 다 호출하고 True 처리
#     return False    # x, y 지점이 이미 방문했거나, 벽 즉 1인 경우.


# result = 0

# for i in range(n):
#     for j in range(m):
#         if dfs(i, j):
#             result += 1

# print(result)
        


n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs[i][j] == True:
            result += 1

print(result)

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료한다.
    if -1 <= x <= n or -1 <= y <= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if data[x][y] == 0:
        # 해당 노드 방문 처리
        data[x][y] = 1
        # 상 하 좌 우의 위치도 모두 재귀적으로 호출한다
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x1, y + 1)
        return True
    return False
        