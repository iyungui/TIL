-- july 테이블에서, 같은 맛의 아이스크림이라도 다른 출하 번호를 갖게 된다고 명시되어 있음
-- 이는, 같은 맛의 아이스크림이 TOTAL_ORDER 를 여러개 가지고 있다는 말
-- JULY 테이블에서 같은 맛의 아이스크림 주문량을 모두 합칩니다.
-- 이는 GROUP BY 절을 사용하여 동일한 FLAVOR에 대한 TOTAL_ORDER의 합계를 계산.
-- 계산된 합계를 FIRST_HALF 테이블에 있는 상반기 주문량과 결합 후, 계산된 합계로 내림차순 정렬, limit3

SELECT
    f.FLAVOR
FROM FIRST_HALF f
JOIN (
    SELECT
        FLAVOR,
        SUM(TOTAL_ORDER) AS sum_total_order
    FROM JULY
    GROUP BY FLAVOR
) AS j USING(FLAVOR)
ORDER BY
    f.TOTAL_ORDER + j.sum_total_order DESC
LIMIT 3;