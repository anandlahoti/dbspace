"""Utility module for time operations."""
import datetime
from dateutil import tz
from utility.common_constants import SomeConstants


class TimeUtility:
    """Utility class for time operations."""

    @staticmethod
    def get_current_time():
        """Get current time in UTC."""
        return datetime.datetime.utcnow().isoformat()

    @staticmethod
    def get_current_date():
        """Get current date in Asia/Calcutta."""
        current_utc_timestamp = datetime.datetime.utcnow()
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('Asia/Calcutta')
        current_utc_timestamp = current_utc_timestamp.replace(tzinfo=from_zone)
        return current_utc_timestamp.astimezone(to_zone).date().strftime("%Y-%m-%d")

    @staticmethod
    def is_timestamp_for_today(timestamp):
        """Check if timestamp is for current date."""
        received_timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        current_date = datetime.datetime.today().strftime("%Y-%m-%d")
        from_zone = tz.gettz('Asia/Calcutta')
        to_zone = tz.gettz('UTC')
        # Set time zone for both datetime objects
        received_timestamp = received_timestamp.replace(tzinfo=from_zone)
        # Convert the received timestamp to UTC
        received_timestamp_utc_date = received_timestamp.astimezone(to_zone).date()
        return str(received_timestamp_utc_date) == str(current_date)

    @staticmethod
    def is_current_time_ahead(time_string):
        """Check if received timestamp value has crossed the current time."""
        received_timestamp = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        current_timestamp = datetime.datetime.now()
        from_zone = tz.gettz('Asia/Calcutta')
        to_zone = tz.gettz('UTC')
        # Set time zone for both datetime objects
        received_timestamp = received_timestamp.replace(tzinfo=from_zone)
        current_timestamp = current_timestamp.replace(tzinfo=to_zone)
        # Convert the received timestamp to UTC
        received_timestamp_utc = received_timestamp.astimezone(to_zone)
        # Compate both timestamp to check if current time is ahead of received timestamp
        latest_timestamp = max((received_timestamp_utc, current_timestamp))
        return latest_timestamp == current_timestamp

    @staticmethod
    def is_timestamp_within_window(start_time, end_time, time_to_check):
        """Check if timestamp is within shift cutoff window."""
        start_timestamp = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_timestamp = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        time_to_check_timestamp = datetime.datetime.strptime(time_to_check, "%Y-%m-%d %H:%M:%S")
        return start_timestamp <= time_to_check_timestamp <= end_timestamp

    @staticmethod
    def get_duration_between_timestamps(start_time, end_time):
        """Calculate duration between two timestamps."""
        from_zone = tz.gettz('Asia/Calcutta')
        start_timestamp = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_timestamp = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        start_timestamp = start_timestamp.replace(tzinfo=from_zone)
        end_timestamp = end_timestamp.replace(tzinfo=from_zone)
        return round((end_timestamp - start_timestamp).seconds / 3600, 2)

    @staticmethod
    def get_elapsed_days(start_date, end_date):
        """Calculate duration between two dates in days."""
        start_date_object = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date_object = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        return (end_date_object - start_date_object).days

    @staticmethod
    def get_date_n_days_ago(given_date, n_days):
        """Get 'n' days older date."""
        current_date_object = datetime.datetime.strptime(given_date, "%Y-%m-%d")
        return (current_date_object - datetime.timedelta(days=n_days)).strftime("%Y-%m-%d")

    @staticmethod
    def get_date_from_timestamp(timestamp):
        """Get date from timestamp."""
        date_object = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
        return date_object.strftime("%Y-%m-%d")

    @staticmethod
    def get_week_year_from_date(given_date):
        """Get week number and year number from date."""
        from_date_object = datetime.datetime.strptime(given_date, "%Y-%m-%d")
        week_number = from_date_object.isocalendar()[1]
        year = from_date_object.year
        return week_number, year

    @staticmethod
    def get_elapsed_minutes(start_timestamp, end_timestamp):
        """Calculate duration between two timestamps in minutes."""
        start_timestamp_object = datetime.datetime.strptime(start_timestamp, "%Y-%m-%dT%H:%M:%S.%f")
        end_timestamp_object = datetime.datetime.strptime(end_timestamp, "%Y-%m-%dT%H:%M:%S.%f")
        return (end_timestamp_object - start_timestamp_object).seconds / 60

    @staticmethod
    def convert_str_to_date(str_date):
        """Convert string to date."""
        date = datetime.datetime.strptime(str_date, SomeConstants.DATE_FORMAT)
        return date

    @staticmethod
    def get_hour_and_minute(date):
        """Get hour and minute from datetime date."""
        return date.strftime("%H.%m")
