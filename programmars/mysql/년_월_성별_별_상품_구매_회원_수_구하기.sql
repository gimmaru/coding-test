-- 코드를 입력하세요
WITH SALES_USER AS(
    SELECT DISTINCT 
           YEAR(SALES_DATE) AS YEAR,
           MONTH(SALES_DATE) AS MONTH,
           USER_ID 
    FROM ONLINE_SALE
)

SELECT SU.YEAR,
       SU.MONTH,
       UI.GENDER,
       COUNT(*) AS USERS
FROM SALES_USER SU
LEFT JOIN USER_INFO UI
ON UI.USER_ID = SU.USER_ID
WHERE UI.GENDER IS NOT NULL
GROUP BY SU.YEAR, SU.MONTH, UI.GENDER
ORDER BY SU.YEAR, SU.MONTH, UI.GENDER;

-- IS NULL, IS NOT NULL