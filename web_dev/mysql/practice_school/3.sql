-- 2.1 查询平均成绩大于等于60的同学的学生编号和学生姓名和平均成绩

/*
1. 在select中套一个子查询, 会不会降低效率 TODO
*/

SELECT
    Student.sid, MAX(sname) as name, AVG(score) as avg
FROM
    Student
RIGHT JOIN
    SC
ON
    Student.sid = SC.sid
GROUP BY
    Student.sid
HAVING
    avg>=60
;

-- select中的子查询
SELECT 
    Sname, SId, (
        SELECT 
            avg(score) 
        FROM 
            SC 
        WHERE 
            SC.SId=Student.SId 
        GROUP BY 
            SId
        HAVING 
            AVG(score)>=60
        ) as avg_score 
FROM 
    Student
HAVING
    avg_score is not NULL
;