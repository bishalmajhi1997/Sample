--Joins Are used to Club two tables or displaying columns from more
--than one table
--Types of Joins--Use 0n Keyword or where clause 
--Inner Join
--Self join
--Cross Join
--Outer Join--Left Outer Join 
--Right Outer Join 
--Full Outer Join

--Ansi Join--Joins which use 'On' keyword is called Ansi Joins
--Inner Join
--Outer Join 
--Left outer Join 
--Right Outer Join 
--Full Outer Join
--Cross Join




--Non Ansi Join -- which uses where clause
---Self Join 
----Equi Join 
----Non Equi Join 




create table student6(
id int primary key identity,
admission_no varchar(50) not null,
first_name varchar(59) not null,
last_name varchar(59) not null,
age int,
city varchar(25) not null
)



create table fee5(
admission_no varchar(69) not null,
course varchar(69) not null,
amount_paid int,
)

INSERT INTO student6 (admission_no, first_name, last_name, age, city)       
VALUES (3354,'Luisa', 'Evans', 13, 'Texas'),       
(2135, 'Paul', 'Ward', 15, 'Alaska'),       
(4321, 'Peter', 'Bennett', 14, 'California'),    
(4213,'Carlos', 'Patterson', 17, 'New York'),       
(5112, 'Rose', 'Huges', 16, 'Florida'),  
(6113, 'Marielia', 'Simmons', 15, 'Arizona'),    
(7555,'Antonio', 'Butler', 14, 'New York'),       
(8345, 'Diego', 'Cox', 13, 'California');  
  
  
INSERT INTO Fee5 (admission_no, course, amount_paid)       
VALUES (3354,'Java', 20000),       
(7555, 'Android', 22000),       
(4321, 'Python', 18000),    
(8345,'SQL', 15000),       
(5112, 'Machine Learning', 30000); 

select * from student6
select * from fee5
SELECT student6.admission_no, student6.first_name, student6.last_name, Fee5.course, Fee5.amount_paid  
FROM student6   
JOIN fee5  
ON Student6.admission_no = fee5.admission_no;


SELECT student6.admission_no, student6.first_name, student6.last_name, Fee5.course, Fee5.amount_paid  
FROM student6   
Inner JOIN fee5  
ON Student6.admission_no = fee5.admission_no;

SELECT student6.admission_no, student6.first_name, student6.last_name, Fee5.course, Fee5.amount_paid  
FROM student6   
left JOIN fee5  
ON Student6.admission_no = fee5.admission_no;

SELECT student6.admission_no, student6.first_name, student6.last_name, Fee5.course, Fee5.amount_paid  
FROM student6   
RIGHT JOIN fee5  
ON Student6.admission_no = fee5.admission_no;

SELECT student6.admission_no, student6.first_name, student6.last_name, Fee5.course, Fee5.amount_paid  
FROM student6   
Full JOIN fee5  
ON Student6.admission_no = fee5.admission_no;

SELECT student6.admission_no, student6.first_name, student6.last_name, Fee5.course, Fee5.amount_paid  
FROM student6   
cross JOIN fee5  


--------non anshi
SELECT s1.first_name,s2.last_name,s2.city from student6 s1,student6 s2 
 where s1.id <> s2.id and s1.city=s2.city
 order by s2.city




