# Describe Table
\d+ table_name

# List Tables
\d

# Alter table with a change in datatype for a column
ALTER table table_name
ALTER COLUMN COLUMN1 type DATATYPE;

# Add column in postgres
ALTER table table_name
ADD COLUMN COLUMN_NAME DATATYPE;
