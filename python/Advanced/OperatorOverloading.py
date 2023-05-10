

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.st="OperatorOverloading"
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __len__(self):
        return len(self.st)

p1 = Point(1, 2)
p2 = Point(3, 4)

# add two Point objects
p3 = p1 + p2

# print the result
print(p3)  # output: (4, 6)
# -------------------------------------------------------------
"""

 Some commonly used operator overloading methods in Python:

    __add__(self, other) - overload the addition operator +
    __sub__(self, other) - overload the subtraction operator -
    __mul__(self, other) - overload the multiplication operator *
    __truediv__(self, other) - overload the true division operator /
    __floordiv__(self, other) - overload the floor division operator //
    __mod__(self, other) - overload the modulo operator %
    __pow__(self, other[, modulo]) - overload the exponentiation operator **
    __eq__(self, other) - overload the equality operator ==
    __ne__(self, other) - overload the inequality operator !=
    __lt__(self, other) - overload the less-than operator <
    __le__(self, other) - overload the less-than-or-equal-to operator <=
    __gt__(self, other) - overload the greater-than operator >
    __ge__(self, other) - overload the greater-than-or-equal-to operator >=
    __len__(self) - overload the len() function
    __getitem__(self, key) - overload indexing using square brackets []
    __setitem__(self, key, value) - overload assignment to indexed values
    __str__(self) - overload the string representation of an object using the str() function
    __repr__(self) - overload the string representation of an object using the repr() function

Note that these are just some examples of commonly used operator 
overloading methods in Python. You can also define your own 
special methods to overload other operators or to provide custom 
behavior for your objects.
"""

