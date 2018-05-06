#!/usr/bin/env bash
#
# Requirements:
# mysql cli
# redis-cli
# awscli
#
#
# Cleaning up data from S3, elasticache and RDS for testing purposes
#---------------------------------------------------------------------------------------
# Example: $SCRIPT -c all -e qa # For deleting data from all resources
# $SCRIPT -c s3 -e qa # For Deleting data from S3
# $SCRIPT -c rds -e qa # For deleting data from RDS MySQL
# $SCRIPT -c elasticache -e qa # For deleting data from Elasticache
    
  while getopts 'c:e:' opt; do
  case $opt in
        c)  RESOURCE="$OPTARG" ;;
        e)  ENV="$OPTARG" ;;
        *)  exit 1            ;;
    esac
  done

  MYSQL_ENDPOINT= xxxxxxxxxxx-${ENV}.xxxxxxxxxx.rds.amazonaws.com
  MYSQL_USERNAME=xxxxx
  MYSQL_PASSWORD=xxxxxxxx
  MYSQL_DB=wipro
  
  REDIS_ENDPOINT=xxxxxxxxx-${ENV}.xxxxxxxxxx.cache.amazonaws.com
  REDIS_PORT=6379
  REDIS_PASSWORD=xxxxxxx
  

   echo "Starting the script ... "
   if [[ $RESOURCE == all ]]; then                 
   echo  "Starting to clean data from S3, RDS and elasticache . . ."
   printf 'Cleaning all'

   aws s3 rm s3://xxxxxxxx-${ENV} --recursive > /dev/null;
   aws s3 rm s3://xxxxxxxxx-${ENV} --recursive > /dev/null;
   aws s3 rm s3://xxxxxxxxx-${ENV} --recursive > /dev/null;
   aws s3 rm s3://xxxxxxxxxx-${ENV} --recursive > /dev/null;    

   mysql -h ${MYSQL_ENDPOINT}  -u ${MYSQL_USERNAME} -p${MYSQL_PASSWORD} -D ${MYSQL_DB} -e "delete from xxxx;delete from xxxxxxx;delete from xxxxxxxxx;delete from xxxxxxx;delete from xxxxxx;" > /dev/null;  

   redis-cli -h ${REDIS_ENDPOINT} -p ${REDIS_PORT} -a ${REDIS_PASSWORD} flushdb > /dev/null;
   
   printf 'Cleaning All Resources Completed\n'

   elif [[ $RESOURCE == S3 ]]; then 
   printf "Cleaning S3"
  
   aws s3 rm s3://xxxxxx-${ENV} --recursive > /dev/null;
   aws s3 rm s3://xxxxxxxxx-${ENV} --recursive > /dev/null;
   aws s3 rm s3://xxxxxxx-${ENV} --recursive > /dev/null;
   aws s3 rm s3://xxxxxxx-${ENV} --recursive > /dev/null;

   printf "Cleaning S3 completed\n"
   elif [[ $RESOURCE == RDS ]]; then
   printf "Cleaning RDS MySql"

   mysql -h ${MYSQL_ENDPOINT}  -u ${MYSQL_USERNAME} -p${MYSQL_PASSWORD} -D ${MYSQL_DB} -e "delete from xxxx;delete from xxxxx;delete from xxxxxxx;delete from xxxx;delete from xxxxxx;" > /dev/null;

   printf "Cleaning RDS MySql Completed\n"

   elif [[ $RESOURCE == elasticache ]]; then
   printf "Cleaning Elasticache"

   redis-cli -h ${REDIS_ENDPOINT} -p ${REDIS_PORT} -a ${REDIS_PASSWORD} flushdb > /dev/null;

   printf "Cleaning Elasticache Completed\n"
   else
    echo "Invalid Input"
    exit 1
   fi
