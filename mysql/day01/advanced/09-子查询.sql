-- 标量子查询
-- 查询1班的学生信息
-- 1. 利用1班名称查询1班的id
SELECT class_id FROM class WHERE class_name='1班';
-- 2. 利用1班id查询所有学生信息
SELECT * FROM student WHERE class_id = '1';
-- 子查询语句
SELECT * FROM student WHERE class_id = 
(SELECT class_id FROM class WHERE class_name='1班');

-- 列子查询
-- 查询1班和2班所有学生信息
-- 1. 查询1班和2班的class_id
SELECT class_id FROM class WHERE class_name = '1班' OR class_name = '2班';
SELECT class_id FROM class WHERE class_name in ('1班', '2班');
-- 2. 利用classid查询对应学生
SELECT * FROM student WHERE class_id = 1 OR class_id=2;
SELECT * FROM student WHERE class_id in (1, 2);
-- 子查询语句
SELECT * FROM student WHERE class_id 
in (SELECT class_id FROM class WHERE class_name in ('1班', '2班'));







