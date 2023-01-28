create table customers(
customers_Id int primary key,
customer_name varchar(50),
address varchar(50)
)
select * from customers;
insert into customers values(1000,'Aayesha','Guntur');
insert into customers values(1001,'Aayesha','Guntur');
insert into customers values(1002,'Aayesha','Guntur');
insert into customers values(1003,'Aayesha','Guntur');
insert into customers values(1004,'Aayesha','Guntur');
drop table customers
delete from customers where customers_id=1005;