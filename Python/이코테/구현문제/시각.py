# 00시 00분 00초 ~ n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수
# for 문으로, 0부터 n + 1 까지, 그리고 그 안에 또 for 문으로 0 ~ 60, for 문으로 0 ~ 60 으로 range 를 두고 하나씩 조회 하면서,
# 3 을 만날 때마다, cnt += 1

n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # if 3 in (i, j, k):      # 이 코드는 예를 들어, 23시 05분 02 초 의 경우, 3 != 23 이므로, 문제의 요구사항을 충족시키지 않는다.
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)

                