# DP 를 사용할 수 있는 경우
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

# # 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
# d = [0] * 100

# # 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
# def fibo(x):
#     # 종료 조건(1 혹은 2일 때 1을 반환)
#     if x == 1 or x == 2:
#         return 1
#     # 이미 계산한 적 있는 문제라면 그대로 반환
#     if d[x] != 0:
#         return d[x]
#     # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
#     d[x] = fibo(x - 1) + fibo(x - 2)
#     return d[x]

# print(fibo(99))

# 다이나믹 프로그래밍(DP) 란, 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법 
# 시간 복잡도: O(N)

# 호출 되는 함수 확인 소스 코드
# d = [0] * 100

# def fibo(x):
#     print('f(' + str(x) + ')', end=' ')
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x - 1) + fibo(x - 2)
#     return d[x]

# fibo(11)


# # 반복문으로 DP 피보나치
# d = [0] * 100

# # 첫 번째, 두 번째 피보나치 수는 각각 1
# d[1], d[2] = 1, 1
# n = 99

# # 보텀업 다이나믹 프로그래밍
# for i in range(3, n + 1):
#     d[i] = d[i - 1] + d[i - 2]

# print(d[n])


d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
print(fibo(99))



