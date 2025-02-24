CREATE DATABASE Banking_Solutions_Database
GO

USE Banking_Solutions_Database
GO

-------------------------------------------------------------------------------------------
--TABLES FOR SAVING ACCOUNT
CREATE TABLE Saving_Account_Info
(	
ACCOUNT_NO VARCHAR(10) PRIMARY KEY,
ACCOUNT_HOLDER_NAME VARCHAR(100),
ACCOUNT_OPENING_DATE DATETIME,
ACCOUNT_TYPE VARCHAR(50),
PHONE_NUMBER VARCHAR(13),
EMAIL_ID VARCHAR(100),
INITIAL_AMOUNT MONEY
)
GO
CREATE TABLE Saving_Account_Transactions
(	
TRANSACTION_ID VARCHAR(40),
ACCOUNT_NO VARCHAR(10),
TRANSACTION_DATE DATETIME,
ACCOUNT_TYPE VARCHAR(50),
TRANSACTION_TYPE VARCHAR(50),
AMOUNT MONEY,
TOTAL_AMOUNT MONEY,
FOREIGN KEY(ACCOUNT_NO) REFERENCES Saving_Account_Info(ACCOUNT_NO)
)
GO
--TABLES FOR CURRENT ACCOUNT
CREATE TABLE Current_Account_Info
(	
ACCOUNT_NO VARCHAR(10) PRIMARY KEY,
ACCOUNT_HOLDER_NAME VARCHAR(100),
ACCOUNT_OPENING_DATE DATETIME,
ACCOUNT_TYPE VARCHAR(50),
PHONE_NUMBER VARCHAR(13),
EMAIL_ID VARCHAR(100),
INITIAL_AMOUNT MONEY
)
GO
CREATE TABLE Current_Account_Transactions
(	
TRANSACTION_ID VARCHAR(40),
ACCOUNT_NO VARCHAR(10) ,
TRANSACTION_DATE DATETIME,
ACCOUNT_TYPE VARCHAR(50),
TRANSACTION_TYPE VARCHAR(50),
AMOUNT MONEY,
TOTAL_AMOUNT MONEY,
FOREIGN KEY(ACCOUNT_NO) REFERENCES Current_Account_Info(ACCOUNT_NO)
)
GO
--TABLES FOR FD ACCOUNT
CREATE TABLE FD_Account_Info
(	
ACCOUNT_NO VARCHAR(10) PRIMARY KEY,
ACCOUNT_HOLDER_NAME VARCHAR(100),
ACCOUNT_OPENING_DATE DATETIME,
ACCOUNT_TYPE VARCHAR(50),
PHONE_NUMBER VARCHAR(13),
EMAIL_ID VARCHAR(100),
INITIAL_AMOUNT MONEY
)
GO
CREATE TABLE FD_Account_Transactions
(	
TRANSACTION_ID VARCHAR(40),
ACCOUNT_NO VARCHAR(10) ,
TRANSACTION_DATE DATETIME,
ACCOUNT_TYPE VARCHAR(50),
TRANSACTION_TYPE VARCHAR(50),
AMOUNT MONEY,
TOTAL_AMOUNT MONEY,
FOREIGN KEY(ACCOUNT_NO) REFERENCES FD_Account_Info(ACCOUNT_NO)
)
GO
--TABLES FOR RECURRING ACCOUNT
CREATE TABLE Recurring_Account_Info
(	
ACCOUNT_NO VARCHAR(10) PRIMARY KEY,
ACCOUNT_HOLDER_NAME VARCHAR(100),
ACCOUNT_OPENING_DATE DATETIME,
ACCOUNT_TYPE VARCHAR(50),
PHONE_NUMBER VARCHAR(13),
EMAIL_ID VARCHAR(100),
INITIAL_AMOUNT MONEY
)
GO
CREATE TABLE Recurring_Account_Transactions
(
TRANSACTION_ID VARCHAR(40),
ACCOUNT_NO VARCHAR(10) ,
TRANSACTION_DATE DATETIME,
ACCOUNT_TYPE VARCHAR(50),
TRANSACTION_TYPE VARCHAR(50),
AMOUNT MONEY,
TOTAL_AMOUNT MONEY,
FOREIGN KEY(ACCOUNT_NO) REFERENCES Recurring_Account_Info(ACCOUNT_NO)
)
GO

