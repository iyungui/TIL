-- /// Solution 1

SELECT
    PRODUCT_ID,
    PRODUCT_NAME,
    PRODUCT_CD,
    CATEGORY,
    PRICE
FROM
    FOOD_PRODUCT
ORDER BY
    PRICE DESC
LIMIT 1;



-- /// Solution 2

SELECT
    PRODUCT_ID,
    PRODUCT_NAME,
    PRODUCT_CD,
    CATEGORY,
    PRICE
FROM
    FOOD_PRODUCT
WHERE
    PRICE IN
    (
        SELECT
            MAX(PRICE)
        FROM
            FOOD_PRODUCT
    )