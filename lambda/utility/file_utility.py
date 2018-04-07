"""Module for file operations."""
from util.logger_utility import LoggerUtility
from util.common_constants import Constants
from util.time_utility import TimeUtility


class FileUtility:
    """Class to perform file operations."""

    @staticmethod
    def create_csv_file_from_list(raw_data_list):
        """Create csv file at run-time from a list."""
        file_name = TimeUtility.get_current_time() + Constants.FILE_EXTENSION_CSV
        file_path = Constants.FILE_IO_BASE_PATH + file_name
        file_handler = open(file_path, "w+")
        for data in raw_data_list:
            file_handler.write("%s\n" % data)
        LoggerUtility.log_debug("File created successfully: " + file_path)
        return file_path
