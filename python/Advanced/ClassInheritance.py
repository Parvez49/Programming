
# ---------------------Inheritance-----------------------
   # Single Inheritance
"""
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def introduce(self):
        print(f"My name is {self.name}, I'm {self.age} years old, and I live at {self.address}.")

class Employee(Person):
    def __init__(self, name, age, address, company, job_title):
        Person.__init__(self,name, age, address)
        self.company = company
        self.job_title = job_title
        self.salary = 0

    def introduce(self):
        super().introduce()
        print(f"I work at {self.company} as a {self.job_title} and my salary is ${self.salary}.")

    def give_raise(self, amount):
        self.salary += amount
        print(f"I got a raise of ${amount}! My new salary is ${self.salary}.")

person = Person("Alice", 25, "123 Main St")
employee = Employee("Bob", 30, "456 Elm St", "Acme Corp", "Software Engineer")

# Call the introduce method on both instances
#person.introduce()
employee.introduce()

# Give the employee a raise and call the introduce method again
#employee.give_raise(5000)
#employee.introduce()
"""


# ---------------------------- Multiple Inheritance -------------------------
   # Subclass can inherit from Multiple Parent classes

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name}, and I'm {self.age} years old.")

class Employee:
    def __init__(self, company, job_title):
        self.company = company
        self.job_title = job_title

    def introduce(self):
        print(f"I work at {self.company} as a {self.job_title}.")

class Manager(Person, Employee):
    def __init__(self, name, age, company, team):
        Person.__init__(self, name, age)
        Employee.__init__(self, company, "Manager")
        self.team = team

    def introduce(self):
        Person.introduce(self)
        Employee.introduce(self)
        print(f"I manage the {self.team} team.")

# Create an instance of the Manager class
manager = Manager("Alice", 35, "Acme Corp", "Engineering")

# Call the introduce method on the Manager instance
manager.introduce()
"""

# --------------------------- Multilevel Inheritance ------------------
   # Subclass can inherit from Another subclass
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I'm {self.age} years old.")

class Employee(Person):
    def __init__(self, name, age, company, job_title):
        super().__init__(name, age)
        self.company = company
        self.job_title = job_title

    def introduce(self):
        super().introduce()
        print(f"I work at {self.company} as a {self.job_title}.")

class Manager(Employee):
    def __init__(self, name, age, company, team):
        super().__init__(name, age, company, "Manager")
        self.team = team

    def introduce(self):
        super().introduce()
        print(f"I manage the {self.team} team.")

# Create an instance of the Person class
person = Person("Alice", 25)

# Create an instance of the Employee class
employee = Employee("Bob", 30, "Acme Corp", "Software Engineer")

# Create an instance of the Manager class
manager = Manager("Charlie", 35, "Acme Corp", "Engineering")

# Call the introduce method on all three instances
person.introduce()
employee.introduce()
manager.introduce()
"""

# ------------------------- Hierarchical Inheritance ----------------------
   # one Base class is Inherited by Multiple derived classes
"""
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello, my name is", self.name)

class Student(Person):
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number
    def study(self):
        print("Studying...")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def teach(self):
        print("Teaching...")

student = Student("John", 123)
teacher = Teacher("Jane", "Mathematics")

student.greet()  # Output: Hello, my name is John
student.study()  # Output: Studying...

teacher.greet()  # Output: Hello, my name is Jane
teacher.teach()  # Output: Teaching...

"""


"""
# ----------------------class-------------------------- 
import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = datetime.datetime.now().year - birth_year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        return age >= 18

person1 = Person("Alice", 25)
person1.greet()

person2 = Person.from_birth_year("Bob", 2000)
person2.greet()
if Person.is_adult(person2.age):
    print(f"{person2.name} is an adult.")
else:
    print

print(person2.is_adult(56))
"""