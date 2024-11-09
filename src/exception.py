import sys
import logging
import os
from datetime import datetime

# Generate log file name based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory if it doesn't exist
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # Ensure directory is created

# Complete path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging to log to a file
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Log file path
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def error_message_detail(error, error_detail: sys):
    """
    This function captures details of the error, including the file name and line number where the error occurred.
    """
    _, _, exc_tb = error_detail.exc_info()  # Get the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name
    error_message = "Error occurred in python script name [{0}] on line number [{1}] with error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom exception class to capture the error message and details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        String representation of the custom error message.
        """
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a divide-by-zero exception
    except Exception as e:  # Capture the exception object
        custom_exc = CustomException(e, sys)
        logging.error(str(custom_exc))  # Log the custom exception to the log file
