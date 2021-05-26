-- 6.查询学过张三老师课程的学生的信息

/*
问题剖析
    1. 先将学生和选课联成一张表
    2. 再将这个表与老师的表联立
    3. 做筛选
    4. 也可以先实现选课与老师的联立
    5. 中间还要用课程联系Tid和Cid
    6. 当一个老师教多门课, 并且有学生选了同一个老师的多门课时, 结果会有重复信息
*/

/*
改进:
    1. 用 in 来代替 JOIN 
    2. 使用多表联结查询
*/

SELECT
    Student.*
FROM
    (
        SELECT
            Sid
        FROM
            SC

        INNER JOIN
            (
                SELECT
                    CId
                FROM
                    Teacher
                INNER JOIN
                    Course
                ON
                    Teacher.Tid = Course.Tid
                WHERE
                    Tname="张三"
            ) as t  
        ON
            t.CId=SC.CId
        GROUP BY
            Sid
    ) as r
LEFT JOIN
    Student
ON
    Student.Sid = r.Sid
;

SELECT
    Student.*
FROM
    Student, SC, Course, Teacher
WHERE
    Course.TId = Teacher.TId
    AND
    Student.Sid = SC.Sid
    AND
    SC.CId = Course.CId
    AND
    Teacher.Tname = "张三"
;
    
