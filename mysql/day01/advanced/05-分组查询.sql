-- SELECT 字段列表 FROM 表名 GROUP BY 分组字段名
-- 注意: 使用了分组之后,select后面只能写分组的字段,或者聚合函数
-- 查询每个班级的学生数量
SELECT COUNT(*), class_id FROM student GROUP BY class_id;   # 1 2

-- 查询每个班级的学生平均年龄
SELECT class_id, AVG(stu_age) FROM student GROUP BY class_id;

-- 查询每个年龄的学生数量
SELECT stu_age , COUNT(*) FROM student GROUP BY stu_age;

-- GROUP_CONCAT(expr) 分组之后的字段聚合
-- 查询每个班级的学生姓名
SELECT class_id, GROUP_CONCAT(stu_name) stu_names FROM student GROUP BY class_id;

-- GROUP BY 和 WHERE同时使用
-- 查询每个班年龄大于30的所有同学姓名
SELECT class_id, GROUP_CONCAT(stu_name) FROM student WHERE stu_age > 30 GROUP BY class_id;

-- HAVING 配合 GROUP BY使用
-- 查询每个年龄人数大于1的年龄和人数
SELECT stu_age, COUNT(*) FROM student GROUP BY stu_age;
SELECT stu_age, COUNT(*) FROM student GROUP BY stu_age HAVING COUNT(*) > 1;

-- 查询班级人数大于3的班级
SELECT class_id, COUNT(*) FROM student GROUP BY class_id HAVING COUNT(*) > 3;

-- 平均年龄大于30的班级
SELECT class_id, AVG(stu_age) FROM student GROUP BY class_id HAVING AVG(stu_age) > 30;

