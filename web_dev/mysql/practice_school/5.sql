-- 4 查询所有学生的学生编号、学生姓名、选课总数、所有课程的总成绩

SELECT
    Student.Sid, Student.Sname, Cnum, Tsocre
FROM
    Student
LEFT JOIN
    (
        SELECT
            Sid, count(*) as Cnum, SUM(SC.score) as Tsocre
        FROM
            SC
        WHERE
            score is not NULL
        GROUP BY
            Sid
    ) as r
ON
    Student.Sid = r.Sid;