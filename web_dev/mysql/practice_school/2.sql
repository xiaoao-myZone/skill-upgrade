-- 1.2 查询01课程比02课程成绩高的学生信息及课程分数 01存在 02可能不存在
SELECT 
    Student.*,
    MAX(CASE WHEN SC.cid='01' THEN SC.score END) AS C1,
    MAX(CASE WHEN SC.cid='02' THEN SC.score END) AS C2
FROM
    Student
RIGHT JOIN
    SC
ON
    Student.sid = SC.sid
GROUP BY
    Student.sid, Student.sage, Student.ssex, Student.sname
HAVING
    C1 is not NULL
    AND
    (
        C2 is NULL
        OR 
        C1>C2 
    );



