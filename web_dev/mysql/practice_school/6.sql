-- 4.1 查询李姓老师的数量

/*
    1. col名不可以加-
    2. count在不同情况下的结果不同
*/
SELECT
    count(*) as FirstNameLi
FROM
    Teacher
WHERE
    Tname like "李%"
-- GROUP BY
--     TId
;
