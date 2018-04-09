# Commands to be run from pgsql
# Use pv utility always while copies
# For pv utility, Ref - http://www.ivarch.com/programs/pv.shtml

# Local machine setup
# COPY CSV DATA FROM CSV FILE to Postgres table
COPY swipedata(COLUMN1, COLUMN2, ... COLUMN*) FROM '/var/lib/pgsql/data/<NAME-OF-CSV-FILE>.csv' DELIMITER '|' CSV HEADER;

# Remotely copy csv file to new location of postgres
psql -h <HOSTNAME> -d <DB-NAME> -U <USER> -c "\copy mytable (column1, column2)  from '/path/to/local/file.csv' with delimiter as ','"

# Count No. of Rows in a table
SELECT count(*) FROM table_name;

# DROP Column from Postgres
ALTER TABLE table_name DROP COLUMN column_name;

# Get top 3 entries from table_name
SELECT * FROM table_name LIMIT 3 OFFSET 1

# Create new table and store output from a current table into it
CREATE TABLE new_table_name AS
SELECT t.* FROM old_table_name t JOIN new_record_ids r ON(r.id = t.id);

# Export select query output into a external csv file
Copy (Select * From table_name) To '/tmp/test.csv' With CSV DELIMITER ',';

# Drop multiple columns in a table
ALTER TABLE table_name DROP COLUMN col1, DROP COLUMN col2;

# Replace values in a column in a table
UPDATE <table-name> SET <COLUMN-NAME> = replace(<COLUMN-NAME>, 'old-text', 'new-text')

-- Ref - http://sqlfiddle.com/#!15/e345e