-------------------------------------------------------------------------------------------
--STORED PROCEDURE FOR INSERT CURRENT_ACCOUNT_INFO VALUES
CREATE PROCEDURE sp_insert_current_account_info
		@accountno VARCHAR(10),
		@acc_holder_name varchar(50),
		@acc_opening_date datetime,
		@acc_type varchar(20),
		@phoneno varchar(30),
		@emailid varchar(100),
		@initialamount money
AS
BEGIN
	INSERT INTO Current_Account_Info(ACCOUNT_NO, ACCOUNT_HOLDER_NAME, ACCOUNT_OPENING_DATE, ACCOUNT_TYPE, PHONE_NUMBER, EMAIL_ID, INITIAL_AMOUNT)
	VALUES(@accountno, @acc_holder_name, @acc_opening_date, @acc_type, @phoneno, @emailid, @initialamount)
END
GO
--STORED PROCEDURE FOR INSERT SAVING_ACCOUNT_INFO VALUES
CREATE PROCEDURE sp_insert_saving_account_info
		@accountno varchar(10),
		@acc_holder_name varchar(50),
		@acc_opening_date datetime,
		@acc_type varchar(20),
		@phoneno varchar(30),
		@emailid varchar(100),
		@initialamount money
AS
BEGIN
	INSERT INTO Saving_Account_Info(ACCOUNT_NO, ACCOUNT_HOLDER_NAME, ACCOUNT_OPENING_DATE, ACCOUNT_TYPE, PHONE_NUMBER, EMAIL_ID, INITIAL_AMOUNT)
	VALUES(@accountno, @acc_holder_name, @acc_opening_date, @acc_type, @phoneno, @emailid, @initialamount)
END
GO
--STORED PROCEDURE FOR INSERT FD_ACCOUNT_INFO VALUES
CREATE PROCEDURE sp_insert_FD_account_info
		@accountno varchar(10),
		@acc_holder_name varchar(50),
		@acc_opening_date datetime,
		@acc_type varchar(20),
		@phoneno varchar(30),
		@emailid varchar(100),
		@initialamount money
AS
BEGIN
	INSERT INTO FD_Account_Info(ACCOUNT_NO, ACCOUNT_HOLDER_NAME, ACCOUNT_OPENING_DATE, ACCOUNT_TYPE, PHONE_NUMBER, EMAIL_ID, INITIAL_AMOUNT)
	VALUES(@accountno, @acc_holder_name, @acc_opening_date, @acc_type, @phoneno, @emailid, @initialamount)
END
GO
--STORED PROCEDURE FOR INSERT RECURRING_ACCOUNT_INFO VALUES
CREATE PROCEDURE sp_insert_Recurring_account_info
		@accountno varchar(10),
		@acc_holder_name varchar(50),
		@acc_opening_date datetime,
		@acc_type varchar(20),
		@phoneno varchar(30),
		@emailid varchar(100),
		@initialamount money
AS
BEGIN
	INSERT INTO Recurring_Account_Info(ACCOUNT_NO, ACCOUNT_HOLDER_NAME, ACCOUNT_OPENING_DATE, ACCOUNT_TYPE, PHONE_NUMBER, EMAIL_ID, INITIAL_AMOUNT)
	VALUES(@accountno, @acc_holder_name, @acc_opening_date, @acc_type, @phoneno, @emailid, @initialamount)
END
GO

-------------------------------------------------------------------------------------------
--STORED PROCEDURE FOR INSERT SAVING_ACCOUNT_TRANSACTION VALUES
CREATE PROCEDURE sp_insert_saving_account_transaction
		@transactionid varchar(40),
		@accountno varchar(10),
		@transaction_date datetime,
		@acc_type varchar(20),
		@transaction_type varchar(20),
		@amount money,
		@totalamount money
AS
BEGIN
	INSERT INTO Saving_Account_Transactions(TRANSACTION_ID, ACCOUNT_NO, TRANSACTION_DATE, ACCOUNT_TYPE, TRANSACTION_TYPE, AMOUNT, TOTAL_AMOUNT)
	VALUES(@transactionid, @accountno, @transaction_date, @acc_type, @transaction_type, @amount, @totalamount)
