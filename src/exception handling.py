def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError as te:
        print(f"Error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("This will always be executed.")

# Example 1: Valid division
divide_numbers(10, 2)

# Example 2: Division by zero
divide_numbers(10, 0)

# Example 3: Type error
divide_numbers(10, '2')

# Example 4: Custom exception
class MyCustomError(Exception):
    pass

def raise_custom_exception():
    try:
        raise MyCustomError("This is a custom exception.")
    except MyCustomError as e:
        print(f"Caught a custom exception: {e}")
    finally:
        print("This will always be executed.")

raise_custom_exception()
