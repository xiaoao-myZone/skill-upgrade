-- 3.查询SC表存在成绩的学生信息

/*
问题剖析
1. 关键在于SC中有多个科目成绩的Sid会使得结果重复
2. 对于第二种更优的解法, 左连和右连区别很大 
3. 搞清楚三种join的关系 TODO
*/

-- Not well
SELECT
    Student.*
FROM
    Student
LEFT JOIN
    SC
ON
    SC.Sid = Student.Sid
where 
    SC.score is not NULL;

-- ok
SELECT
    Student.*
FROM
    Student
INNER JOIN
    (
        SELECT
            Sid
        FROM
            SC
        WHERE
            score is not NULL
        GROUP BY
            Sid
    ) as r
ON
    r.Sid = Student.Sid;