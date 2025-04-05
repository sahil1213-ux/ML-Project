# The code to logging and it is used to track the logs of all executions that are happening in the project and it is helpful to track the errors and exceptions that are happening in the project.
# # The logging module in Python is a built-in module that provides a flexible framework for emitting log messages from Python programs. It is used to track events that happen when the software runs, so you can see what happened and when.
# # The logging module is part of the Python standard library, so you don't need to install anything extra to use it.
# it creates a log file in the logs directory and it will create a log file with the name of the current date and time and it will log all the information in that file.

import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(LOG_DIR,exist_ok=True) 

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)
# # Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='a',
    format='[%(asctime)s ] - %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
)

# if __name__ == "__main__":
#     # Test the logging
#     logging.info("Logging is working")

# so whenever you execute, A new log file in logs folder will be created with the name of the current date and time and it will log all the information in that file.
