"""Common constants module."""


class Constants:
    """General constants class."""

    LOGGER_NAME = 'application'
    DEFAULT_LOG_LEVEL = 'INFO'
    VALID_IO_STATUS_VALUES = [
        'timein',
        'timeout'
    ]

    # Notification Constants
    MESSAGE_REFERENCE = 'message'
    TOADDRESSES_REFERENCE = 'ToAddresses'
    CCADDRESSES_REFERENCE = 'CcAddresses'
    BODY_REFERENCE = 'Body'
    HTML_TEMPLATE = 'email_template.html'
    SUBJECT_REFERENCE = 'Subject'
    SES_MAIL_CHARSET = 'UTF-8'
    RECORDS_REFERENCE = "Records"
    SNS_REFERENCE = "Sns"
    SNS_MSG_REFERENCE = "Message"
    SNS_MSG_SUBJECT = "Notification message"
    SNS_TOPIC = "sns_topic"

    FILE_IO_BASE_PATH = '/tmp/'
    FILE_EXTENSION_CSV = '.csv'
    FILE_EXTENSION_JSON = '.json'
    RDS_AURORA_DEFAULT_PORT_NO = 3306
    REDIS_CACHE_DEFAULT_PORT_NO = 6379

    def __setattr__(self, attr, value):
        """Restrict editing constant values."""
        if hasattr(self, attr):
            raise Exception("Attempting to alter read-only value")

        self.__dict__[attr] = value


class BotoConstants:
    """Set boto constants."""

    # Notifications constants
    BOTO_CLIENT_AWS_SES = "ses"
    BOTO_CLIENT_AWS_SNS = "sns"

    def __setattr__(self, attr, value):
        """Set attributes."""
        if hasattr(self, attr):
            raise Exception("Attempting to alter read-only value")

        self.__dict__[attr] = value


class ReferenceKeys:
    """Reference key constants class."""

    RECORDS_REFERENCE = 'Records'
    KINESIS_REFERENCE = 'kinesis'
    DATA_REFERENCE = 'data'
    S3_REFERENCE = 's3'
    UTF_ENCODING_REFERENCE = 'utf-8'
    DATE_REFERENCE = 'DATE'
    TIMESTAMP_REFERENCE = 'TIMESTAMP'
    STATUS_REFERENCE = 'STATUS'
    CONTENTS_REFERENCE = 'Contents'
    KEY_REFERENCE = 'Key'
    BODY_REFERENCE = 'Body'
    OBJECTS_REFERENCE = 'Objects'
    OBJECT_REFERENCE = 'object'
    BUCKET_REFERENCE = 'bucket'
    NAME_REFERENCE = 'name'

    def __setattr__(self, attr, value):
        """Restrict editing constant values."""
        if hasattr(self, attr):
            raise Exception("Attempting to alter read-only value")

        self.__dict__[attr] = value


class EnvironmentVariables:
    """Environment variables constants class."""

    ELASTICACHE_REDIS_ENDPOINT_ENV_VAR = 'REDIS_ENDPOINT'
    ELASTICACHE_REDIS_PORT_ENV_VAR = 'REDIS_PORT_NO'
    LOG_LEVEL = 'LOG_LEVEL'
    RDS_DB_ENDPOINT_ENV_VAR = 'RDS_DB_ENDPOINT'
    RDS_DB_USER_ENV_VAR = 'RDS_DB_USERNAME'
    RDS_DB_PASSWORD_ENV_VAR = 'RDS_DB_PASSWORD'
    RDS_DB_PORT_ENV_VAR = 'RDS_DB_PORT_NO'
    RDS_DB_NAME_ENV_VAR = 'RDS_DB_NAME'

    def __setattr__(self, attr, value):
        """Restrict editing constant values."""
        if hasattr(self, attr):
            raise Exception("Attempting to alter read-only value")

        self.__dict__[attr] = value


class SomeConstants:
    """Some values constant class."""
    
    DATE_FORMAT = "%Y-%m-%d"
    FROM_DATE_REFERENCE = "fromdate"
    TO_DATE_REFERENCE = "todate"
