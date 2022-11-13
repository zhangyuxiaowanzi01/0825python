-- 标量子查询
-- 查询1班的学生信息
-- 1. 利用1班名称查询1班的id
SELECT class_id FROM class WHERE class_name='1班';
-- 2. 利用1班id查询所有学生信息
SELECT * FROM student WHERE class_id = '1';
-- 子查询语句
SELECT * FROM student WHERE class_id = 
(SELECT class_id FROM class WHERE class_name='1班');