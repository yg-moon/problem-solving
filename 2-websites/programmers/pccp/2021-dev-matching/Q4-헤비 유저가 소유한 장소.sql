SELECT *
FROM PLACES
WHERE HOST_ID in (
        SELECT HOST_ID
        FROM PLACES
        GROUP BY HOST_ID
        HAVING COUNT(*) >= 2
    )
    /*
     - 난이도: Lv3
     - 간단한 서브쿼리 문제
     */