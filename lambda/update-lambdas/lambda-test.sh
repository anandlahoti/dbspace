#!/bin/bash
#
# Requirements:
# - jq utility
# - aws cli
#
# Usage:
# ./lambda-test.sh -r 1.0.01 -b 2 -f lambda-config-qa.json

S3_BUCKET=

while getopts 'r:b:f:' opt; do
    case $opt in
        r)  RELEASE_VERSION="$OPTARG" ;;
        b)  BUILD_VERSION="$OPTARG" ;;
        f)  FILE_NAME="$OPTARG" ;;
        *)  exit 1            ;;
    esac
   done

NO_OF_ENTRIES=$(jq '. | length' ${FILE_NAME})

echo "Updating Lambda configurations ..."
for (( i=0; i<${NO_OF_ENTRIES}; i++)) 
do 
  LAMBDA_NAME=$(jq '.['$i'].FunctionName' ${FILE_NAME} | sed -e 's/^"//' -e 's/"$//')
  KMS_KEY='arn:aws:kms:ap-southeast-1:xxxxxxxxxxxx:key/xxxxxxxxxxxx'
  echo "Updating entry for $((1 + ${i})) lambda - ${LAMBDA_NAME}"
  jq '.['$i']' ${FILE_NAME} > /tmp/LAMBDA_$i.json
  aws lambda update-function-configuration --cli-input-json file:///tmp/LAMBDA_$i.json > /dev/null;
  aws lambda update-function-configuration --function-name ${LAMBDA_NAME} --kms-key-arn ${KMS_KEY} > /dev/null;
  if [ $? -eq 0 ]; then
    echo OK.Lambda configurations for ${LAMBDA_NAME} lambda are now updated.
  else
    echo FAIL.Cannot create json file for ${LAMBDA_NAME} lambda with id ${i}.
  fi  
done

echo "Uploading s3 artifacts for Lambdas.."
for (( i=0; i<${NO_OF_ENTRIES}; i++)) 
do
  LAMBDA_NAME=$(jq '.['$i'].FunctionName' ${FILE_NAME} | sed -e 's/^"//' -e 's/"$//')
  echo "Updating s3 code for $((1 + ${i})) lambda - ${LAMBDA_NAME}"
  if [[ $LAMBDA_NAME == 'AuthenticationQA' || $LAMBDA_NAME == 'Authentication' ]]; then
    S3_ARTIFACT='AUTHENTICATION'
    aws lambda update-function-code --function-name ${LAMBDA_NAME} --s3-bucket ${S3_BUCKET} --s3-key ${RELEASE_VERSION}/${S3_ARTIFACT}/${S3_ARTIFACT}-BUILD-${BUILD_VERSION}.zip > /dev/null;
  elif [[ $LAMBDA_NAME == 'xxxxxxxxxxxx' || $LAMBDA_NAME == 'TicTof' ]]; then
    S3_ARTIFACT='TIC_TOF'
    aws lambda update-function-code --function-name ${LAMBDA_NAME} --s3-bucket ${S3_BUCKET} --s3-key ${RELEASE_VERSION}/${S3_ARTIFACT}/${S3_ARTIFACT}-BUILD-${BUILD_VERSION}.zip > /dev/null;
  elif [[ $LAMBDA_NAME == 'xxxxxxxxxxxx' || $LAMBDA_NAME == 'xxxxxxxxxxxx' ]]; then
    S3_ARTIFACT='DATA_PROCESSOR'
    aws lambda update-function-code --function-name ${LAMBDA_NAME} --s3-bucket ${S3_BUCKET} --s3-key ${RELEASE_VERSION}/${S3_ARTIFACT}/${S3_ARTIFACT}-BUILD-${BUILD_VERSION}.zip > /dev/null;
  elif [[ $LAMBDA_NAME == 'xxxxxxxxxxxx' || $LAMBDA_NAME == 'xxxxxxxxxxxx' ]]; then
    S3_ARTIFACT='DATA_PROCESSOR'
    aws lambda update-function-code --function-name ${LAMBDA_NAME} --s3-bucket ${S3_BUCKET} --s3-key ${RELEASE_VERSION}/${S3_ARTIFACT}/${S3_ARTIFACT}-BUILD-${BUILD_VERSION}.zip > /dev/null;
  elif [[ $LAMBDA_NAME == 'xxxxxxxxxxxx' || $LAMBDA_NAME == 'xxxxxxxxxxxx' ]]; then
    S3_ARTIFACT='DATA_PROCESSOR'
    aws lambda update-function-code --function-name ${LAMBDA_NAME} --s3-bucket ${S3_BUCKET} --s3-key ${RELEASE_VERSION}/${S3_ARTIFACT}/${S3_ARTIFACT}-BUILD-${BUILD_VERSION}.zip > /dev/null;
  elif [[ $LAMBDA_NAME == 'xxxxxxxxxxxx' || $LAMBDA_NAME == 'xxxxxxxxxxxx' ]]; then
    S3_ARTIFACT='DATA_PROCESSOR'
    aws lambda update-function-code --function-name ${LAMBDA_NAME} --s3-bucket ${S3_BUCKET} --s3-key ${RELEASE_VERSION}/${S3_ARTIFACT}/${S3_ARTIFACT}-BUILD-${BUILD_VERSION}.zip > /dev/null;
  elif [[ $LAMBDA_NAME == 'xxxxxxxxxxxx' || $LAMBDA_NAME == 'xxxxxxxxxxxx' ]]; then
    S3_ARTIFACT='NOTIFICATION_DATA_PROCESSOR'
    aws lambda update-function-code --function-name ${LAMBDA_NAME} --s3-bucket ${S3_BUCKET} --s3-key ${RELEASE_VERSION}/${S3_ARTIFACT}/${S3_ARTIFACT}-BUILD-${BUILD_VERSION}.zip > /dev/null;
  elif [[ $LAMBDA_NAME == 'xxxxxxxxxxxx' || $LAMBDA_NAME == 'xxxxxxxxxxxx' ]]; then
    S3_ARTIFACT='REFERENCE_DATA'
    aws lambda update-function-code --function-name ${LAMBDA_NAME} --s3-bucket ${S3_BUCKET} --s3-key ${RELEASE_VERSION}/${S3_ARTIFACT}/${S3_ARTIFACT}-BUILD-${BUILD_VERSION}.zip > /dev/null;
  else
    echo "Fail to recognize the FunctionName. Please check your JSON File again."
  fi
  if [ $? -eq 0 ]; then
    echo OK.Code for ${LAMBDA_NAME} lambda is now updated from s3.
  else
    echo FAIL.Cannot update code from s3 for ${LAMBDA_NAME}.
  fi
