# starts at 11h 5m

# Dict, Tuple, List are general purpose data types
# Classes - which allows for creating our own data types and name them

# Class is a blueprint for pieces of data, objects
# Primary feature of OOP, creating your own objects and data types with name 

# docs.python.org/3/tutorial/classes.html

# classes have attributes or properties that allow you to specify values inside of them 
# . allows getting into it


class Student:
    ...                 # ... is place holder, just invented a data type without any functionality
    
def main():
    student = get_student()
    print(f"{student.name} of {student.house}")     # class.key is how classes data can be indexed
                                                    
def get_student():                       # a variable student passes value to Class Student()
    student = Student()                   # creating an object of that class Student() 
    student.name = input("Name: ")              # student.name is how classes are accessed
    student.house = input ("House: ")
    return student    
                                           
if __name__=="__main__":
    main()



# Objects
# whenever a "Class" key word is used, we are creating an "Object"
# we create objects from classes, object is incarnation of class
# object is an instance of a class
# store data using dot notations (student.name)

# they are mutable and can be made immutable

# attributes of a class - instance variables (technically)

# name and class are variables called name and house inside an object whose type is student



# by defining a class you also get a function of same name
# not just attributes or instance variables, there are also "methods" or functions which you can define
# these functions allow you to determine behaviours and gives you better control

# a standard function "__init__(self)"  is __dunder  __init dunder init method
# instance method - if you want to initialise contents of an object from a class we use this method
# there is opportunity to customise this classes objects

# ?? "self" is a attribute that has to be made inordr to define other attributes??
# suppose house and name are passed to the init method, method is just a function inside of a class
# there will be no where to put them, to be able to store them somewhere (in the object)
# so this init method will have to take a semi secret method which has to come first 
# self (can be named anything), self gives you access to the current object that was just created

# student = Student(name, house) is constructor creating a student object, without any name or house
# the data has to be stored into the object, so pyton will call the init method automatically and gives reference to object
# to populate the object with values,
# so within init method we can do self.name to create a new attribute (instance variable) to put the name

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
            
def main():
    student = get_student()
    print(f"{student.name} of {student.house}")   
                                                    
def get_student():                       
    name = input("Name: ")
    house = input ("House: ")
    student = Student(name, house)      # a constructor call, line that construct a student object for me
    return student                      # the Student() is called from __init__()
                                        # return Student(name, house)   direct return of data 
if __name__=="__main__":
    main()

# this is similar to adding keys to dictionaries, adding variables to objects (self.name = name)
# instance variables to objects

# Class is just code
# Objects are stored in memory

# Classes can do what dict does
# but much more can be done , ensuring the correctness of data, better errorcheck, design more complicated software and efficiently
