/* TO SHOW STATUS of the DB */
SHOW ENGINE INNODB STATUS

/* To Display no. of threads we are running*/
SHOW PROCESSLIST

/*Change Column Name */
ALTER TABLE TABLE_NAME CHANGE `oldname` `newname` decimal(NEW-DATA-TYPE)

/*Obtain Stored Values in a TABLE*/
SELECT * FROM TABLE_NAME

/* Show the no. of Columns in a table and its data types */
DESCRIBE EMP_METADATA

-- Drop PRIMARY Key
ALTER TABLE TABLE_NAME DROP PRIMARY KEY

-- List Primary Key in a table
SHOW index from TABLE_NAME where Key_name = 'PRIMARY'

-- Create Composite Key in a table
ALTER TABLE TABLE_NAME ADD PRIMARY KEY (COLUMN1, COLUMN2)

/*Get value from a particular column using a entry made in different column*/
SELECT COLUMN1 FROM TABLE_NAME WHERE COLUMN2='23'

-- Inserting multiple values in a table
-- Note the differnt single quotes used in the query
INSERT INTO `TABLE1` (`COLUMN1`,`COLUMN2`,`COLUMN3`,`COLUMN4`) VALUES ('VALUE1','VALUE2','VALUE3','VALUE4')

-- CREATE TABLE
create table table_name(COLUMN1 int,COLUMN2 text,COLUMN3 text)

-- ALTER COLUMN TYPE
ALTER TABLE tablename MODIFY columnname INTEGER;

-- ADD Column after another column
ALTER table tablename Add COLUMN COLUMN1 varchar(500) AFTER COLUMN2

-- Modify column to accept null values
alter table tablename MODIFY COLUMN COLUMN1 VARCHAR(50) NULL
