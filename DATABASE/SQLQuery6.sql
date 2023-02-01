--DDL-create alter drop
--dml-insert update delete
--drop from [MOCK_DATA _4(1)] where id=2
--MAX,MIN,AVG,COUNT,SUM
delete from [MOCK_DATA _4(1)] where id=2
select * from [MOCK_DATA _4(1)] where id<300 and id>400
select * from [MOCK_DATA _4(1)] where id between 20 and 30
select * from [MOCK_DATA _4(1)] where id=2
select * from [MOCK_DATA _4(1)] where id between 20 and 30

select distinct gender from [MOCK_DATA _4(1)] where gender='male'
select gender,first_name from [MOCK_DATA _4(1)] where first_name='Patrick'
select * from [MOCK_DATA _4(1)] 
alter table [MOCK_DATA _4(1)] add department_name varchar(50)
update [MOCK_DATA _4(1)] set phonenumber=27727,department_name='fsd' where id=10
update [MOCK_DATA _4(1)] set department_name='qqq' where id in (2,3,4,5,6,9,10)
update [MOCK_DATA _4(1)] set department_name='ndnndnn' where id between 20 and 30
update [MOCK_DATA _4(1)] set department_name='bsusbdbeb',phonenumber=777788855 where id between 2 and 12

--like opeartor
select * from [MOCK_DATA _4(1)] where first_name like 'F%'
select * from [MOCK_DATA _4(1)] where first_name like '%F'
select * from [MOCK_DATA _4(1)] where first_name like '%F%'
select * from [MOCK_DATA _4(1)] where first_name like '%co%'
select * from [MOCK_DATA _4(1)] where first_name like '%c%o%'
select * from [MOCK_DATA _4(1)] where first_name like '_c%'
select * from [MOCK_DATA _4(1)] where first_name like 'a_%'
select * from [MOCK_DATA _4(1)] where first_name like 'c__'
select * from [MOCK_DATA _4(1)] where first_name like 'c__%'

-----
select * from [MOCK_DATA _4(1)] order by id desc
select * from [MOCK_DATA _4(1)] order by id asc
select * from [MOCK_DATA _4(1)] order by first_name desc
select * from [MOCK_DATA _4(1)] order by first_name asc

----
select count(*) from [MOCK_DATA _4(1)]
alter table [MOCK_DATA _4(1)] alter column phonenumber bigint
select sum(phonenumber) from [MOCK_DATA _4(1)]
select max(phonenumber) from  [MOCK_DATA _4(1)]
select min(phonenumber) from  [MOCK_DATA _4(1)]
select avg(phonenumber) from  [MOCK_DATA _4(1)]
select count(phonenumber) from  [MOCK_DATA _4(1)]
--