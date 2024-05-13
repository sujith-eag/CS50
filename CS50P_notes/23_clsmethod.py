# at 12h 28m


# class methods
 # @classmethod
""" There are instance methods and instance variables bu we also have classmethods.
Sometime it is not better to associate functions with objects of a class 
but rather with the class itself .

@classmethod is a decorator function, which signifies that this method isnt an instance method
that has access to self, this doesnt have access to self but knows which class it is inside
"""

import random
class Hat:
    def __init__(self):
        self.houses = [ "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]

    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)         # print(name, "is in", random.choice(self.house))

hat = Hat ()    #instantiate an hat object, this is a common syntax for instantiating a class object
hat.sort("Harry")

# instance methods
# if i dont want to instantiate the hat with a function hat=Hat(), it can become 1hat=Hat(), 2hat=Hat()
# but i want to associate it with the class itself
# then we can use @classmethod


import random
class Hat:
    
    houses = [ "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]
    # class variables within class itself, just because i need a variable in this class, no

    @classmethod                            # there is no self now so class is directly referenced
    def sort(cls, name):                    # to avoid conflict with class key word, "cls" is used for reference
        house = random.choice(cls.houses)   # accessing list present in this class
        print(name, "is in", house)         # print(name, "is in", random.choice(self.house))

    #hat = Hat() is not needed anymore to instantiate an hat object
Hat.sort("Harry")
    # using class name, .method name and passing any varible



# classes should represent real life objects
# it is common sense to have all the related variables, and functions within that class
# cleaning up the previous code


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input ("House: ")
        return cls(name, house)  # cls means create an object of the current class
# there is a function called get, a student method which can be called without instantiating a student object first
 
def main():
    student = Student.get()   
    print(student)

if __name__=="__main__":
    main()


# instance methods and instance models belong to or operate on specific objects, specific student or hat
# Class methods operate on the entire class itself, all objects of a class


# there are @staticmethods

# ends at 12h 59m