END
GO
--STORED PROCEDURE FOR INSERT CURRENT_ACCOUNT_TRANSACTION VALUES
CREATE PROCEDURE sp_insert_current_account_transaction
		@transaction_id varchar(40),
		@accountno varchar(10),
		@transaction_date datetime,
		@acc_type varchar(20),
		@transaction_type varchar(20),
		@amount money,
		@totalamount money
AS
BEGIN
	INSERT INTO Current_Account_Transactions(TRANSACTION_ID, ACCOUNT_NO, TRANSACTION_DATE, ACCOUNT_TYPE, TRANSACTION_TYPE, AMOUNT, TOTAL_AMOUNT)
	VALUES(@transaction_id, @accountno, @transaction_date, @acc_type, @transaction_type, @amount, @totalamount)
END
GO
--STORED PROCEDURE FOR INSERT FD_ACCOUNT_TRANSACTION VALUES
CREATE PROCEDURE sp_insert_FD_account_transaction
		@transaction_id varchar(40),
		@accountno varchar(10),
		@transaction_date datetime,
		@acc_type varchar(20),
		@transaction_type varchar(20),
		@amount money,
		@totalamount money
AS
BEGIN
	INSERT INTO FD_Account_Transactions(TRANSACTION_ID, ACCOUNT_NO, TRANSACTION_DATE, ACCOUNT_TYPE, TRANSACTION_TYPE, AMOUNT, TOTAL_AMOUNT)
	VALUES(@transaction_id, @accountno, @transaction_date, @acc_type, @transaction_type, @amount, @totalamount)
END
GO
--STORED PROCEDURE FOR INSERT Recurring_ACCOUNT_TRANSACTION VALUES
CREATE PROCEDURE sp_insert_Recurring_account_transaction
		@transaction_id varchar(40),
		@accountno varchar(10),
		@transaction_date datetime,
		@acc_type varchar(20),
		@transaction_type varchar(20),
		@amount money,
		@totalamount money
AS
BEGIN
	INSERT INTO Recurring_Account_Transactions(TRANSACTION_ID, ACCOUNT_NO, TRANSACTION_DATE, ACCOUNT_TYPE, TRANSACTION_TYPE, AMOUNT, TOTAL_AMOUNT)
	VALUES(@transaction_id, @accountno, @transaction_date, @acc_type, @transaction_type, @amount, @totalamount)
END
GO

-------------------------------------------------------------------------------------------
--STORED PROCEDURE FOR GENERATING FOR FETCHING MAX_ACCOUNT_ID OF SAVING ACCOUNT
CREATE PROCEDURE sp_SA_max_account_id
AS
BEGIN
	SELECT MAX(ACCOUNT_NO) FROM Saving_Account_Info
END
GO
--STORED PROCEDURE FOR GENERATING FOR FETCHING MAX_ACCOUNT_ID OF CURRENT ACCOUNT
CREATE PROCEDURE sp_CA_max_account_id
AS
BEGIN
	SELECT MAX(ACCOUNT_NO) FROM Current_Account_Info
END
GO
--STORED PROCEDURE FOR GENERATING FOR FETCHING MAX_ACCOUNT_ID OF FD ACCOUNT
CREATE PROCEDURE sp_FD_max_account_id
AS
BEGIN
	SELECT MAX(ACCOUNT_NO) FROM FD_Account_Info
END
GO
--STORED PROCEDURE FOR GENERATING FOR FETCHING MAX_ACCOUNT_ID OF RECURRING ACCOUNT
CREATE PROCEDURE sp_Recurring_max_account_id
AS
BEGIN
	SELECT MAX(ACCOUNT_NO) FROM Recurring_Account_Info
END
GO

-------------------------------------------------------------------------------------------
--STORED PROCEDURE FOR CALCULATING DEPOSIT AMOUNT USING LAST AMOUNT OF THE USER(ACCOUNT_ID)
CREATE PROCEDURE sp_fetch_last_saving_acc_amount
		@accountno varchar(10) 
AS
BEGIN
	SELECT TOTAL_AMOUNT FROM Saving_Account_Transactions
	WHERE ACCOUNT_NO=@accountno
	ORDER BY TRANSACTION_DATE DESC
END
GO
CREATE PROCEDURE sp_fetch_last_current_acc_amount
		@accountno varchar(10)
