# at 11h 28m

# Data Validation

# trying to avoid blank data, and allowing only one of few fixed data

# "raise" an exception
    # if an unput is blank, we can raise a value error
# init__(self, name, house=0)  can make an argument optional
# can add first second name

class Student:
    def __init__(self, name, house):
        if not name:                                 # "not name" is    if name == ""  (check for empty)
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def __str__(self):
    return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(f"{student.name} of {student.house}")    # print(student) will specify the location of data, not data
                                                    
def get_student():                       
    name = input("Name: ")
    house = input ("House: ")
    student = Student(name, house)
    return student                      
                                        
if __name__=="__main__":
    main()


# __str__ is another special method in class
"""
defined in a class, python will autonmatically call this function 
when a function(print) wants to see the object as a string. without it in a class it will be odd
def __str__(self):  when string is defined it will have access to the curent data, so automatically prints it
"""


class Student:
    def __init__(self, name, house):
        if not name:                        
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
 
def main():
    student = get_student()   
    print(student)

def get_student():                       
    name = input("Name: ")
    house = input ("House: ") 
    return Student(name, house)                      

if __name__=="__main__":
    main()



#Function inside of a class is called a Method
# __init__  __str__ are methods that just work
# methods can be defined


# Properties - attributes with more defence mechanisms
# @property

# decoretors are functions that modify other functions

# you cant have an instance variable and function named the same, they will clash


class Student:
    def __init__(self, name, house):
        if not name:                        
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

     # Getter - gets some attributes   
    @property
    def house(self):
        return self._house
    
    # Setter - sets some attributes
    @house.setter 
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
 
def main():
    student = get_student()   
    print(student)

def get_student():                       
    name = input("Name: ")
    house = input ("House: ") 
    return Student(name, house)                      

if __name__=="__main__":
    main()


# setter doesnt let the data be circumvented, it has to pass through a setter
# it recognises the pattern that is assessing the class data



# class int (x, base=10)    int is a class, getting object of type int
# class str (object='')    str is a class, getting object of type str
# str.lower()  is a method in str class
# str.strip([chars])
# class list([iterable])
# list.append(x)   a method in list class
# class dict
 


