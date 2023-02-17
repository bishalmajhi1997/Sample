-------User defined Function-------------------
---Max(),min(),avg(),sum(),count()
create function udf_net_saless( 
@quantity int,
@price dec(10,2),
@discount dec(3,2)
)
 returns dec(10,2)
 as
  begin 
  return @quantity * @price *(1-@discount)
  end
  ---------
 select dbo.udf_net_saless(35,500,0.3) as net_sales---dbo is  mandatory

 ---------------------

 create table student(
 rollno int primary key,
 marks int,

 )
 insert into student values(1,90)
 insert into student values(2,80)

 insert into student values(3,70)
 insert into student values(4,60)
 insert into student values(5,50)


 select * from student
 create table subject(
 subject1 int,
 subject2 int,
 subject3 int,
 rollno int foreign key references student)
 insert into subject values(20,30,40,1)
  insert into subject values(30,30,40,2)
 insert into subject values(0,30,40,2)
 insert into subject values(30,30,40,3)
 insert into subject values(20,30,40,3)

 select * from subject

 -------------
 create function getstudentmarks(@rno int)
 returns varchar(50)
 as 
  begin 
    return (select marks from student where rollno=@rno)
end
print(dbo.getstudentmarks(3))



--------
create function getallstudentmarks(@marks int)
returns table as return (select * from student where marks>=@marks)

-- print(dbo.getallstudentmarks(60)) is showing error.
 select * from getallstudentmarks(60)

 ----------------
 alter table student add name varchar(50)
 update student set name='bishal' where rollno in (1)
  update student set name='kumar' where rollno in (2)
 update student set name='majhi' where rollno in (3)
 update student set name='moulali' where rollno in (4)
 update student set name='yousuf' where rollno in (5)

 select * from student

 ---------
 create function getavg(@name varchar(50))
 returns @marks table(name varchar(50),subject1 int,subject2 int,subject3 int,average decimal(4,2))
 as begin
     declare  @avg decimal(4,2)
	 declare @rno int
	 insert into @marks(name) values (@name)
	 select @rno=rollno from student where name=@name
     select @avg=(subject1+subject2+subject3)/3 from subject 
     update @marks set subject1=(select subject1 from subject where rollno=@rno),
                  subject2=(select subject2 from subject where rollno=@rno),
				  subject3=(select subject3 from subject where rollno=@rno),
				  average=@avg
				  where name=@name
			return end
print(dbo.getavg('bishal'))

select * from getavg('bishal')