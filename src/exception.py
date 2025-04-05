# the code to handle exceptions

import sys # this will have all the exceptions information
from src.logger import logging # this will have the logging information 
def error_message_details(error, error_details:sys):
    """
    error: Exception object
    error_details: sys module to get the exception details
    exc_tb: traceback object to get the details of the exception
    """
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message
    

# if __name__ == "__main__":
#     # Test the logging
#     try:
#         # Simulate an error
#         1 / 0
#     except Exception as e:
#         logging.info("Division by zero error")
#         # Log the error message
#         raise CustomException(e, sys)

# this is a custom exception class helpful to call the error message
# and the error details
# Q1 Why we used self in __init__ method?
# ans __init__ method is a constructor method in Python. It is used to initialize the attributes of the class when an object is created. The self parameter refers to the instance of the class itself, allowing us to access its attributes and methods.