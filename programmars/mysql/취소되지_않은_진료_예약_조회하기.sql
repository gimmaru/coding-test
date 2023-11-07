-- 코드를 입력하세요
WITH DR_APNT AS(
    SELECT APNT.APNT_NO,
           APNT.PT_NO,
           APNT.APNT_YMD,
           DR.MCDP_CD,
           DR.DR_NAME
    FROM DOCTOR DR JOIN (
        SELECT * FROM APPOINTMENT
        WHERE APNT_YMD LIKE '2022-04-13%'
    ) APNT
    ON DR.DR_ID = APNT.MDDR_ID
    WHERE DR.MCDP_CD = 'CS'
    AND APNT.APNT_CNCL_YN = 'N'
)

SELECT DR_APNT.APNT_NO,
       PT.PT_NAME,
       PT.PT_NO,
       DR_APNT.MCDP_CD,
       DR_APNT.DR_NAME,
       DR_APNT.APNT_YMD
FROM PATIENT PT
JOIN DR_APNT
ON PT.PT_NO = DR_APNT.PT_NO
ORDER BY DR_APNT.APNT_YMD;