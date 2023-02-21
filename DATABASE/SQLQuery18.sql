create table employee13(
employeeid integer not null identity(1,1),
employeename varchar(50),
employeeaddress varchar(50),
monthsalary  numeric(10,2),
primary key clustered (employeeid)
)

	CREATE TABLE EmployeesAudit
    (
      AuditID INTEGER NOT NULL IDENTITY(1, 1) ,
      EmployeeID INTEGER ,
      EmployeeName VARCHAR(50) ,
      EmployeeAddress VARCHAR(50) ,
      MonthSalary NUMERIC(10, 2) ,
      ModifiedBy VARCHAR(128) ,
      ModifiedDate DATETIME ,
      Operation VARCHAR(20) 
      PRIMARY KEY CLUSTERED ( AuditID )
    )
---------------------------------------------------------------
	INSERT INTO dbo.Employee13
        ( EmployeeName ,
          EmployeeAddress ,
          MonthSalary
        )
SELECT 'Mahi Dhoni', 'Ranchi', 10000
UNION ALL
SELECT 'SACHIN TENDULKAR', 'MUMBAI', 10000
UNION ALL
SELECT 'VIRAT KOHLI', 'NEW DELHI', 10000
UNION ALL
SELECT 'VVS LAXMAN', 'CHENNAI', 10000
-----------------------------------------------
select * from EmployeesAudit
select * from employee13
Truncate Table EmployeesAudit
------------------------------------

CREATE TABLE Employee14
    (
      EmployeeID integer NOT NULL IDENTITY(1, 1) ,
      EmployeeName VARCHAR(50) ,
      EmployeeAddress VARCHAR(50) ,
      MonthSalary NUMERIC(10, 2),
      PRIMARY KEY CLUSTERED (EmployeeID)
    )
-------------------------------------------------------------
	CREATE TABLE EmployeesAudit3
    (
      AuditID INTEGER NOT NULL IDENTITY(1, 1) ,
      EmployeeID INTEGER ,
      EmployeeName VARCHAR(50) ,
      EmployeeAddress VARCHAR(50) ,
      MonthSalary NUMERIC(10, 2) ,
      ModifiedBy VARCHAR(128) ,
      ModifiedDate DATETIME ,
      Operation VARCHAR(20) 
      PRIMARY KEY CLUSTERED ( AuditID )
    )

--------------------------------------------------------------------------------
--FORM 1 : DML TRIGGER FOR INSERT STATEMENT

	alter TRIGGER TR_Employees_INSERT ON dbo.Employee14
    FOR INSERT
AS
BEGIN
   SELECT * FROM INSERTED 
   SELECT * FROM DELETED

   PRINT ' TRIGGER TR_Audit_Employees_INSERT AUTOMATICALLY TRIGGERED'

   IF EXISTS ( SELECT * FROM Inserted )
                BEGIN
                    INSERT  INTO dbo.EmployeesAudit3
                            ( EmployeeID ,
                              EmployeeName ,
                              EmployeeAddress ,
                              MonthSalary ,
                              ModifiedBy ,
                              ModifiedDate ,
                              Operation
                            )
                            SELECT  I.EmployeeID ,
                                    I.EmployeeName ,
                                    I.EmployeeAddress ,
                                    I.MonthSalary ,
                                    'Manish' ,
                                     GETDATE() ,
                                    'INSERT'
                            FROM    INSERTED I
                END


END

Insert into Employee14 Values ('Sachin','Mumbai',1000000)
Insert into Employee14 Values ('Mahi','Ranchi',1000000)
Insert into Employee14 Values ('Kohli','Delhi',1000000)
Insert into Employee14 Values ('Ashwin','Chennai',1000000)



---------------------------------------------------------------------------------------------
	INSERT INTO dbo.Employee14
        ( EmployeeName ,
          EmployeeAddress ,
          MonthSalary
        )
SELECT 'Mahi Dhoni', 'Ranchi', 10000
UNION ALL
SELECT 'SACHIN TENDULKAR', 'MUMBAI', 10000
UNION ALL
SELECT 'VIRAT KOHLI', 'NEW DELHI', 10000
UNION ALL
SELECT 'VVS LAXMAN', 'CHENNAI', 10000
------------------------------------------------------------------------------------------
select * from Employee14
select * from EmployeesAudit3
-----------------------------------------------------------------------------------------------------
--FORM 2 : DML TRIGGER FOR UPDATE STATEMENT

CREATE OR ALTER TRIGGER TR_Employees_UPDATE ON dbo.Employee14
    FOR UPDATE
AS
BEGIN
   SELECT * FROM INSERTED
   SELECT * FROM DELETED

   IF EXISTS ( SELECT * FROM DELETED )
                BEGIN
                    INSERT  INTO dbo.EmployeesAudit3
                            ( EmployeeID ,
                              EmployeeName ,
                              EmployeeAddress ,
                              MonthSalary ,
                              ModifiedBy ,
                              ModifiedDate ,
                              Operation
                            )
                            SELECT  I.EmployeeID ,
                                    I.EmployeeName ,
                                    I.EmployeeAddress ,
                                    I.MonthSalary ,
                                    'Manish' ,
                                    GETDATE() ,
                                    'UPDATE'
                            FROM    inserted I
                END


