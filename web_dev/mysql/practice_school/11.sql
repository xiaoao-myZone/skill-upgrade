-- 10.查询没学过‘张三’老师教授的任一门课程的学生姓名

/*
需求分析
    1. 找到所有张三教授的课程
    2. 将SC中的学生分组, 然后查找里面是否有这些课
    3. 或者, 搜索有这些课的学生id在Student中做排除
*/
SELECT DISTINCT
    Student.*
FROM
    Student
WHERE
    SId not in (
        SELECT DISTINCT
            SId
        FROM
            SC
        WHERE
            CId in (
                SELECT
                    CId
                FROM
                    Course, Teacher
                WHERE
                    Teacher.Tname = '张三'
                    AND
                    Teacher.TId = Course.TId
            )
    )
;
