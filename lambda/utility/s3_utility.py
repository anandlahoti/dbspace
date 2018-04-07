"""Module for S3 operations."""
import json
import boto3
import botocore
from utility.logger_utility import LoggerUtility
from utility.common_constants import ReferenceKeys


class S3Utility:
    """Class to perform S3 operations."""

    @staticmethod
    def upload_file_object(file_path, bucket_name, object_name):
        """Upload file object to S3."""
        s3_client = boto3.client(ReferenceKeys.S3_REFERENCE)
        with open(file_path, 'rb') as file_content:
            s3_client.upload_fileobj(file_content, bucket_name, object_name)
        LoggerUtility.log_debug("File upload to " + bucket_name + " bucket completed. File name: " + object_name)

    @staticmethod
    def put_object(data_object, bucket_name, object_name):
        """Upload data object to S3."""
        s3_client = boto3.client(ReferenceKeys.S3_REFERENCE)
        # Using Put Object.Another option is to use download file/upload file from boto3
        s3_client.put_object(Body=str(data_object).encode(), Bucket=bucket_name, Key=object_name)
        LoggerUtility.log_debug("Put object on S3 completed: " + object_name)

    @staticmethod
    def check_if_file_present(s3_file_path, bucket_name):
        """Check if file exist or not."""
        s3_client = boto3.client(ReferenceKeys.S3_REFERENCE)
        list_object = s3_client.list_objects(Bucket=bucket_name, Prefix=s3_file_path)
        file_exists = False
        if 'Contents' in list_object:
            file_exists = True
        return file_exists

    @staticmethod
    def download_file_from_s3(s3_file_path, bucket_name):
        """Download file from s3 ."""
        s3_client = boto3.client(ReferenceKeys.S3_REFERENCE)
        # Using file path in lambda under tmp directory
        filepath = '/tmp/' + 'file1.json'
        try:
            s3_client.download_file(bucket_name, s3_file_path, filepath)
            LoggerUtility.log_info("File downloaded from S3 completed: " + s3_file_path)
            return filepath
        except botocore.exceptions.ClientError as client_error:
            if client_error.response['Error']['Code'] == "404":
                LoggerUtility.log_error("The object does not exist.")
            else:
                raise Exception("FATAL: " + str(client_error) + " not found!")

    @staticmethod
    def put_json_object_to_s3(data_object, s3_file_path, bucket_name):
        """Upload the updated file to back S3."""
        s3_client = boto3.resource(ReferenceKeys.S3_REFERENCE)
        s3_client.Bucket(bucket_name).put_object(Body=json.dumps(data_object), Bucket=bucket_name, Key=s3_file_path)
        LoggerUtility.log_debug("Put object to S3 completed: " + s3_file_path)

    @staticmethod
    def list_objects(bucket_name, object_prefix):
        """List all objects inside S3 bucket."""
        s3_client = boto3.client(ReferenceKeys.S3_REFERENCE)
        bucket_objects = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=object_prefix)
        if ReferenceKeys.CONTENTS_REFERENCE in bucket_objects:
            LoggerUtility.log_debug("Found '" + str(len(bucket_objects)) + "' objects in bucket!")
            return bucket_objects[ReferenceKeys.CONTENTS_REFERENCE]
        return []

    @staticmethod
    def read_object(bucket_name, object_key):
        """Read object from S3 bucket."""
        s3_resource = boto3.resource(ReferenceKeys.S3_REFERENCE)
        s3_object = s3_resource.Object(bucket_name, object_key)
        return s3_object.get()[ReferenceKeys.BODY_REFERENCE].read().decode(ReferenceKeys.UTF_ENCODING_REFERENCE)

    @staticmethod
    def delete_objects(bucket_name, object_list):
        """Delete objects from S3 bucket from an object list."""
        s3_delete_object_list = []
        for s3_key in object_list:
            s3_delete_object_list.append({ReferenceKeys.KEY_REFERENCE: s3_key})
        s3_client = boto3.client(ReferenceKeys.S3_REFERENCE)
        deletion_response = s3_client.delete_objects(
            Bucket=bucket_name,
            Delete={
                ReferenceKeys.OBJECTS_REFERENCE: s3_delete_object_list
            }
        )
        if 'Deleted' in deletion_response:
            LoggerUtility.log_debug("Deleted '" + str(len(deletion_response['Deleted'])) + "' objects from '" + bucket_name + "' bucket successfully!")
        else:
            LoggerUtility.log_debug("Deleted '" + str(s3_delete_object_list[0]) + "' object from '" + bucket_name + "' bucket successfully!")
        if 'Errors' in deletion_response:
            LoggerUtility.log_warning("Failed to delete '" + str(len(deletion_response['Errors'])) + "' objects from '" + bucket_name + "' bucket!")
