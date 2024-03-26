def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None # 다 돌아봐도 찾고자 하는 값이 없음.

# n 원소의 개수, 그리고 target 찾고자 하는 값. 입력받기
n, target = map(int, input().split())

array = list(map(int, input().split()))

# 이진 탐색 수행결과 출력
result = binary_search(array, target, 0, n - 1)

if result == None:
    print("찾고자 하는 값이 없습니다.")
else:
    print(result + 1)


# 연습: 이진탐색, 반복문으로 구현하기