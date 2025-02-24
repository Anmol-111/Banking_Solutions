CREATE DATABASE BankApplication
GO
USE BankApplication
GO
CREATE TABLE NEW_SAVING_ACCOUNT_DETAILS(
ACCOUNT_NO INT NOT NULL PRIMARY KEY,
ACCOUNT_HOLDER_NAME VARCHAR(50) NOT NULL,
ACCOUNT_OPENING_DATE DATE NOT NULL,
ACCOUNT_TYPE VARCHAR(50) NOT NULL,
INITIAL_AMOUNT MONEY NOT NULL
)
GO
create PROCEDURE sp_newsavingaccount_data 
				@account_no int,
				@name varchar(50),
				@date date,
				@acc_type varchar(50),
				@amount money
AS
BEGIN
		INSERT INTO NEW_SAVING_ACCOUNT_DETAILS(ACCOUNT_NO, ACCOUNT_HOLDER_NAME, ACCOUNT_OPENING_DATE, ACCOUNT_TYPE, INITIAL_AMOUNT) 
		VALUES(@account_no, @name, @date, @acc_type, @amount)
END
GO

EXEC sp_newsavingaccount_data 11111, 'Anmol Prakash', '2024-12-23', 'SAVING', 10000000
GO

SELECT * FROM NEW_SAVING_ACCOUNT_DETAILS
GO
USE BankApplication
GO
CREATE PROCEDURE sp_account_verifying
				 @account_no int
AS
BEGIN
		SELECT * FROM NEW_SAVING_ACCOUNT_DETAILS
		WHERE ACCOUNT_NO=@account_no
END
GO

EXEC sp_account_verifying 11111
GO

ALTER PROCEDURE sp_last_account_no 
AS
BEGIN
		SELECT MAX(ACCOUNT_NO) FROM NEW_SAVING_ACCOUNT_DETAILS
END
GO

EXEC sp_last_account_no

DELETE FROM NEW_SAVING_ACCOUNT_DETAILS WHERE ACCOUNT_NO>11111
GO
USE BankApplication
GO
CREATE PROCEDURE sp_delete_data
		@account_no int
AS
BEGIN
		DELETE FROM NEW_SAVING_ACCOUNT_DETAILS WHERE ACCOUNT_NO=@account_no
END
GO

CREATE PROCEDURE sp_update_data
		@account_no int,
		@account_holder_name varchar(50)
AS
BEGIN
		UPDATE NEW_SAVING_ACCOUNT_DETAILS
		SET ACCOUNT_HOLDER_NAME=@account_holder_name
		WHERE ACCOUNT_NO=@account_no
END
GO

