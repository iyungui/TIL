# 이진 탐색으로 풀기.

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
    
# n = int(input())
# array = list(map(int, input().split()))
# array.sort()

# m = int(input())
# x = list(map(int, input().split()))

# # 손님이 확인 요청한 부품 번호를 하나씩 확인
# for i in x:
#     # 해당 부품이 존재하는 지 확인.
#     result = binary_search(array, i, 0, n - 1)
#     if result != None:
#         print('yes', end = ' ')
#     else:
#         print('no', end=' ')

##
# 계수 정렬로 풀기
# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1

# m = int(input())

# x = list(map(int, input().split()))

# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')



##
# 집합 자료형 이용해서 풀기
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')