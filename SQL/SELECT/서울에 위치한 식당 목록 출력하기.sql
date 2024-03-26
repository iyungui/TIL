-- 서울에 위치한 식당 목록 출력하기
/*
GROUP BY 절을 사용하는 주된 이유는 여러 행의 데이터를 기준 컬럼(들)의 고유한 값에 따라 그룹화하여, 
각 그룹에 대해 집계 함수(예: AVG, SUM, COUNT 등)를 적용하기 위함입니다. 
이 경우, REST_INFO 테이블과 REST_REVIEW 테이블을 조인한 후, 
주소가 '서울특별시'로 시작하는 식당들에 대해 각 식당의 리뷰 평균 점수를 계산하고자 합니다. 

이를 위해:
각 식당(REST_ID)별로 그룹화하고
그룹별로 리뷰 점수(REVIEW_SCORE)의 평균을 계산합니다.
*/

SELECT
    I.REST_ID,
    I.REST_NAME,
    I.FOOD_TYPE,
    I.FAVORITES,
    I.ADDRESS,
    ROUND(AVG(R.REVIEW_SCORE), 2) AS SCORE
FROM
    REST_REVIEW R
JOIN
    REST_INFO I ON I.REST_ID = R.REST_ID
WHERE
    I.ADDRESS LIKE '서울%'
GROUP BY
    I.REST_ID,
    I.REST_NAME,
    I.FOOD_TYPE,
    I.FAVORITES,
    I.ADDRESS
ORDER BY
    SCORE DESC, I.FAVORITES DESC;


