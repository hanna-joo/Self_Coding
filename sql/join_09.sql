-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/133027
-- (7월 총 주문량 + 상반기 총 주문량) 값이 큰 순서대로 상위 3개 맛 조회
-- 조회 : FLAVOR
-- 정렬 : 총 주문량 값 DESC

-- SOLUTION 1 : 행 합치기 > GROUP BY > ORDER BY
SELECT FLAVOR
FROM (
    SELECT * FROM FIRST_HALF
    UNION ALL 
    SELECT * FROM JULY
) AS TOTAL
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3;


-- SOLUTION 2 :  GROUP BY > 열 합치기 > ORDER BY
SELECT A.FLAVOR
FROM FIRST_HALF AS A
    INNER JOIN (
        SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
        FROM JULY
        GROUP BY FLAVOR
    ) AS B
    ON A.FLAVOR = B.FLAVOR
ORDER BY (A.TOTAL_ORDER + B.TOTAL_ORDER) DESC
LIMIT 3;


-- SOLUTION 3 : FULL OUTER JOIN > ORDER BY
SELECT FLAVOR
-- INNER JOIN을 하게 되면 JULY에 아이스크림 신메뉴 혹은 단종 메뉴가 없어짐
-- 따라서 FULL OUTER JOIN 필수
-- mysql에는 FULL OUTER JOIN이 없음
FROM (
    SELECT A.FLAVOR, A.TOTAL_ORDER AS ATO, B.TOTAL_ORDER AS BTO
    FROM FIRST_HALF AS A
        LEFT OUTER JOIN JULY AS B
        ON A.FLAVOR = B.FLAVOR
    UNION
    SELECT A.FLAVOR, A.TOTAL_ORDER AS ATO, B.TOTAL_ORDER AS BTO
    FROM FIRST_HALF AS A
        RIGHT OUTER JOIN JULY AS B
        ON A.FLAVOR = B.FLAVOR
) AS TOTAL
GROUP BY FLAVOR
ORDER BY ATO + SUM(BTO) DESC
LIMIT 3;