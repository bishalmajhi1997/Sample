create table employ_1(empid int,empsalary int)
insert into employ_1 values (1,10000)
insert into employ_1 values (2,20000)
insert into employ_1 values (3,30000)
insert into employ_1 values (4,40000)
select * from employ_1

create procedure usp_employee_crud
(
@empid int,
@empsalary int
)
as 
begin
  update employ_1
  set empsalary=@empsalary where empid=@empid
end

exec usp_employee_crud 3,40000

alter table employ_1 add first_name varchar(20)
alter table employ_1 add last_name varchar(20) 
alter table employ_1 add city varchar(20) 
alter table employ_1 add first_name varchar(20) 
select * from employ_1
update employ_1 set first_name='Bishal',last_name='kumar',city='mumbai' where empid =1
update employ_1 set first_name='majhi',last_name='arpita',city='kolkata' where empid =2
update employ_1 set first_name='trupti',last_name='mandal',city='chennai' where empid =3
update employ_1 set first_name='shristi',last_name='bhagat',city='newdelhi' where empid =4

create procedure employeee_all_crud(
@id int,
@first_name varchar(30),
@last_name varchar(30),
@salary decimal(20,2),
@city varchar(20),
@statementype nvarchar(20)='')
as
   begin
     if @statementype='Insert'
	    begin
		   insert into employ_1(empid,first_name,last_name,empsalary,city) values (@id,@first_name,@last_name,@salary,@city)
	    end
	 if @statementype='select'
	    begin
		    select * from employ_1 where empid=@id
		end
	 if @statementype='update'
	    begin 
		    update employ_1 set first_name=@first_name,last_name=@last_name,empsalary=@salary,city=@city
		end
	 if @statementype='delete'
	    begin 
		     delete from employ_1 where empid=@id
		end
	       
	end

exec employeee_all_crud @statementype='insert' ,@id=1001,@first_name='abhijeet',@last_name='prasad',@salary=363636,@city='hyderabad'
exec employeee_all_crud @statementype='insert' ,@id=1002,@first_name='abhijeet',@last_name='prasad',@city='jammu',@salary=2222

exec employeee_all_crud @statementype='update' ,@id=1002,@first_name='kumar',@last_name='sonu',@city='baikunyh',@salary=26363
exec employeee_all_crud @statementype='delete' ,@id=1002,@first_name='kumar',@last_name='sonu',@city='baikunyh',@salary=26363
exec employeee_all_crud @statementype='select',@id=1001,@first_name='kumar',@last_name='sonu',@city='baikunyh',@salary=26363
select * from employ_1