select * from employee_4
....truncate,drop,delete----
delete from employee_4 where id=2----it deletes only single rows 
truncate table employee_4---------it deletes the entire rows.
drop table employee_4-----------it deletes the whole table
-------------------insert rollback---------------------
begin tran
insert into employee_3 values (3)
---
rollback
-----------
select * from employee_3
------------------update rollback------------------------
begin tran
update employee_3  set id=8
------
rollback
----------------

-----assignments-----------------
create emoployee table 
employe id,name,salary
------bonus--------
salary>3000 and less than 6000 bonus 30 percent of salary
salary>6000 and less than 9000 bonus 20 percent of salary
salary>600000 and less tham 200000 bonus 10 percent of salary
salary >20000 salary bonus 200000000 bonsu 5 percent of salary