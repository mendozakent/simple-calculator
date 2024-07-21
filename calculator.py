# Define addition function
def add(num1, num2):
    # return the sum of num1 and num2
    return num1 + num2


# Define subtraction function
def subtract(num1, num2):
    # return the difference of num1 and num2
    return num1 - num2


# Define multiplication function
def multiply(num1, num2):
    # return the product of num1 and num2
    return num1 * num2


# Define division function
def divide(num1, num2):
    if num2 == 0:
        raise ValueError('Cannot divide by zero')
    return num1 / num2


# Validate if the number is a valid floating-point number.
def validate_number(number):
    try:
        # Attempt to convert the input value into a float.
        float(number)
    except ValueError:
        # If conversion fails, raise an error.
        raise ValueError('Input is not a valid number.')
    return number


# Round result to a specified number of decimal places. This case it is 2.
def round_result(result, precision=2):
    try:
        result = float(result)
    except ValueError:
        raise ValueError('Result must be a number')

    return round(result, precision)
