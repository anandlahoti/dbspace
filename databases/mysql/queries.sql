# TO SHOW STATUS of the DB
SHOW ENGINE INNODB STATUS

# TO Display no. of threads we are running
SHOW PROCESSLIST

# Change Column Name
ALTER TABLE TABLE_NAME CHANGE `oldname` `newname` decimal(NEW-DATA-TYPE)

#Obtain Stored Values in a TABLE
SELECT * FROM TABLE_NAME

# Show the no. of Columns in a table and its data types
DESCRIBE EMP_METADATA

# Drop PRIMARY Key
ALTER TABLE TABLE_NAME DROP PRIMARY KEY

# List Primary Key in a table
SHOW index from TABLE_NAME where Key_name = 'PRIMARY'

# Create Composite Key in a table
ALTER TABLE TABLE_NAME ADD PRIMARY KEY (COLUMN1, COLUMN2)
