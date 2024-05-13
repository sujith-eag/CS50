# starts at 13h

# inheritance  - a compelling feature of oop
"""
designing the classes in a hierarchical fashion so they can inherit the attributes ie methods or variables form
another class, if they have those in common.
if code is getting copy pasted then there is a method to write code once and reuse it
"""

# the names and error checkings are getting copied between them

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name=name
        self.house=house

class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name")
        self.name=name
        self.subject=subject



# Seperating out all the common attributes of professor and students
# super() is a way of accessing the superclass, __init__ is refering to its initial methods

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name=name
                                        # wizard becomes the super class of student and professor
class Student(Wizard):               #student inherits from wizard, it is a sub class of wizard
    def __init__(self, name, house):
        super().__init__(name)       # the name from student class is passed to init of wizard class, super class
        self.house=house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject=subject

wizard = Wizard ("Albus")
student = Student("Harry", "Gryffindor")
professor=Professor("Severus", "Defense against the dark arts")

# the wizard = Wizard ("Albus") is the init which calls the init method of wizard
# the student and professor calls will call both their init and the superclass init methods


# Hierarchy of Exceptions
"""
BaseException
    KeyboardInterrupt
    Exception
        ArithmeticError
            ZeroDivisionError
        AssertionError
        AttributeError
        EOFError
        ImportError
            ModuleNotFoundError
        LookupError
            KeyError
        NameError
        SyntaxError
            IndentationError
        ValueError
"""


# operator overloading 
# taking the usual math operators and assign them new meaning with our own interpretation
# docs.python.org/3/reference/datamodel.html#special-method-names
# object.__add__(self, other)      self refers to whats on left and other refers to whats on right of +
# trying to add harry + ron will result in TypeError, Vault Vault cannot be added


class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0 ):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
    
potter = Vault(100, 50, 25)
print (potter)

weasley = Vault(25, 50, 100)
print(weasley)

# handled by operator overloading       galleons = potter.galleons + weasley.galleons
# at __add__ method                     sickles = potter.sickles + weasley.sickles
                                        #knuts = potter.knuts + weasley.knuts

total = potter + weasley                 #total = Vault(galleons, sickles, knuts)
print (total)

# there are list of allowed to be overloaded

# ends at 13h 29m
