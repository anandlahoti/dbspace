"""Utility module for Aurora client."""
import os
import pymysql
from util.logger_utility import LoggerUtility
from util.common_constants import EnvironmentVariables, Constants


class RDSUtility:
    """Utility for RDS connections."""

    @staticmethod
    def create_connection():
        """Create connection to RDS."""
        try:
            port_no = int(os.environ[EnvironmentVariables.RDS_DB_PORT_ENV_VAR])
        except KeyError as key_error:
            # Use default port if environment variable is not set
            LoggerUtility.log_warning(str(key_error) + " not configured, using default port!")
            port_no = Constants.RDS_AURORA_DEFAULT_PORT_NO
        try:
            rds_connection = pymysql.connect(
                host=os.environ[EnvironmentVariables.RDS_DB_ENDPOINT_ENV_VAR],
                user=os.environ[EnvironmentVariables.RDS_DB_USER_ENV_VAR],
                passwd=os.environ[EnvironmentVariables.RDS_DB_PASSWORD_ENV_VAR],
                db=os.environ[EnvironmentVariables.RDS_DB_NAME_ENV_VAR],
                port=port_no,
                connect_timeout=10,
                cursorclass=pymysql.cursors.DictCursor
            )
            return rds_connection
        except pymysql.InternalError as connection_error:
            LoggerUtility.log_error(str(connection_error))
            LoggerUtility.log_error("FATAL: Failed to create connection to RDS!")

    @staticmethod
    def close_connection(sql_connection):
        """Close connection to RDS."""
        sql_connection.close()

    @staticmethod
    def get_data_from_rds(sql_connection, sql_query):
        """Fetch data from RDS."""
        query_result = {}
        try:
            with sql_connection.cursor() as cursor:
                cursor.execute(sql_query)
                # Only for fetching all values
                query_result = cursor.fetchall()
                # Use cursor.commit() for making commiting changes to RDS
            LoggerUtility.log_info("Database transaction successful!")
        except Exception as transaction_error:
            LoggerUtility.log_error("Failed to perform database transaction: " + str(transaction_error))
        return query_result
