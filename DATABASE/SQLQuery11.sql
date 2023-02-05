----Countries----------
--india,australia,----
create table countries(
country_id int not null primary key,
country_name varchar(50) not null,
currency varchar(50) not null,
timezone varchar(30) not null,
)
select * from countries
insert into countries values(1,'INDIA','Rupee','IST')
insert into countries values(3,'EUROPE','euores','EST')
insert into countries values(2,'AUSTRALIA','dollars','AST')
insert into countries values(4,'USA','dollars','UST')
insert into countries values(5,'KANADA','dollars','KST')
insert into countries values(6,'JAPAN','japanese','JST')
insert into countries values(7,'CHINA','chinese','CST')
insert into countries values(8,'RUSSIA','russian','RST')
insert into countries values(9,'AFGHANISTAN','afghani','AST')
insert into countries values(10,'NEPAL','nepalian','NST')
insert into countries values(11,'BHUTAN','bhutanian','BST')
insert into countries values(12,'UKRAINE','ukranine','UST')


create table states_child(
country_id int not null foreign key references countries,
stateid  int not null primary key,
statename varchar(50))
select * from states_child
select * from countries

insert into states_child values(6,11,'washington')
insert into states_child values(6,12,'boston')
insert into states_child values(6,13,'assam')
insert into states_child values(6,14,'madhya pradesh')
insert into states_child values(6,15,'sikim')

insert into states_child values(7,16,'kolkata')
insert into states_child values(7,17,'bihar')
insert into states_child values(7,18,'odisha')

insert into states_child values(8,19,'France')
insert into states_child values(8,20,'Queensland')
insert into states_child values(8,21,'Tasmania')

insert into states_child values(9,22,'Lahore')
insert into states_child values(9,23,'Riyadh')
insert into states_child values(9,24,'wales')

insert into states_child values(10,25,'chicago')
insert into states_child values(10,26,'maxico')
insert into states_child values(10,27,'boston')

insert into states_child values(7,28,'Sydney')
insert into states_child values(7,29,'Malaga')
insert into states_child values(7,30,'Biscay')

insert into states_child values(7,31,'Melbourne')
insert into states_child values(7,32,'canbera')
insert into states_child values(7,33,'brisbone')

create table cities_grandchild(
cityid int primary key,
cityname varchar(50),
stateid int foreign key references states_child)

drop table countries
select * from states_child
select * from countries
select * from cities_grandchild

insert into cities_grandchild values(1,'chennai',1)
insert into cities_grandchild values(2,'bengalore',1)
insert into cities_grandchild values(3,'bhadrak',1)
insert into cities_grandchild values(4,'sonapur',2)
insert into cities_grandchild values(5,'baleswar',2)
insert into cities_grandchild values(6,'cuttack',2)
insert into cities_grandchild values(7,'khorda',3)
insert into cities_grandchild values(8,'chennai',3)
insert into cities_grandchild values(9,'koraput',3)
insert into cities_grandchild values(10,'kalanha',4)
insert into cities_grandchild values(11,'kalimbnagar',1)
insert into cities_grandchild values(12,'chennai',4)
insert into cities_grandchild values(13,'balangir',4)
insert into cities_grandchild values(14,'keonjhar',5)
insert into cities_grandchild values(15,'athagarh',5)
insert into cities_grandchild values(16,'mak',6)
insert into cities_grandchild values(17,'guntur',6)

select * from states_child
select * from countries
select * from cities_grandchild
