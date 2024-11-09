import logging
import os
from datetime import datetime

# Generate log file name based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory if it doesn't exist
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Complete path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Corrected syntax here
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Corrected format
    level=logging.INFO,  # Added missing equals sign and logging level
)

if __name__=="__main__":
    logging.info("Logging has started.")
                                      