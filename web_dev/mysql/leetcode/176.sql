SELECT *
FROM
    (SELECT
        `Salary` AS `SecondHighestSalary`
    FROM
        `TEST`
    GROUP BY
        `Salary`
    ORDER BY
        `Salary` DESC
    LIMIT 1,1);

-- SELECT * FROM TB_NAME; TB_NAME是一个空表,会出现None吗? 不会
-- 以上有两点疑问, 相同情况下,我在5.7.33-0ubuntu0.16.04.1测试的结果是,当不存在第二名时, 返回结果没有None, 是empty
-- 在上述的mysql版本中, from 接的子查询必须带有 alias

select IFNULL((select distinct(`Salary`) 
from `Employee`
order by `Salary` desc
limit 1,1),null) as `SecondHighestSalary`

--这个可以

