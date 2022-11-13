-- SELECT 字段列表 FROM 表名 LIMIT 起始索引, 查询记录数;   
-- 起始索引，默认就是0.如果起始索引就作为0使用，可以省略
-- 查询学生表中最后3名同学
SELECT * FROM student ORDER BY stu_id DESC LIMIT 0, 3;
SELECT * FROM student ORDER BY stu_id DESC LIMIT 3;

-- 分页原理
-- 当前第几页  每页显示条数（2）
-- 页数 limit START, LIMIT 
/*
      1         0, 2
			2 				2, 2
			3         4, 2
			4         6, 2
			    start = (当前页-1) * 每页显示条数
*/

