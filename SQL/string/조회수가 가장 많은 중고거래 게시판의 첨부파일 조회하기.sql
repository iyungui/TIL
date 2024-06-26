-- solution 1
SELECT
    CONCAT('/home/grep/src/', b.BOARD_ID, '/', f.FILE_ID, f.FILE_NAME, f.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_FILE f ON b.BOARD_ID = f.BOARD_ID
WHERE
    b.VIEWS IN (
        SELECT
            MAX(VIEWS)
        FROM USED_GOODS_BOARD
    )
ORDER BY
    f.FILE_ID DESC;

-- solution 2 (join)
SELECT
    CONCAT('/home/grep/src/', b.BOARD_ID, '/', f.FILE_ID, f.FILE_NAME, f.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE f 
JOIN (
    SELECT *
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
) AS b USING(BOARD_ID)
ORDER BY f.FILE_ID DESC;

-- solution3 (join 없이)__ 주의 where 절에서 in 이 아니라, = 이 쓰임. 찾는 BOARD_ID 가 여러 개가 아니라, '하나' 이기 때문 (LIMIT 1)
SELECT
    CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
)
ORDER BY
    FILE_ID DESC;