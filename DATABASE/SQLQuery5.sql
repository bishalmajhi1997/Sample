---COLUMN---ALTER
alter table
select * from [MOCK_DATA _4(1)]
alter table [MOCK_DATA _4(1)] add course varchar(50) --adding columns
alter table [MOCK_DATA _4(1)] drop column course    --deleting columns
create table dummy1(rollno int,phonenumber int)
insert into dummy1 values(10,63727245978)
select * from dummy1
alter table dummy1 alter column phonenumber bigint
drop table dummy1

alter table [MOCK_DATA _4(1)] add phonenumber bigint
alter table [MOCK_DATA _4(1)]  alter column phonenumber int

alter table dummy1 add phonenumber1 int 
alter table dummy1 alter column phonenumber1 bigint
update dummy1 set phonenumber1=8456878272 where rollno=10

insert into dummy1 values(11,20282992,2992922)
insert into dummy1 values(11,20282992,2992922)
insert into dummy1 values(11,20282992,2992922)
insert into dummy1 values(11,20282992,2992922)
insert into dummy1 values(11,20282992,2992922)
-----CONDITION---
alter table [MOCK_DATA _4(1)] add PH1 int
select * from [MOCK_DATA _4(1)] where  id>343
select * from [MOCK_DATA _4(1)] where  id<343
select * from [MOCK_DATA _4(1)] where  id>=343
select * from [MOCK_DATA _4(1)] where  id<>3

------AND OR----

select * from [MOCK_DATA _4(1)] where  id>500 and id>8000
select * from [MOCK_DATA _4(1)] where  id>500 or id>8000

select * from [MOCK_DATA _4(1)] where  id<600 and id>500
select * from [MOCK_DATA _4(1)] where  id>500 and id<600

---between---
select * from [MOCK_DATA _4(1)] where  id between 500 and 550
select * from [MOCK_DATA _4(1)] where  id not between 10 and 20

