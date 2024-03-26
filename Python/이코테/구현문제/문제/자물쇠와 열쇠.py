# def rotate_key(key):
#     M = len(key)
#     rotated = [[0] * M for _ in range(M)]
#     for r in range(M):
#         for c in range(M):
#             rotated[c][M-1-r] = key[r][c]
#     return rotated

# def check_match(extended_lock, key, start_x, start_y, M, N):
#     for x in range(M):
#         for y in range(M):
#             extended_lock[start_x + x][start_y + y] += key[x][y]
#     for i in range(N, 2*N):
#         for j in range(N, 2*N):
#             if extended_lock[i][j] != 1:
#                 return False
#     return True

# def reset_extended_lock(extended_lock, key, start_x, start_y, M, N):
#     for x in range(M):
#         for y in range(M):
#             extended_lock[start_x + x][start_y + y] -= key[x][y]

# def solution(key, lock):
#     M, N = len(key), len(lock)
#     extended_lock_size = N * 3
#     extended_lock = [[0] * extended_lock_size for _ in range(extended_lock_size)]
    
#     # 자물쇠를 확장된 영역의 중앙에 배치
#     for i in range(N):
#         for j in range(N):
#             extended_lock[i + N][j + N] = lock[i][j]
    
#     for rotation in range(4):  # 4가지 회전 방향에 대해
#         key = rotate_key(key)  # 열쇠 회전
#         for x in range(1, 2*N):
#             for y in range(1, 2*N):
#                 if check_match(extended_lock, key, x, y, M, N):
#                     return True
#                 reset_extended_lock(extended_lock, key, x, y, M, N)
                
#     return False

# # 입력 예제
# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# # 함수 실행
# solution(key, lock)

def rotate_key(key):
    n = len(key)  # 행 길이 계산
    m = len(key[0])   # 열 길이 계산
    result = [[0] * n for _ in range(m)]    # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result

def check_match(extended_lock, key, start_x, start_y, M, N):
    # 열쇠의 크기 M. 열쇠의 모든 요소를 순회
    for x in range(M):
        for y in range(M):
            # 열쇠의 각 요소를, 확장된 자물쇠의 start_x + x, start_y + y 위치에 더함.
            # 이는, 열쇠를 특정 위치에 맞춰보는 작업을 시뮬레이션 한 것.
            extended_lock[start_x + x][start_y + y] += key[x][y]
    
    # 확장된 자물쇠의 중앙 부분(즉, 실제 자물쇠 부분)을 순회. 자물쇠의 크기 N
    for i in range(N, 2*N):
        for j in range(N, 2*N):
            # 확장된 자물쇠의 자물쇠 부분에 있는 각 요소가 정확히 1인지 확인.
            # 열쇠의 돌기와 자물쇠의 홈이 정확히 맞아떨어진 경우에만 값이 1이 됨.
            # 1이 아닌 경우는 돌기와 돌기가 만나거나(값이 2이상), 홈이 채워지지 않은 경우(값이 0)
            if extended_lock[i][j] != 1:
                return False
    return True

def reset_extended_lock(extended_lock, key, start_x, start_y, M, N):
    for x in range(M):
        for x in range(M):
            extended_lock[start_x + x][start_y + y] -= key[x][y]

def solution(key, lock):
    M, N = len(key), len(lock)
    extended_lock_size = N * 3
    extended_lock = [[0] * extended_lock_size for _ in range(extended_lock_size)]

    # 자물쇠를 확장된 영역의 중앙에 배치
    for i in range(N):
        for j in range(N):
            extended_lock[i + N][j + N] = lock[i][j]
    
    for rotation in range(4):   # 4가지 회전 방향에 대해
        key = rotate_key(key)   # 열쇠 회전
        for x in range(1, 2*N):
            for y in range(1, 2*N):
                if check_match(extended_lock, key, x, y, M, N):
                    return True
                reset_extended_lock(extended_lock, key, x, y, M, N)
    
    return False


