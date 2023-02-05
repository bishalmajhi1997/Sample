create table student_marksheet(
studentid int unique,
name varchar(10),
marks int not null)
select * from student_marksheet
insert into student_marksheet values(1,'Bishal',88)
insert into student_marksheet values(2,'Moulali',77)
insert into student_marksheet values(3,'Khaja',66)
insert into student_marksheet values(4,'Arpita',55)
insert into student_marksheet values(5,'Trupti',86)
insert into student_marksheet values(6,'Jaku',98)
insert into student_marksheet values(7,'Manoj',80)
insert into student_marksheet values(8,'Krishna',44)
insert into student_marksheet values(9,'Shristi',37)
insert into student_marksheet values(10,'Askha',95)
insert into student_marksheet values(11,'Mama',93)
insert into student_marksheet values(12,'Nandini',66)
select studentid as "STUDENT_ID" ,name as "STUDENT_NAME", marks as "SCORE" ,marks/10 as "CGPA" from student_marksheet
-------case statements----------------
select * ,
     case
	    when marks >=90 then 'a+'
		when marks >=80 then 'b+'
	    when marks >=70 then 'c+'
	    when marks >=60 then 'd+'
	    when marks >=50 then 'e+'
	    when marks >=40 then 'f+'
	    when marks >=45 then 'g+'
	    when marks >=50 then 'f+'
	    when marks >=30 then 'o+'
        else 'f'
	end as 'grade'
from student_marksheet;
------case statements-------------
select * from student_marksheet order by marks desc
select * from student_marksheet order by marks asc
-------------------------------------------------------
select name,marks ,
     case
	    when marks >=90 then 'a+'
		when marks >=80 then 'b+'
	    when marks >=70 then 'c+'
	    when marks >=60 then 'd+'
	    when marks >=50 then 'e+'
	    when marks >=40 then 'f+'
	    when marks >=45 then 'g+'
	    when marks >=50 then 'f+'
	    when marks >=30 then 'o+'
        else 'f'
	end as 'grade'
from student_marksheet order by marks desc;

------------------------------------------------
select name,
     case
	    when marks >=90 then 'a+'
		when marks >=80 then 'b+'
	    when marks >=70 then 'c+'
	    when marks >=60 then 'd+'
	    when marks >=50 then 'e+'
	    when marks >=40 then 'f+'
	    when marks >=45 then 'g+'
	    when marks >=50 then 'f+'
	    when marks >=30 then 'o+'
        else 'f'
	end as 'grade'
from student_marksheet order by marks desc
----------------------------------------------------
select name,
     case
	    when marks >=90 then 'a+'
		when marks >=80 then 'b+'
	    when marks >=70 then 'c+'
	    when marks >=60 then 'd+'
	    when marks >=50 then 'e+'
	    when marks >=40 then 'f+'
	    when marks >=45 then 'g+'
	    when marks >=50 then 'f+'
	    when marks >=30 then 'o+'
        else 'f'
	end as 'grade',
	count(*) as 'number_of_students' 
from student_marksheet group by marks order by grade desc
Select Name,count(Marks) from student_marksheet

----------------------------------------------
select 
     case
	    when marks >=90 then 'a+'
		when marks >=80 then 'b+'
	    when marks >=70 then 'c+'
	    when marks >=60 then 'd+'
	    when marks >=50 then 'e+'
	    when marks >=40 then 'f+'
	    when marks >=45 then 'g+'
	    when marks >=50 then 'f+'
	    when marks >=30 then 'o+'
        else 'f'
	end as "Result",
	count(*) as "number_of_students" 
from student_marksheet group by marks order by Result desc
-----------------------
select name,
     case 
	     when marks >=60 then 'Passed'
	     else  'failed'
     end as 'result'
from student_marksheet  order by marks desc
-----------------------------------------------
