# Based on PostgreSQL 
# Connect using Psql. Ref - https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-from-psql.html
# Ref - https://docs.aws.amazon.com/redshift/latest/dg/c_SQL_commands.html

# Export to a single csv file by using parallel off

# MAXFILESIZE AS max-size [ MB | GB ]
-- The maximum size of files UNLOAD creates in Amazon S3. 
-- The default unit is MB.
-- If MAXFILESIZE is not specified, the default maximum file size is 6.2 GB. 
-- Ref - (https://docs.aws.amazon.com/redshift/latest/dg/r_UNLOAD.html)

unload ('select * from table_name')
to 's3://mybucket/.../.../table_name_' credentials 
'aws_access_key_id=<access-key-id>;aws_secret_access_key=<secret-access-key>'
parallel off;

# Using Gzip, to make that file even smaller for download

unload ('select * from table_name')
to 's3://mybucket/.../.../table_name_' credentials 
'aws_access_key_id=<access-key-id>;aws_secret_access_key=<secret-access-key>'
parallel off
gzip;
