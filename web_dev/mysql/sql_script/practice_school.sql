-- https://zhuanlan.zhihu.com/p/60216741
-- https://www.zhihu.com/search?type=content&q=mysql%E7%BB%83%E4%B9%A0%E9%A2%98
CREATE DATABASE IF NOT EXISTS `school` DEFAULT CHARACTER SET utf8mb4;
USE `school`;
DROP TABLE IF EXISTS `Student`;
create table `Student`(
    `SId` varchar(10),
    `Sname` varchar(10),
    `Sage` datetime,
    `Ssex` varchar(10)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 

insert into `Student` (`SId`, `Sname`, `Sage`, `Ssex`) values 
('01', '赵雷', '1990-01-01', '男'), 
('02' , '钱电' , '1990-12-21' , '男'),
('03' , '孙风' , '1990-12-20' , '男'),
('04' , '李云' , '1990-12-06' , '男'),
('05' , '周梅' , '1991-12-01' , '女'),
('06' , '吴兰' , '1992-01-01' , '女'),
('07' , '郑竹' , '1989-01-01' , '女'),
('09' , '张三' , '2017-12-20' , '女'),
('10' , '李四' , '2017-12-25' , '女'),
('11' , '李四' , '2012-06-06' , '女'),
('12' , '赵六' , '2013-06-13' , '女'),
('13' , '孙七' , '2014-06-01' , '女');

create table `Teacher`(
    `TId` varchar(10),
    `Tname` varchar(10));
insert into `Teacher` values 
('01' , '张三'),
('02' , '李四'),
('03' , '王五');

create table `Course`(
    `CId` varchar(10),
    `Cname` nvarchar(10),
    `TId` varchar(10)
    );
insert into `Course` values 
('01' , '语文' , '02'),
('02' , '数学' , '01'),
('03' , '英语' , '03');


create table `SC`(
    `SId` varchar(10),
    `CId` varchar(10),
    `score` decimal(18,1)
    );
    
insert into `SC` values 
('01' , '01' , 80),
('01' , '02' , 90),
('01' , '03' , 99),
('02' , '01' , 70),
('02' , '02' , 60),
('02' , '03' , 80),
('03' , '01' , 80),
('03' , '02' , 80),
('03' , '03' , 80),
('04' , '01' , 50),
('04' , '02' , 30),
('04' , '03' , 20),
('05' , '01' , 76),
('05' , '02' , 87),
('06' , '01' , 31),
('06' , '03' , 34),
('07' , '02' , 89),
('07' , '03' , 98);

