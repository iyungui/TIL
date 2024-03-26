'''
배열 A 오름차순으로 정렬
배열 B 내림차순으로 정렬

배열 A, B 를 차례대로 조회하며, k번 바꿔치기 후, A 의 모든 원소의 합의 최댓값 출력
'''

n, k = map(int, input().split())

a, b = list(map(int, input().split())), list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

# 첫 번쨰 인덱스부터 확인하며, 두 배열의 원소를 최대 k 번 비교
for i in range(k):
    # A 의 원소가 B 의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
