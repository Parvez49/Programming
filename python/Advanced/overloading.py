

# Method overloading is the ability to define multiple methods
# with the same name but with different parameters.
#
# However, in Python, we can achieve a similar effect using
# default arguments and variable-length arguments.
# Here's an example:

"""
class Calculator:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c

calculator = Calculator()

print(calculator.add(1))  # Output: 1
print(calculator.add(1, 2))  # Output: 3
print(calculator.add(1, 2, 3))  # Output: 6
"""

class Calculator:
    def add(self, *args):
        #print(type(args)) # tuple
        result = 0
        for arg in args:
            result += arg
        return result
calculator = Calculator()

print(calculator.add(1))  # Output: 1
print(calculator.add(1, 2))  # Output: 3
print(calculator.add(1, 2, 3))  # Output: 6

