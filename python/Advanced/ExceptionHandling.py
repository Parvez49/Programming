

"""
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An error occurred:", e)
"""

"""
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    result = x / y
    print("Result:", result)
"""

"""
try:
    file = open("myfile.txt", "r")
    # do something with the file
except FileNotFoundError:
    print("File not found.")
finally:
    if 'file' in locals():
        file.close()
"""

"""
import math
class NegativeNumberError(Exception):
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot take square root of negative number!")
    return math.sqrt(num)
try:
    result = square_root(-10)
    print(result)
except NegativeNumberError as error:
    print(error)
"""

# -----------------------------------------------------------
"""
The assert statement in Python takes a condition and an 
optional message as arguments. If the condition is true, 
the assertion is ignored and the program continues to execute 
normally. If the condition is false, an AssertionError is 
raised with the optional message as its argument. 
Here's an example:
"""

def divide(num1, num2):
    assert num2 != 0, "Cannot divide by zero!"
    return num1 / num2
result = divide(10, 0)

"""
Assertions can be useful for catching programming errors early 
in the development process, and for providing informative error 
messages to developers about what went wrong. However, it's 
important to note that assertions should not be used to handle 
user input or other unexpected errors that might occur at 
runtime, since they can be disabled in production code and can 
cause security vulnerabilities if used improperly.
"""



