# # 퀵 정렬: 다른 정렬 알고리즘(선택 정렬, 삽입 정렬) 보다 많이 사용되는 알고리즘.
# # "기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까?"

# # 리스트에서 첫 번째 데이터를 pivot 으로 정한다.
# # 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
# # 큰 데이터와 작은 데이터의 위치를 서로 교환.

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array, start, end):
#     # 원소가 1개인 경우 종료
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:    # 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
#             array[right], array[pivot] = array[pivot], array[right]
#         else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]
    
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     quick_sort(array, start, right - 1) # 피벗과 교환된 'right' 의 위치는 이제 피벗보다 작거나 같은 값들의 구간을 나타냄. right - 1 은 피벗 바로 왼쪽에 위치한 값을 나타냄.
#     quick_sort(array, right + 1, end)   # 피벗과 교환된 'right' 의 위치는 피벗보다 작거나 같은 값들의 구간을 나타냄. right + 1 은 피벗보다 큰 값들의 구간이 시작되는 지점.

# quick_sort(array, 0, len(array) - 1)
# print(array)

# 파이썬에 최적화된 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면, 정렬된 것으로 간주하므로 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + [quick_sort(right_side)]

print(quick_sort(array))

# 퀵 정렬의 시간 복잡도: O(nlogn), 최악의 경우 O(n^2)
# 퀵 정렬의 수학적 검증보다, 퀵 정렬 구현과 시간 복잡도 정도만 이해하자.
# 이미 정렬되어 있는 경우, 삽입 정렬을 O(n) 그러나, 퀵 정렬은 O(n^2)

    
