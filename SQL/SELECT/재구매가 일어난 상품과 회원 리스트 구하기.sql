/*
동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재한다고 했고
재구매 이력이 있는 회원 ID와 상품 ID를 나타내는 문제입니다!
 
따라서 '회원 ID'와 '상품 ID'을 각각 의미하는 'USER_ID', 'PRODUCT_ID' 컬럼을 기준으로
'GROUP BY'문을 이용하여 집계하고 
집계 결과에서 2회 이상 구매한 내역만 조회하면 되겠다고 생각했어요!
*/

SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;


--
