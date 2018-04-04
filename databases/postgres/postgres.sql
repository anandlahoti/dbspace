# Commands to be run from pgsql

# COPY CSV DATA FROM CSV FILE to Postgres table
COPY swipedata(COLUMN1, COLUMN2, ... COLUMN*) FROM '/var/lib/pgsql/data/<NAME-OF-CSV-FILE>.csv' DELIMITER '|' CSV HEADER;

# Count No. of Rows in a table
SELECT count(*) FROM table_name;

# DROP Column from Postgres
ALTER TABLE table_name DROP COLUMN column_name;

# Get top 3 entries from table_name
SELECT * FROM table_name LIMIT 3 OFFSET 1
