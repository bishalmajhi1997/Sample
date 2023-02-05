create table fsd_python(
rollno int,
name varchar(30),
course varchar(50)
)
insert into fsd_python values(1001,'Bishal','fsd')
insert into fsd_python values(1002,'kumar','fsd')
insert into fsd_python values(1003,'majhi','fsd')
insert into fsd_python values(1004,'depeak','fsd')
insert into fsd_python values(1005,'sworna','fsd')
insert into fsd_python values(1006,'gayatri','fsd')
insert into fsd_python values(1007,'kajal','fsd')
select * from fsd_python
------------------------------------------------------------------
create table fsd(rollno int,
name varchar(50),
course varchar(50))
insert into fsd select * from fsd_python
select * from fsd

--------------------------------------------------------------------
create table student_results(
rollno int,
result varchar(50)

)
-------------------------------------------
alter table student_marksheet add results varchar(50)
select * from student_marksheet
update student_marksheet
      set results=
	     case when marks >=60 then 'passed'
               when marks=60 then 'just passed'
		 else 'failed'
	   end 

