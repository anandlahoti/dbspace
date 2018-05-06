#!/bin/bash
#--------------------------- 
# Usage:
#
# $SCRIPT -r 1.0.01 -f lambda/lambda-config-qa.json -e dev
#
# Pre-requisistes include:
# - aws cli
# - jq utility

while getopts 'r:f:e:' opt; do
    case $opt in
        r)  RELEASE_VERSION="$OPTARG" ;;
        f)  FILE_NAME="$OPTARG" ;;
        e)  ENV="$OPTARG" ;;    
        *)  exit 1            ;;
    esac
   done

RDS_MYSQL_NAME=xxxxx-${ENV}
AWS_ACCOUNT_ID=xxxxxx
AWS_REGION=xxxxx
POSTGRES_DB_NAME=xxxxxxxx
EC2_ID=xxxxxxxxx
S3_BUCKET1=xxxxx-${ENV}
S3_BUCKET2=xxxxxxxx-${ENV}
S3_BUCKET3=xxxxxx-${ENV}
S3_BUCKET4=xxxxxxx-${ENV}
S3_BUCKET5=xxxxxx-${ENV}

echo "Updating tags for all lambdas"

NO_OF_ENTRIES=$(jq '. | length' ${FILE_NAME})

for (( i=0; i<${NO_OF_ENTRIES}; i++)) 
do 
  LAMBDA_NAME=$(jq '.['$i'].FunctionName' ${FILE_NAME} | sed -e 's/^"//' -e 's/"$//')
  echo "Updating entry for $((1 + ${i})) lambda - ${LAMBDA_NAME}"  
  aws lambda tag-resource --resource arn:aws:lambda:${AWS_REGION}:${AWS_ACCOUNT_ID}:function:${LAMBDA_NAME} --tags '{"Version": "'${RELEASE_VERSION}'"}' > /dev/null;
  if [ $? -eq 0 ]; then
    echo OK.Tags for ${LAMBDA_NAME} lambda are now updated.
  else
    echo FAIL.Cannot add tags for ${LAMBDA_NAME} lambda with id ${i}.
  fi  
done

echo "Updating tags for Aurora MySQL"
aws rds add-tags-to-resource --resource-name arn:aws:rds:${AWS_REGION}:${AWS_ACCOUNT_ID}:db:${RDS_MYSQL_NAME} --tags Key=Version,Value=${RELEASE_VERSION}

if [ $? -eq 0 ]; then
  echo OK.Tags for ${RDS_MYSQL_NAME} lambda are now updated.
else
  echo FAIL.Cannot add tags for ${RDS_MYSQL_NAME}.
fi

echo "Updating tags for RDS Postgres"
aws rds add-tags-to-resource --resource-name arn:aws:rds:${AWS_REGION}:${AWS_ACCOUNT_ID}:db:${POSTGRES_DB_NAME} --tags Key=Version,Value=${RELEASE_VERSION}

if [ $? -eq 0 ]; then
  echo OK.Tags for ${POSTGRES_DB_NAME} lambda are now updated.
else
  echo FAIL.Cannot add tags for ${POSTGRES_DB_NAME}.
fi

echo "Updating tags for EC2"
aws ec2 create-tags --resources ${EC2_JAVA_CLIENT_ID} --tags Key=Version,Value=${RELEASE_VERSION}

if [ $? -eq 0 ]; then
  echo OK.Tags for ${EC2_JAVA_CLIENT_ID} are now updated.
else
  echo FAIL.Cannot add tags for ${EC2_JAVA_CLIENT_ID}.
fi

echo "Updating tags for S3"

aws s3api put-bucket-tagging --bucket ${S3_BUCKET1} --tagging 'TagSet=[{Key=Version,Value='${RELEASE_VERSION}'}]'
aws s3api put-bucket-tagging --bucket ${S3_BUCKET2} --tagging 'TagSet=[{Key=Version,Value='${RELEASE_VERSION}'}]'
aws s3api put-bucket-tagging --bucket ${S3_BUCKET3} --tagging 'TagSet=[{Key=Version,Value='${RELEASE_VERSION}'}]'
aws s3api put-bucket-tagging --bucket ${S3_BUCKET4} --tagging 'TagSet=[{Key=Version,Value='${RELEASE_VERSION}'}]'
aws s3api put-bucket-tagging --bucket ${S3_BUCKET5} --tagging 'TagSet=[{Key=Version,Value='${RELEASE_VERSION}'}]'

if [ $? -eq 0 ]; then
    echo OK.Tags for S3 buckets are now updated.
else
    echo FAIL.Cannot add tags for S3 buckets.
fi
