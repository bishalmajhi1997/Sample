create table employee_5(employee_id int,name varchar(50),salary int)
select * from employee_5
insert into employee_5 values(1,'bishal',20000)
insert into employee_5 values(2,'Moulali',30000)
insert into employee_5 values(3,'SKKHAJA',40000)
insert into employee_5 values(4,'Monika',50000)
insert into employee_5 values(5,'Trupti',60000)
insert into employee_5 values(6,'Manoj',70000)
insert into employee_5 values(7,'Arpita',80000)
alter table employee_5 add bonus bigint
update employee_5 set bonus=
          case when salary>30000 and salary<60000 then salary *30/100
		   when salary>60000 and salary<70000 then salary *20/100
		   when salary>50000 and salary<80000 then salary *40/100
           when salary>40000 and salary<50000 then salary *35/100
		   when salary >20000 then salary*10/100
		   else 20000
		   end

create procedure countstudent9 (@studentcount int output)
as 
 begin  
 select @studentcount=count(employee_id) from employee_5
 end
 ---
declare @totalstudentx int
---Don't forget to use the keyword output
exec countstudent9 @totalstudentx output
---print the result
print @totalstudentx
-------------

---------------------------
create table productqty(id int identity(1,1),
region varchar(100),
product varchar(50),
year int,
quantity int)
insert into productqty (region,product,quantity,year) values('east','computer',20209999,2020),('South', 'Computer', 2020, 45000),
('North', 'Computer', 2020, 25000),
('East', 'Hard Disk', 2020, 1900),
('West', 'Computer', 2021, 25000),
('South', 'Hard Disk', 2021, 5500),
('West', 'Hard Disk', 2021, 6500),
('East', 'Pen Drive', 2021, 1200),
('North', 'Mouse', 2019, 1600),
('South', 'Pen Drive', 2019, 2700),
('East', 'Mouse', 2019, 2000),
('West', 'Pen Drive', 2019, 1900); 
select * from productqty
select sum(year) as totalpurchase from productqty group by quantity
select product,sum(year) as totalpurchaseforthatyear  from productqty where id in  (2,3,4,5,6,7,8,9,10,11,12,13) group by quantity,product
select region,sum(year) as totalyear from productqty where id in (2,3,4,5,6,7,8,9,10,11,12,13) group by region,year
select region,sum(year) as tt from productqty group by region
select quantity,sum(year) as tt from productqty group by quantity
select region,quantity,sum(year) as tt from productqty group by region,quantity

----------------if else,if-----------------
if(1=1)
print 'if statement:condition is true'
else
print 'else statement:condition is false'

if(1=2)
print 'if statement:condition is true'
else
print 'else statement:condition is false'

declare @course_id int=4
if(@course_id=4)
print 'true'

declare @age int
 set @age=20
if @age <18
    print 'underage'
else

   if @age <22 
       print 'you are below 50'
   else
       print 'senior'	
