# Simple csv file grep row for a particular entry

cat xxxx.csv | grep '173460'

# Sort according to date in second column
# -t is for the delimiter

cat xxxx.csv | grep '173460' | sort -t"," -k2

# Sample date filter

2017-12-01
2017-12-02
.
.
.
2017-12-31

# Print only 6th and 7th column in a csv
# Use man awk in bash
# awk -F denotes delimeter to be used
# $1 = Column 1
# $2 = Column 2
....

cat xxxx.csv | grep '173460' | sort -t"," -k2 | awk -F"," '{print $6 $7}'

# Compare $1/$2/$3 ... with $1/$2/$3/ ...
# Not equal to(!=), equal to (==)
cat xxxx.csv | grep '173460' | sort -t"," -k2 | awk -F" " '$2 != $4'

# Replace symbols/characters with other symbols/characters
# Replace " with space
tr '"' " "

