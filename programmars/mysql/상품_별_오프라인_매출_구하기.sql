-- 코드를 입력하세요
SELECT PD.PRODUCT_CODE,
       SUM(PD.PRICE * OS.SALES_AMOUNT) AS SALES
FROM PRODUCT PD
RIGHT JOIN OFFLINE_SALE OS
ON PD.PRODUCT_ID = OS.PRODUCT_ID
GROUP BY PD.PRODUCT_CODE
ORDER BY SALES DESC, PD.PRODUCT_CODE;
