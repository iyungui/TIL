# # 떡의 개수 N, 요청한 떡의 길이 M
# n, m = map(int, input().split())

# # 떡의 개별 높이
# array = list(map(int, input().split()))

# # 적어도 m 만큼의 떡을 얻기 위한 절단기 설정의 높이 최댓값

# # 파라메트릭 서치: 최적화 문제를 결정 문제(예 혹은 아니오)로 바꾸어 해결하는 기법 *
# # => 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 사용.

# # !적절한 높이를 찾을 때까지 절단기의 높이 H를 반복해서 조정하는 것. (이진 탐색을 이용하기.). 
# # 현재 이 높이로 자르면 조건을 만족할 수 있는가? -> 조건의 여부에 따라서, 탐색범위를 좁힘(이진 탐색)
# start = 0
# end = max(array)

# result = 0

# while start <= end:
#     total = 0   # 잘린 떡의 전체 길이
#     mid = (start + end) // 2    # 절단기 높이
#     for x in array:
#         # 잘랐을 때의 떡의 양 계산
#         if x > mid: # 절단기의 높이보다 높은 떡에 대해서
#             total += x - mid
#     # 떡의 양이 요구보다 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
#     if total < m:
#         end = mid - 1
#     # 떡의 양이 요구보다 많은 경우 덜 자르기(오른쪽 부분 탐색)
#     else:
#         result = mid    # 요청한 떡의 길이 m 과 잘린 떡의 전체 길이가 일치했을 때, mid(그 때의 높이) 가 정답.
#         start = mid + 1

# print(result)


n, m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)
result = 0
while start>=end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < mid:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)