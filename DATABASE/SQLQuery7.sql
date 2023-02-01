create table EMPLOYEE_1(id int primary key,name varchar(50))
--properties of primary key...Does not allowed duplicate values.
insert into EMPLOYEE_1 values(1,'Manish')
insert into EMPLOYEE_1 values(2,'bishal')
select * from EMPLOYEE_1
--CONSTRAINTS---
--PRIMARY KEY CONSTRAINT---
--FOREIGN KEY CONSTRAINT----
---UNIQUE KEY CONSTRAINT---
---NOT NULL CONTSTRAINT----
----CHECK CONSTRAINT---
----DEFAULT CONSTRAINT-----
create table EMPLOYEE_2(
EmployeeID int primary key,--primaey constraint---
name varchar(50) Not null,---not null constraint--
phonenumber bigint unique ,---unqiue constraint----
age int )
insert into EMPLOYEE_2 (EmployeeID,name,phonenumber,age) VALUES (1,'bishal',888888999,66)
insert into EMPLOYEE_2 (EmployeeID,name,phonenumber,age) VALUES (2,'kumar',888888989,66)
insert into EMPLOYEE_2 (EmployeeID,name,phonenumber,age) VALUES (3,'moulali',8888868999,69)
insert into EMPLOYEE_2 (EmployeeID,name,phonenumber,age) VALUES (4,'null',88888689939,69)
insert into EMPLOYEE_2 (EmployeeID,name,age) VALUES (5,'sai',79)
---insert into EMPLOYEE_2 (EmployeeID,phonenumber,age) VALUES (5,88888888888,79)--not null(name is mandatory)

select * from EMPLOYEE_2

---properties of primary key()--doesn't allow duplicate values or not null
--using constraint WHILE altering---
create table employee_4(id int not null)
insert into employee_4 values(1)
insert into employee_4 values(2)
insert into employee_4 values(3)
insert into employee_4 values(4)
insert into employee_4 values(5)

alter table employee_4 add primary key(id)
select * from employee_4
--------------------------------------------------
alter table employee_2 add constraint uk_emp_ph_no unique(phonenumber)----unique constraint----
alter table employee_2 drop constraint uk_emp_ph_no
alter table employee_2 add constraint ck_66PLUS2 check (age>=66)--check constraint===
    