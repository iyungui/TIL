from itertools import combinations
import sys
s = sys.stdin.readline().rstrip
# 연구소의 크기 n, m
n, m = map(int, s().split())

# 0: 빈칸, 1: 벽, 2: 바이러스

# 연구소 맵
lab_map = []

for _ in range(n):
    lab_map.append(list(map(int, s().split())))


def spread_virus(x, y, map_copy):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and map_copy[nx][ny] == 0:
            map_copy[nx][ny] = 2
            spread_virus(nx, ny, map_copy)

def count_safe_area(map_copy):
    safe_area = sum(row.count(0) for row in map_copy)
    return safe_area

# 가능한 모든 벽의 조합을 시도하며, 각 조합에 대해 바이러스 퍼짐 시뮬레이션 후, 남은 안전영역의 크기를 리턴
def solution():
    max_safe = 0
    empty_spaces = [(i, j) for i in range(n) for j in range(m) if lab_map[i][j] == 0]
    for walls in combinations(empty_spaces, 3):
        map_copy = [row[:] for row in lab_map]
        for x, y in walls:
            map_copy[x][y] = 1  # 벽 세우기
        for i in range(n):
            for j in range(m):
                if map_copy[i][j] == 2: # 바이러스가 있는 곳에서
                    spread_virus(i, j, map_copy)
        max_safe = max(max_safe, count_safe_area(map_copy))
    return max_safe

print(solution())