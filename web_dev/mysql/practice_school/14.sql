-- 13.查询平均成绩由高到低显示所有学生的所有课程的成绩及平均成绩
-- sql有办法根据col内的值生成colName吗?

/*
colName不可以使用'-', 可以使用'_'
*/
SELECT
    Student.SId,
    Sname,
    CId_01, 
    CId_02, 
    CId_03, 
    avgScore
FROM
    Student
LEFT JOIN
    (
        SELECT
            SId,
            SUM(IF(CId='01', score, null)) CId_01, 
            SUM(IF(CId='02', score, null)) CId_02, 
            SUM(IF(CId='03', score, null)) CId_03, 
            AVG(score) avgScore
        FROM
            SC
        GROUP BY
            SC.SId

    ) as r
ON
    Student.SId = r.SId
ORDER BY
    avgScore
DESC
;

select * from SC
left join (select sid,avg(score) as avg_score from SC
           group by sid)r 
on r.sid=SC.sid
order by avg_score desc;
