SELECT
    CAR_ID,
    MAX(CASE
        WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN '대여중'
        ELSE '대여 가능'
    END) AS AVAILABILITY
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY
    CAR_ID
ORDER BY
    CAR_ID DESC;

/*
제시하신 쿼리는 각 자동차 ID별로 '2022-10-16' 날짜가 대여 시작일과 대여 종료일 사이에 있는지 확인하여, 해당 날짜에 대여 중인 경우 '대여중'을, 그렇지 않은 경우 '대여 가능'을 표시하는 방식으로 구성되어 있습니다. MAX 함수를 사용한 이유는 CASE문을 통해 반환된 '대여중' 또는 '대여 가능' 상태 중 '대여중' 상태를 우선시하여 선택하기 위함입니다. SQL에서 '대여중'과 '대여 가능' 중 문자열 '대여중'이 '대여 가능'보다 사전적으로 뒤에 오기 때문에, MAX 함수를 사용하면 각 CAR_ID에 대해 한 번이라도 '대여중' 상태가 나타나면 '대여중'을 결과로 반환합니다.

이 쿼리는 자동차가 특정 날짜에 대여 가능한지 여부를 정확히 판단하기 위해 필요한 로직을 적절히 구현합니다. 각 CAR_ID에 대해 '2022-10-16'이 대여 기간 내에 있는 경우, 즉 어떤 대여 기록에서도 해당 날짜에 대여 상태인 경우에 '대여중'으로 표시합니다. 그리고 모든 CAR_ID에 대해 이 조건을 검사한 후, 자동차 ID를 기준으로 내림차순으로 결과를 정렬합니다.

이렇게 함으로써, 특정 날짜에 어떤 자동차가 대여 중인지, 그리고 대여 가능한지의 여부를 정확히 알 수 있으며, 제시한 쿼리는 이러한 요구사항을 만족시키는 효과적인 방법입니다.
*


/-- 코드를 입력하세요
SELECT
    CAR_ID,
    CASE
        WHEN DATE_FORMAT(START_DATE, '%Y-%m-%d') <= '2022-10-16' AND DATE_FORMAT(END_DATE, '%Y-%m-%d') >= '2022-10-16' THEN '대여중'
        ELSE '대여 가능'
    END AS ASAVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC;