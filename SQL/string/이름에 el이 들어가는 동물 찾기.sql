SELECT
    ANIMAL_ID,
    NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%'
AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME

-- 만약, 대소문자를 구분해야 한다면,
-- WHERE UPPER(NAME) LIKE '%EL%'
위와 같이 대문자로 변경 후, 대문자와 비교하는 식으로 작성.