# 공포도가 x 인 모험가는 반드시 x 명 이상으로 그룹을 구성.
# 최대 몇 개의 모험가 그룹을 만들 수 있는가.
# n 명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.
import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, input().split()))
data.sort()

result = 0   # 총 그룹의 수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1  # 현재 그룹에 해당 모험가를 먼저 포함시키기.
    if count >= i:  # count (그룹 안의 모험가의 수) 가 현재 i 공포도 이상 이라면 
        result += 1 # 그룹 결성 완료.
        count = 0

print(result)