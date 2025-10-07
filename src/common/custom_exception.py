import sys


class CustomException(Exception):
    """
    Custom Exception class that provides detailed error information
    including message, original exception, file name, and line number.
    """

    def __init__(self, message: str, error_detail: Exception = None):
        """
        Initialize the CustomException with a message and optional error details.
        """
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        """
        Generate a detailed error message with traceback information.
        """
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return (
            f"{message} | Error: {error_detail} | "
            f"File: {file_name} | Line: {line_number}"
        )

    def __str__(self):
        """
        Return the formatted error message when the exception is printed.
        """
        return self.error_message
