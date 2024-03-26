/*
SELECT
    CATEGORY,
    MAX(PRICE) AS MAX_PRICE, 
    PRODUCT_NAME
FROM
    FOOD_PRODUCT
WHERE
    CATEGORY IN ('과자', '국', '김치', '식용유')
GROUP BY
    CATEGORY
ORDER BY
    PRICE DESC;


위 코드가 틀린 이유는 각 CATEGORY 그룹 내에 여러 PRODUCT_NAME이 존재할 수 있고, MAX(PRICE)로 그룹화된 결과에 대해 어떤 PRODUCT_NAME을 선택해야 하는지 SQL이 결정할 수 없기 때문입니다.

예를 들어, '식용유' 카테고리에 여러 가지 상품이 있고 각각 다른 가격이 있다면, MAX(PRICE) 함수는 이 중 가장 높은 가격을 찾지만, 그 가격에 해당하는 PRODUCT_NAME을 자동으로 결정할 수 없습니다.

문제를 해결하기 위해, 각 분류별로 가장 비싼 상품을 찾은 후 해당 상품의 이름을 가져오려면 서브쿼리, 윈도우 함수 또는 다른 접근 방식을 사용해야 합니다. 
*/


-- solution 1
SELECT
    CATEGORY,
    PRICE AS MAX_PRICE, 
    PRODUCT_NAME
FROM
    FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (
    SELECT
        CATEGORY,
        MAX(PRICE)
    FROM FOOD_PRODUCT
    GROUP BY
        CATEGORY
    HAVING
        CATEGORY IN ('과자', '국', '김치', '식용유')
)
ORDER BY
    PRICE DESC;


-- solution 2
SELECT
    f.CATEGORY,
    f.PRICE AS MAX_PRICE, 
    f.PRODUCT_NAME
FROM
    FOOD_PRODUCT f
INNER JOIN (
    SELECT
        CATEGORY,
        MAX(PRICE) AS MAX_PRICE
    FROM
        FOOD_PRODUCT
    GROUP BY
        CATEGORY
    HAVING
        CATEGORY IN ('과자', '국', '김치', '식용유')
) AS max_price_query ON f.CATEGORY = max_price_query.CATEGORY AND f.PRICE = max_price_query.MAX_PRICE
ORDER BY
    PRICE DESC;