"""Dao for Endpoint1."""
import pymysql
import redis
from aurora_client import AuroraClient
from util.redis_utility import RedisUtility
from util.logger_utility import LoggerUtility


class EndPoint1Dao():
    """Dao for Mapping table."""

    def save_data(self, body):
        """Save Data to Aurora."""
        aurora_client = AuroraClient()
        connection = aurora_client.create_connection()
        with connection.cursor() as cursor:
            try:
                keys = ", ".join(str(key) for key in list(body.keys()))
                values = str(list(body.values()))[1:-1]
                query = "INSERT INTO TABLE1 ({}) VALUES ({})".format(keys, values)
                LoggerUtility.log_info(query)
                cursor.execute(query)
                connection.commit()
                EndPoint1Dao.save_data_redis(self, body)
                LoggerUtility.log_info("Data inserted successfully")
            except pymysql.InternalError as exception:
                LoggerUtility.log_error(exception)
                connection.rollback()
                return False
            # Close Connectionto Aurora/RDS
            finally:
                try:
                    if connection is not None:
                        connection.close()
                except Exception as exception:
                    LoggerUtility.log_error(exception)
            return True

    def save_data_redis(self, body):
        """Save Info to Redis."""
        try:
            redis_utility = RedisUtility()
            key1_value = body['KEY1']            
            key2_value = body['KEY2']
            key3_value = body['KEY3']
            value_redis = {"KEY2": "" + key2_value, "KEY3": "" + key3_value}
            redis_utility.set_json_value(key1_value, value_redis)
            LoggerUtility.log_info("Data inserted in redis successfully")
            return True
        except redis.ConnectionError as exception:
            LoggerUtility.log_error(exception)
            return False
