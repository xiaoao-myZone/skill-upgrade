-- 1.1 查询01课程比02课程成绩高的学生信息及课程分数 01 02都存在


/*
1. 需要组合一张表, 有学生的基本信息, 以及01, 02 两个课程的成绩
2. 需要将课程01和课程02作为新字段
3. 比较这两个新字段
*/

/*
1. 选中一个表的所有字段, Student.*
2. column不区分大小写, 但是表名和数据库名需要区分大小写
3. CASE WHEN THEN END, 自定义函数
4. 子查询需要被包入一个()
5. sql语句的编译顺序, from --> join --> on --> where --> group by --> select --> having --> order by --> limit
*/

USE `school`

SELECT
    Student.*, 
    MAX(CASE WHEN SC.CId='01' THEN SC.score END) as C1,
    MAX(CASE WHEN SC.CId='02' THEN SC.score END) as C2
FROM
    Student
LEFT JOIN
    SC
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

-- 子查询

SELECT
    *
FROM 
    Student 
RIGHT JOIN
    (
        SELECT 
            t1.sid, C1,C2 
        FROM
            (
                SELECT 
                    sid,score as C1 
                FROM 
                    SC
                WHERE 
                    SC.cid='01'
            ) as t1,
            (
                SELECT 
                    sid,score as C2 
                FROM 
                    SC 
                WHERE 
                    SC.cid='02'
            ) as t2
        WHERE 
            t1.sid=t2.sid 
            AND 
            t1.c1>t2.c2
    ) AS r
ON 
    Student.sid=r.sid;

-- from 后面可以跟多个表
