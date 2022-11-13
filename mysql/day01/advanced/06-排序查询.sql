-- SELECT 字段列表 FROM 表名 ORDER BY 字段1 [排序方式] , 字段2 [排序方式], 字段N [排序方式];
-- 查询学生信息，以年龄升序排序
SELECT * FROM student ORDER BY stu_age;
SELECT * FROM student ORDER BY stu_age ASC;
-- 查询学生信息，以年龄降序排序
SELECT * FROM student ORDER BY stu_age DESC;

-- 查询学生信息，先进行class_id降序，在学生年龄升序
SELECT * FROM student ORDER BY class_id DESC, stu_age ASC;
