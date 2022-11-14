-- alter table 从表 add [constraint 约束名字] foreign key (外键字段) references 主表(关联字段) 
ALTER TABLE student ADD constraint student_class_fk 
FOREIGN KEY(class_id) REFERENCES class(class_id);

show create table student;