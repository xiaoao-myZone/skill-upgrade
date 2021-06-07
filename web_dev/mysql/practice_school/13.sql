-- 12.检索01课程分数小于60，按分数降序排列的学生信息
SELECT
    Student.*, score
FROM
    Student
INNER JOIN
    (
        SELECT
            SId, score
        FROM
            SC
        WHERE
            SC.CId = "01"
            AND
            SC.score<60

    ) as r
ON
    Student.SId = r.SId
ORDER BY
    r.score
DESC
;
