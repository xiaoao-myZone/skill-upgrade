-- 14.查询各科成绩的最高分、最低分和平均分
SELECT
    CId, max(score) high, min(score) low, avg(score) avarage
From 
    SC
GROUP BY
    CId
;