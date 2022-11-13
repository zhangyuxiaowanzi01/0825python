/* 
SELECT 字段列表 FROM 表A ... 
UNION [ ALL ]
SELECT 字段列表 FROM 表B ....;
*/
-- UNION
SELECT stu_id, stu_name FROM student
UNION
SELECT stu_id, stu_name FROM student;

SELECT stu_age FROM student
UNION
SELECT stu_id FROM student;

-- UNION ALL
SELECT stu_id, stu_name FROM student
UNION ALL
SELECT stu_id, stu_name FROM student;