AS
BEGIN
	SELECT TOTAL_AMOUNT FROM Current_Account_Transactions
	WHERE ACCOUNT_NO=@accountno
	ORDER BY TRANSACTION_DATE DESC
END
GO
CREATE PROCEDURE sp_fetch_last_FD_acc_amount
		@accountno varchar(10)
AS
BEGIN
	SELECT TOTAL_AMOUNT FROM FD_Account_Transactions
	WHERE ACCOUNT_NO=@accountno
	ORDER BY TRANSACTION_DATE DESC
END
GO
CREATE PROCEDURE sp_fetch_last_Recurring_acc_amount
		@accountno varchar(10)
AS
BEGIN
	SELECT TOTAL_AMOUNT FROM Recurring_Account_Transactions
	WHERE ACCOUNT_NO=@accountno
	ORDER BY TRANSACTION_DATE DESC
END
GO

-------------------------------------------------------------------------------------------
--STORED PROCEDURE FOR FETCHING ALL DETAILS FROM SAVING ACCOUNT
CREATE PROCEDURE sp_fetchall_savingacc_details
		@accountno varchar(10)
AS
BEGIN
	SELECT ACCOUNT_NO, ACCOUNT_HOLDER_NAME, ACCOUNT_OPENING_DATE, ACCOUNT_TYPE, PHONE_NUMBER, EMAIL_ID, INITIAL_AMOUNT 
	FROM Saving_Account_Info
	WHERE ACCOUNT_NO=@accountno
END
GO
--STORED PROCEDURE FOR FETCHING ALL DETAILS FROM CURRENT ACCOUNT
CREATE PROCEDURE sp_fetchall_currentacc_details
		@accountno varchar(10)
AS
BEGIN
	SELECT ACCOUNT_NO, ACCOUNT_HOLDER_NAME, ACCOUNT_OPENING_DATE, ACCOUNT_TYPE, PHONE_NUMBER, EMAIL_ID, INITIAL_AMOUNT 
	FROM Current_Account_Info
	WHERE ACCOUNT_NO=@accountno
END
GO
--STORED PROCEDURE FOR FETCHING ALL DETAILS FROM FD ACCOUNT
CREATE PROCEDURE sp_fetchall_FDacc_details
		@accountno varchar(10)
AS
BEGIN
	SELECT ACCOUNT_NO, ACCOUNT_HOLDER_NAME, ACCOUNT_OPENING_DATE, ACCOUNT_TYPE, PHONE_NUMBER, EMAIL_ID, INITIAL_AMOUNT 
	FROM FD_Account_Info
	WHERE ACCOUNT_NO=@accountno
END
GO
--STORED PROCEDURE FOR FETCHING ALL DETAILS FROM RECURRING ACCOUNT
CREATE PROCEDURE sp_fetchall_Recurringacc_details
		@accountno varchar(10)
AS
BEGIN
	SELECT ACCOUNT_NO, ACCOUNT_HOLDER_NAME, ACCOUNT_OPENING_DATE, ACCOUNT_TYPE, PHONE_NUMBER, EMAIL_ID, INITIAL_AMOUNT 
	FROM Recurring_Account_Info
	WHERE ACCOUNT_NO=@accountno
END
GO

-------------------------------------------------------------------------------------------
-- SP FOR FETCHING ALL THE RECORDS FROM SAVING ACCOUNT TRANSACTION TABLE
CREATE PROCEDURE sp_fetchall_saving_account_transaction
		@accountno varchar(10)
AS 
BEGIN
	SELECT TRANSACTION_ID, TRANSACTION_DATE, TRANSACTION_TYPE, AMOUNT FROM Saving_Account_Transactions
	WHERE ACCOUNT_NO=@accountno
END
GO
-- SP FOR FETCHING ALL THE RECORDS FROM CURRENT ACCOUNT TRANSACTION TABLE
CREATE PROCEDURE sp_fetchall_current_account_transaction
		@accountno varchar(10)
AS 
BEGIN
	SELECT TRANSACTION_ID,TRANSACTION_DATE, TRANSACTION_TYPE, AMOUNT FROM Current_Account_Transactions
	WHERE ACCOUNT_NO=@accountno
END
GO
-- SP FOR FETCHING ALL THE RECORDS FROM FD ACCOUNT TRANSACTION TABLE
CREATE PROCEDURE sp_fetchall_FD_account_transaction
		@accountno varchar(10)
