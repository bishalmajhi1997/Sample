create table students1(
id int identity primary key,
name varchar(50) not null,
gender varchar(50) not null,
age int not null,
total_marks int not null
)

insert into students1 VALUES ('Jolly Evans', 'Female', 20, 520),
('Josh Butler', 'Male', 22, 645),
('Rose Huges', 'Female', 25, 610),
('Laura Bennet', 'Female', 18, 430),
('Alan Simmons', 'Male', 20, 500),
('Kate Huges', 'Female', 22, 600),
('Joseph Paul', 'Male', 18, 643),
('Antonio Butler', 'Male', 23, 513),
('Diego Bennet', 'Male', 21, 699),
('Elis Simmons', 'Female', 27, 540); 

select * from students1
-------------------------------------------------------------------------------------------------------
create table #femalestudents1(
name varchar(50),
age int,
gender varchar(50)
)
select * from #femalestudents1
insert into #femalestudents1 select name,age,gender from students1 where gender='female'
-----------------------------------------------------------------------------------------------------------
create table #malestudents1(
name varchar(50),
age int,
gender varchar(50)
)
select * from  #malestudents1
insert into #malestudents1 select name,age ,gender from students1 where gender='male'
------------------------------------------------------------------------------------------------------------------
declare @student1 table(
id int,
name varchar(50)
)
insert into @student1 values(1,'bishal')
insert into @student1 values(2,'kumar')
insert into @student1 values(3,'majhi')
insert into @student1 values(4,'moulali')
insert into @student1 values(5,'mayanka')
insert into @student1 values(6,'khaja')
select * from @student1
----------------------------------------------------------------------





