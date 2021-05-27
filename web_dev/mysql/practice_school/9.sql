-- 8.查询至少一门课与学号为‘01’的同学所学相同的同学的信息
/*
要点分析:
    1. 搜索01同学学过的课程
    2. Student左连SC
    3. 在结果中排除01
*/

/*
改进:
    1.子查询应该会快一点
    2. 01需不需要被排除另说
*/
SELECT distinct
    Student.*
FROM
    Student
LEFT JOIN
    SC
ON
    Student.Sid=SC.Sid
WHERE
    Student.Sid <> "01"
    AND
    CId in (
        SELECT
            CId
        FROM
            SC
        WHERE
            Sid="01"
    )
-- GROUP BY
--     Student.Sid

;

-- 参考
select *
from Student
where SId in (
select distinct SId from SC
where CId in (select CId from SC where SId='01'));