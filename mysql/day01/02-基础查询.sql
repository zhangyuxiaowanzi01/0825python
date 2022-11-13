-- 查询多个字段
-- SELECT 字段1, 字段2, ... FROM 表名 ;
SELECT stu_no, stu_name FROM student;
-- SELECT * FROM 表名 ;
SELECT * FROM student;

-- 字段设置别名
-- SELECT 字段1 [AS 别名1], 字段2 [AS 别名2] ... FROM 表名;
SELECT stu_no as number, stu_name as name FROM student; 
-- SELECT 字段1 [ 别名1], 字段2 [ 别名2] ... FROM 表名;
SELECT stu_no number, stu_name name FROM student; 

-- 去除重复记
-- SELECT DISTINCT 字段列表 FROM 表名;
SELECT DISTINCT class_id FROM student;

