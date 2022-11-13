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

-- 行子查询（子查询结果为一行）
-- 查询class_id=1这个班级年龄最大的人
-- 1. 查询class=1的班级中的最大年龄
SELECT class_id, max(stu_age) FROM student WHERE class_id = 1; 
-- 2. 利用班级id和最大年龄查询对应学生信息
SELECT * FROM student WHERE class_id = 1 and stu_age = 32;
-- 子查询语句
SELECT * FROM student WHERE (class_id, stu_age) = 
(SELECT class_id, max(stu_age) FROM student WHERE class_id = 1);

-- 表子查询（子查询结果为多行多列）
-- 1. 查询分数大于39的所有学生信息
SELECT * FROM student WHERE stu_score > 39;
-- 2. 在分数大于39的学生里找出年龄小于30的学生信息
SELECT * FROM 
(SELECT * FROM student WHERE stu_score > 39) sub_student
WHERE stu_age < 30;