AS 
BEGIN
	SELECT TRANSACTION_ID,TRANSACTION_DATE, TRANSACTION_TYPE, AMOUNT FROM FD_Account_Transactions
	WHERE ACCOUNT_NO=@accountno
END
GO
-- SP FOR FETCHING ALL THE RECORDS FROM RECURRING ACCOUNT TRANSACTION TABLE
CREATE PROCEDURE sp_fetchall_Recurring_account_transaction
		@accountno varchar(10)
AS 
BEGIN
	SELECT TRANSACTION_ID, TRANSACTION_DATE, TRANSACTION_TYPE, AMOUNT FROM Recurring_Account_Transactions
	WHERE ACCOUNT_NO=@accountno
END
GO

-------------------------------------------------------------------------------------------
-- SP FOR DELETE THE DATA FROM SAVING ACCOUNT AS WELL AS FROM THE SAVING TRANSACTION INFO
CREATE PROCEDURE sp_saving_account_delete_data
		@accountno varchar(10)
AS
BEGIN
	DELETE FROM Saving_Account_Info WHERE ACCOUNT_NO=@accountno
END
GO
CREATE PROCEDURE sp_saving_account_transaction_delete_data
		@accountno varchar(10)
AS
BEGIN
	DELETE FROM Saving_Account_Transactions WHERE ACCOUNT_NO=@accountno
END
GO
-- SP FOR DELETE THE DATA FROM CURRENT ACCOUNT AS WELL AS FROM THE SAVING TRANSACTION INFO
CREATE PROCEDURE sp_current_account_delete_data
		@accountno varchar(10)
AS
BEGIN
	DELETE FROM Current_Account_Info WHERE ACCOUNT_NO=@accountno
END
GO
CREATE PROCEDURE sp_current_account_transaction_delete_data
		@accountno varchar(10)
AS
BEGIN
	DELETE FROM Current_Account_Transactions WHERE ACCOUNT_NO=@accountno
END
GO
-- SP FOR DELETE THE DATA FROM CURRENT ACCOUNT AS WELL AS FROM THE SAVING TRANSACTION INFO
CREATE PROCEDURE sp_FD_account_delete_data
		@accountno varchar(10)
AS
BEGIN
	DELETE FROM FD_Account_Info WHERE ACCOUNT_NO=@accountno
END
GO
CREATE PROCEDURE sp_FD_account_transaction_delete_data
		@accountno varchar(10)
AS
BEGIN
	DELETE FROM FD_Account_Transactions WHERE ACCOUNT_NO=@accountno
END
GO
-- SP FOR DELETE THE DATA FROM CURRENT ACCOUNT AS WELL AS FROM THE RECURRING TRANSACTION INFO
CREATE PROCEDURE sp_Recurring_account_delete_data
		@accountno varchar(10)
AS
BEGIN
	DELETE FROM Recurring_Account_Info WHERE ACCOUNT_NO=@accountno
END
GO
CREATE PROCEDURE sp_Recurring_account_transaction_delete_data
		@accountno varchar(10)
AS
BEGIN
	DELETE FROM Recurring_Account_Transactions WHERE ACCOUNT_NO=@accountno
END
GO

-------------------------------------------------------------------------------------------
-- SP for data updation
CREATE PROCEDURE sp_saving_account_data_updation 
    @accountno varchar(10),
    @column_name VARCHAR(40), 
    @column_value SQL_VARIANT
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    DECLARE @column_value_converted NVARCHAR(MAX);  -- Declare a variable to store the converted value

    -- Convert the column value to NVARCHAR(MAX) explicitly (or VARCHAR, depending on your needs)
    SET @column_value_converted = CONVERT(NVARCHAR(MAX), @column_value);

    -- Constructing the dynamic SQL string
    SET @sql = 'UPDATE Saving_Account_Info ' +
               'SET ' + QUOTENAME(@column_name) + ' = @column_value ' +  -- Use QUOTENAME for column name
               'WHERE ACCOUNT_NO = @accountno';  -- Properly handle the account number with parameterized query

    -- Execute the dynamic SQL with proper parameter binding
    EXEC sp_executesql @sql, 
                       N'@column_value NVARCHAR(MAX), @accountno varchar(10)',  -- Declare parameters for execution
                       @column_value_converted, @accountno;  -- Pass the converted value
