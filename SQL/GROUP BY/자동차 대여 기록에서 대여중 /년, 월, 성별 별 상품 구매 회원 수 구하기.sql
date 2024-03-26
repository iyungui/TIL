-- 년, 월, 성별 별 상품 구매 회원 수 구하기
-- 회원 정보 USER_INFO, 온라인 상품 판매 정보 ONLINE_SALE
-- DISTINCT를 해야 하는 이유는 상품을 구매한 회원수이기 때문인데, ONLINE_SALE 테이블에는 중복된 유저가 존재하기 때문에 중복을 제거해야 한다.

SELECT
    YEAR(s.SALES_DATE) AS YEAR,
    MONTH(s.SALES_DATE) AS MONTH,
    u.GENDER,
    COUNT(DISTINCT u.USER_ID) AS USERS
FROM USER_INFO u
JOIN ONLINE_SALE s USING(USER_ID)
WHERE
    u.GENDER IS NOT NULL
GROUP BY
    YEAR, MONTH, u.GENDER
ORDER BY
    YEAR, MONTH, u.GENDER
    