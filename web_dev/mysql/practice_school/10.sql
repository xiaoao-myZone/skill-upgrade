-- 9.查询和01同学课程完全相同的学生的信息
/*
要点分析:
    1. 可将课程排序后组合起来, 用=来比较(不可行)
*/
select SId,Count(SId) as num_course
from sc  
where CId in('01','02','03')
group by SId
having num_course=3;
-- 你可真牛逼

select *
from student
where SId in(select SId
                    from sc  
                    where CId in(select CId from sc where SId='01')
                    group by SId
                    having Count(SId)=(select count(CId)from sc where SId='01'));
