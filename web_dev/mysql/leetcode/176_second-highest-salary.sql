-- 编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+

-- 例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。

-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

-- 来源：力扣（LeetCode）
-- 链接：https://leetcode-cn.com/problems/second-highest-salary
-- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-- Thinking:
-- 1. 可以用子查询找到最大值，然后用not in 
-- 2. 直接用limit分片， 哈哈

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

