-- 7.查询没有学全所有课程的同学的信息
/*
改进:
    1. 多表联结查询需要在中间加逗号
    2. 多表联结不会出现NULL的情况, 与inner join类似
    3. 表达式判断会有三种返回值true, false, null
*/

SELECT
    M.*
FROM
    (
        SELECT  
            count(*) as C1
        FROM
            Course
    ) as C, 
    (
        SELECT 
            Student.*, C2
        FROM
            Student
        LEFT JOIN
            (
                SELECT
                    Sid, count(*) as C2
                FROM
                    SC
                GROUP BY
                    Sid 
            ) as S
        ON 
            Student.Sid = S.Sid 
    ) as M
WHERE
    M.C2 is NULL
    OR
    C.C1>M.C2
;

-- 参考
select student.*,count(sc.SId) as num_course
from student left join sc
on student.SId=sc.SId
group by student.SId
having num_course<(select count(CId) from course);