END
-------------------------------------------------------------------
Update Employee14 Set EmployeeName = 'God Of Cricket' where EmployeeID =7
select * from Employee14
select * from EmployeesAudit3
--------------------------------------------------------------------------------
--FORM 3 : DML TRIGGER FOR DELETE STATEMENT
CREATE OR ALTER TRIGGER TR_Employees_DELETE ON dbo.Employee14
    FOR DELETE
AS
BEGIN
   SELECT * FROM INSERTED
   SELECT * FROM DELETED

   IF EXISTS ( SELECT * FROM DELETED )
                BEGIN
                    INSERT  INTO dbo.EmployeesAudit3
                            ( EmployeeID ,
                              EmployeeName ,
                              EmployeeAddress ,
                              MonthSalary ,
                              ModifiedBy ,
                              ModifiedDate ,
                              Operation
                            )
                            SELECT  D.EmployeeID ,
                                    D.EmployeeName ,
                                    D.EmployeeAddress ,
                                    D.MonthSalary ,
                                    '' ,
                                    GETDATE() ,
                                    'DELETE'
                            FROM    DELETED D
                END


END
-------------------------------------------------------------------------------
Delete from Employee14 where EmployeeID = 6
select * from Employee14
select * from EmployeesAudit3
--------------------------------------------------------------------------------------------------
---------FORM 4 : DML TRIGGER FOR UPDATE ,INSERT ,DELETE STATEMENT

 ALTER TRIGGER TR_Audit_Employees ON dbo.Employee14
    FOR INSERT, UPDATE, DELETE
AS
BEGIN
    DECLARE @login_name VARCHAR(128)
 
    SELECT  @login_name = login_name
    FROM    sys.dm_exec_sessions
    WHERE   session_id = @@SPID

DECLARE @OPERATION VARCHAR(20)
DECLARE @I INT
DECLARE @D INT
SET @I = (SELECT COUNT(*) FROM INSERTED)
SET @D = (SELECT COUNT(*) FROM DELETED)
SELECT @I AS INSERTED, @D AS DELETED

 
    IF ( (@I>@D) AND (@I>0) )  -- INSERT OPERATION
    BEGIN
            
                    INSERT  INTO dbo.EmployeesAudit3
                            ( EmployeeID ,
                              EmployeeName ,
                              EmployeeAddress ,
                              MonthSalary ,
                              ModifiedBy ,
                              ModifiedDate ,
                              Operation
                            )
                            SELECT  I.EmployeeID ,
                                    I.EmployeeName ,
                                    I.EmployeeAddress ,
                                    I.MonthSalary ,
                                    @login_name ,
                                    GETDATE() ,
                                    'INSERT'
                            FROM    INSERTED I
       END      
       ELSE IF( (@I>0) AND (@D>0) ) --UPDATE
       BEGIN
                    INSERT  INTO dbo.EmployeesAudit3
                            ( EmployeeID ,
                              EmployeeName ,
                              EmployeeAddress ,
                              MonthSalary ,
                              ModifiedBy ,
                              ModifiedDate ,
                              Operation
                            )
                            SELECT  D.EmployeeID ,
                                    D.EmployeeName ,
                                    D.EmployeeAddress ,
                                    D.MonthSalary ,
                                    @login_name ,
                                    GETDATE() ,
                                    'UPDATE'
                            FROM    Deleted D
        END  
        ELSE  --DELETE 
        BEGIN
            INSERT  INTO dbo.EmployeesAudit3
                    ( EmployeeID ,
                      EmployeeName ,
                      EmployeeAddress ,
                      MonthSalary ,
                      ModifiedBy ,
                      ModifiedDate ,
                      Operation
                    )
                    SELECT  D.EmployeeID ,
                            D.EmployeeName ,
                            D.EmployeeAddress ,
                            D.MonthSalary ,
                            @login_name ,
                            GETDATE() ,
                            'DELETE'
                    FROM    DELETED D
        END
END

--------------------------------------------------------------------------------------
Insert into Employee14 Values ('Sachin','Mumbai',1000000)
Insert into Employee14 Values ('Mahi','Ranchi',1000000)
Insert into Employee14 Values ('Kohli','Delhi',1000000)
Insert into Employee14 Values ('Ashwin','Chennai',1000000)

Update Employee14 Set EmployeeName = 'God Of Cricket' where EmployeeID =17
select * from Employee14
select * from EmployeesAudit3

Delete from Employee14 where EmployeeID = 18
select * from Employee14
select * from EmployeesAudit3

------------------------------------------------------------------------------------------------------------------------------------------

----Triggers on ddl commands
CREATE TABLE TABLE_AUDIT_LOG (
    log_id INT IDENTITY PRIMARY KEY,
    event_data XML NOT NULL,
    changed_by SYSNAME NOT NULL
);
GO

CREATE OR ALTER TRIGGER trg_TABLE_changes ON DATABASE
FOR
    CREATE_TABLE,
    ALTER_TABLE, 
    DROP_TABLE
AS
BEGIN
    SET NOCOUNT ON;
PRINT 'DDL TRIGGER trg_TABLE_changes CALLED'
    INSERT INTO TABLE_AUDIT_LOG (
        event_data,
        changed_by
    )
    VALUES (
        EVENTDATA(),
        USER
    );
END;
Drop Table Test1


GO
CREATE TABLE TEST1
(
  ID INT,
  FN VARCHAR(10)
)

GO

SELECT * FROM TABLE_AUDIT_LOG
