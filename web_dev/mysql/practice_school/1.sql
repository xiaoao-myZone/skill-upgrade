/* 
1.1
查询01课程比02课程成绩高的学生信息及课程分数 01 02都存在
*/

/*
1. 需要组合一张表, 有学生的基本信息, 以及01, 02 两个课程的成绩
2. 需要将课程01和课程02作为新字段
3. 比较这两个新字段
*/

USE `school`

SELECT
    Student.*, 
    MAX(CASE WHEN SC.CId='01' THEN SC.score END) as C1,
    MAX(CASE WHEN SC.CId='02' THEN SC.score END) as C2
FROM
    SC
LEFT JOIN
    Student
ON
    SC.SId = Student.SId
GROUP BY
    Student.Sid, Student.Sname, Student.Sage, Student.Ssex
HAVING
    C1 is not NULL
    AND
    C2 is not NULL
    AND
    C1>C2
;