done

if [[ $FILE_NAME == 'lambda-config-qa.json' ]]; then
    echo "Found $FILE_NAME - using QA Enviornment to update the triggers"
    aws events put-rule --name "xxxxxxxxxxxx" --schedule-expression "rate(5 minutes)"
    aws lambda add-permission --function-name xxxxxxxxxxxx --action 'lambda:InvokeFunction' --principal events.amazonaws.com --source-arn arn:aws:events:ap-southeast-1:xxxxxxxxxxxx:rule/xxxxxxxxxxxx --statement-id xxxxxxxxxxxx
    aws events put-targets --rule xxxxxxxxxxxx --targets "Id"="1","Arn"="arn:aws:lambda:ap-southeast-1:xxxxxxxxxxxx:function:xxxxxxxxxxxx"

    aws events put-rule --name "xxxxxxxxxxxx" --schedule-expression "rate(5 minutes)"
    aws lambda add-permission --function-name xxxxxxxxxxxx --action 'lambda:InvokeFunction' --principal events.amazonaws.com --source-arn arn:aws:lambda:ap-southeast-1:xxxxxxxxxxxx:function:xxxxxxxxxxxx --statement-id xxxxxxxxxxxx
    aws events put-targets --rule xxxxxxxxxxxx --targets "Id"="1","Arn"="arn:aws:lambda:ap-southeast-1:xxxxxxxxxxxx:function:xxxxxxxxxxxx"

    EVENT_SOURCE_MAPPING=$(aws lambda list-event-source-mappings --function-name xxxxxxxxxxxx)
    UUID=$(echo $EVENT_SOURCE_MAPPING | jq '.EventSourceMappings[].UUID' | sed -e 's/^"//' -e 's/"$//')
    ARRAYI=( $UUID )
    ENABLE_EVENT_SOURCE=$(aws lambda update-event-source-mapping --function-name xxxxxxxxxxxx --uuid $ID --enabled)
    
    echo "Enabled Kinesis Trigger for aw-data-processorQA - $ENABLE_EVENT_SOURCE"


elif [[ $FILE_NAME == 'lambda-config-dev.json' ]]; then
    echo "Found $FILE_NAME - using Dev Enviornment to update the triggers"
    
    aws events put-rule --name "xxxxxxxxxxxx" --schedule-expression "rate(5 minutes)"
    aws lambda add-permission --function-name xxxxxxxxxxxx --action 'lambda:InvokeFunction' --principal events.amazonaws.com --source-arn arn:aws:events:ap-southeast-1:xxxxxxxxxxxx:rule/xxxxxxxxxxxx --statement-id xxxxxxxxxxxx
    aws events put-targets --rule xxxxxxxxxxxx --targets "Id"="1","Arn"="arn:aws:lambda:ap-southeast-1:xxxxxxxxxxxx:function:xxxxxxxxxxxx"

    aws events put-rule --name "xxxxxxxxxxxx" --schedule-expression "rate(5 minutes)"
    aws lambda add-permission --function-name xxxxxxxxxxxx --action 'lambda:InvokeFunction' --principal events.amazonaws.com --source-arn arn:aws:lambda:ap-southeast-1:xxxxxxxxxxxx:function:xxxxxxxxxxxx --statement-id xxxxxxxxxxxx
    aws events put-targets --rule xxxxxxxxxxxx --targets "Id"="1","Arn"="arn:aws:lambda:ap-southeast-1:xxxxxxxxxxxx:function:xxxxxxxxxxxx"

    EVENT_SOURCE_MAPPING=$(aws lambda list-event-source-mappings --function-name xxxxxxxxxxxx)
    UUID=$(echo $EVENT_SOURCE_MAPPING | jq '.EventSourceMappings[].UUID' | sed -e 's/^"//' -e 's/"$//')
    ARRAYI=( $UUID )
    ENABLE_EVENT_SOURCE=$(aws lambda update-event-source-mapping --function-name xxxxxxxxxxxx --uuid $ID --enabled)
    
    echo "Enabled Kinesis Trigger for xxxxxxxxxxxx - $ENABLE_EVENT_SOURCE"
else
    echo "Fail to recognize the $FILE_NAME. Please check the name of JSON File again."
  fi
