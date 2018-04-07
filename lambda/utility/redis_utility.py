"""Utility module for redis cache operations."""
import os
import json
import redis
from utility.logger_utility import LoggerUtility
from utility.common_constants import EnvironmentVariables, Constants


class RedisUtility:
    """Class to perform redis cache operations."""

    __redis_client = None

    def __init__(self):
        """Class constructor."""
        try:
            port_no = int(os.environ[EnvironmentVariables.ELASTICACHE_REDIS_PORT_ENV_VAR])
        except KeyError as port_not_configured:
            # Use default port if environment variable is not set
            LoggerUtility.log_warning(str(port_not_configured) + " not configured, using default port!")
            port_no = Constants.REDIS_CACHE_DEFAULT_PORT_NO
        self.__redis_client = redis.StrictRedis(host=os.environ[EnvironmentVariables.ELASTICACHE_REDIS_ENDPOINT_ENV_VAR], port=port_no, db=0)

    def set_value(self, key, value):
        """Set string value against a key in cache."""
        self.__redis_client.set(key, value)

    def get_value(self, key):
        """Fetch string value against a key in cache."""
        cached_value = self.__redis_client.get(key)
        if cached_value is None:
            return None
        return cached_value

    def set_json_value(self, key, value):
        """Set json string against a key in cache."""
        self.__redis_client.set(key, json.dumps(value))

    def get_json_value(self, key):
        """Fetch json string value against a key in cache."""
        cached_value = self.__redis_client.get(key)
        if cached_value is None:
            return None
        return json.loads(cached_value)

    def delete_key(self, key):
        """Delete object from cache."""
        self.__redis_client.delete(key)

    def set_expiry_on_key(self, key, ttl_seconds):
        """Set object expiry in cache."""
        self.__redis_client.expire(key, ttl_seconds)
