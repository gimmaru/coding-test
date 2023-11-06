-- 코드를 입력하세요
SELECT * 
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE INSTR(OPTIONS, '네비게이션') != 0
    ORDER BY CAR_ID DESC;

-- INSTR: https://jjeongil.tistory.com/929

-- 코드를 입력하세요
SELECT * 
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE OPTIONS LIKE '%네비게이션%'
    ORDER BY CAR_ID DESC;