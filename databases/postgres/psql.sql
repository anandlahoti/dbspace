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

# Export Table to JSON
\t
\a
\o file.json
SELECT row_to_json(r) FROM table_name AS r;

# Check the file using
# cat file.json on local system
