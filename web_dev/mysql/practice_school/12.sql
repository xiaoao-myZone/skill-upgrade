-- 11.查询两门及以上不及格课程的同学的学号，姓名和平均成绩

SELECT
    Student.SId, Student.Sname, AGV
FROM
    Student
INNER JOIN
    (
        SELECT
            SId, COUNT(IF(score<60, true, null)) as C, AVG(score) as AGV
        FROM
            SC
        GROUP BY
            SId
        HAVING
            C>1
    ) as r 

ON
    Student.SId = r.SId