END
GO
CREATE PROCEDURE sp_Current_account_data_updation 
    @accountno varchar(10),
    @column_name VARCHAR(40), 
    @column_value SQL_VARIANT
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    DECLARE @column_value_converted NVARCHAR(MAX);  -- Declare a variable to store the converted value

    -- Convert the column value to NVARCHAR(MAX) explicitly (or VARCHAR, depending on your needs)
    SET @column_value_converted = CONVERT(NVARCHAR(MAX), @column_value);

    -- Constructing the dynamic SQL string
    SET @sql = 'UPDATE Current_Account_Info ' +
               'SET ' + QUOTENAME(@column_name) + ' = @column_value ' +  -- Use QUOTENAME for column name
               'WHERE ACCOUNT_NO = @accountno';  -- Properly handle the account number with parameterized query

    -- Execute the dynamic SQL with proper parameter binding
    EXEC sp_executesql @sql, 
                       N'@column_value NVARCHAR(MAX), @accountno varchar(10)',  -- Declare parameters for execution
                       @column_value_converted, @accountno;  -- Pass the converted value
END
GO
CREATE PROCEDURE sp_FD_account_data_updation 
    @accountno varchar(10),
    @column_name VARCHAR(40), 
    @column_value SQL_VARIANT
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    DECLARE @column_value_converted NVARCHAR(MAX);  -- Declare a variable to store the converted value

    -- Convert the column value to NVARCHAR(MAX) explicitly (or VARCHAR, depending on your needs)
    SET @column_value_converted = CONVERT(NVARCHAR(MAX), @column_value);

    -- Constructing the dynamic SQL string
    SET @sql = 'UPDATE FD_Account_Info ' +
               'SET ' + QUOTENAME(@column_name) + ' = @column_value ' +  -- Use QUOTENAME for column name
               'WHERE ACCOUNT_NO = @accountno';  -- Properly handle the account number with parameterized query

    -- Execute the dynamic SQL with proper parameter binding
    EXEC sp_executesql @sql, 
                       N'@column_value NVARCHAR(MAX), @accountno varchar(10)',  -- Declare parameters for execution
                       @column_value_converted, @accountno;  -- Pass the converted value
END
GO
CREATE PROCEDURE sp_Recurring_account_data_updation 
    @accountno varchar(10),
    @column_name VARCHAR(40), 
    @column_value SQL_VARIANT
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    DECLARE @column_value_converted NVARCHAR(MAX);  -- Declare a variable to store the converted value

    -- Convert the column value to NVARCHAR(MAX) explicitly (or VARCHAR, depending on your needs)
    SET @column_value_converted = CONVERT(NVARCHAR(MAX), @column_value);

    -- Constructing the dynamic SQL string
    SET @sql = 'UPDATE Recurring_Account_Info ' +
               'SET ' + QUOTENAME(@column_name) + ' = @column_value ' +  -- Use QUOTENAME for column name
               'WHERE ACCOUNT_NO = @accountno';  -- Properly handle the account number with parameterized query

    -- Execute the dynamic SQL with proper parameter binding
    EXEC sp_executesql @sql, 
                       N'@column_value NVARCHAR(MAX), @accountno varchar(10)',  -- Declare parameters for execution
                       @column_value_converted, @accountno;  -- Pass the converted value
END
GO

-------------------------------------------------------------------------------------------
SELECT * FROM Saving_Account_Info
GO
SELECT * FROM Current_Account_Info
GO
SELECT * FROM FD_Account_Info
GO
SELECT * FROM Recurring_Account_Info
GO
SELECT * FROM Saving_Account_Transactions
GO
SELECT * FROM Current_Account_Transactions
GO
SELECT * FROM FD_Account_Transactions
GO
SELECT * FROM Recurring_Account_Transactions
GO
/**
DELETE FROM Saving_Account_Info
GO
DELETE FROM Saving_Account_Transactions
GO
DELETE FROM Current_Account_Info
GO
DELETE FROM Current_Account_Transactions
GO
DELETE FROM FD_Account_Info
GO
DELETE FROM FD_Account_Transactions
GO
DELETE FROM Recurring_Account_Info
GO
DELETE FROM Recurring_Account_Transactions
GO
**/