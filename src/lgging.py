import logging

# Configure the logging settings
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
def divide_numbers(x, y):
    try:
        result = x / y
        logging.info(f"Division result: {result}")
    except ZeroDivisionError:
        logging.error("Cannot divide by zero!")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")

# Using the function
divide_numbers(10, 2)
divide_numbers(10, 0)
