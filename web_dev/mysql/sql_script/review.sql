-- 信息都在一个表里， 学生id， 某科考试成绩， 考试日期（可能缺考， 缺考没有记录）
-- 输出每个学生最近三天的成绩与日期






SELECT
    sid, date, score
from
    scores A
where 
    (
        SELECT
            count(1)
        FROM
            scores B
        where
            A.sid=B.sid AND B.date>A.date

    )<3
order by A.sid, A.date
;

