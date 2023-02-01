------Foreign Key ------
----parent table
---Child Table
create table employee_Parent(
Employee_ID int primary key,
EmployeeName varChar(max) not null,
DOB date not null,
role varchar(60),
phonenumber bigint unique,
)
select * from employee_Parent
insert into employee_Parent values(1001,'bishal','12-11-2999',101,92992828828)
insert into employee_Parent values(1002,'kumar','11-11-1999','Full stack developer',643322454)
insert into employee_Parent values(1003,'majhi','sep 19 2019','react developer',765554444)
insert into employee_Parent values(1004,'mayank','oct 20 2999','python developer',92892828828)
insert into employee_Parent values(1005,'sai','nov 28 1888','django developer',92977828828)
insert into employee_Parent values(1006,'nadini','dec 29 1999','js developer',92997777828828)
update employee_Parent set role='backend developer' where Employee_ID in(1002,1003,1005)


create table employee_Experience(
ExperienceID int unique,
companyname varchar(60) not null,
total_experience int not null,
last_package varchar(20),
last_designation varchar(50),
EmployeeID int Foreign Key References employee_Parent
)

select * from employee_Experience
select * from employee_Parent
insert into employee_Experience values (1,'IBM',2,'8 lakhs','Backend developer',1001)
insert into employee_Experience values (2,'Deloitte',3,'7 lakhs','Full stack developer developer',1002)
insert into employee_Experience values (3,'TCS',2,'6 lakhs','FSD developer',1001) 
insert into employee_Experience values (4,'oracle',7,'10 lakhs','react developer',1002)
insert into employee_Experience values (5,'TCS',2,'6 lakhs','JS developer',1005)
insert into employee_Experience values (6,'TCS',2,'6 lakhs','FSD developer',1004) 
insert into employee_Experience values (7,'HCL',9,'9 lakhs','BACKEND developer',1005) 
select * from employee_Experience order by EmployeeID





select * from employee_Experience order by EmployeeID