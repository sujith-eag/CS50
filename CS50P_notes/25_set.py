# starts at 13h 30m

# set  (data type)
# collection of values with no duplicates values (not a list) will delete the duplicates
# docs.python.org/3/library/stdtypes.html#set


# doing it without using a set

students = [
    {"name": "Hermione", "house": "Gryffindor" },
    {"name": "Harry", "house": "Gryffindor" },
    {"name": "Ron", "house": "Gryffindor" },
    {"name": "Draco", "house": "Slytherin" },
    {"name": "Padma", "house": "Ravenclaw" } ]

houses = []              # can also be list(),  list to accumilate all the houses uniquely
for student in students:                # iterarting over the students in dict, one dict at a time, so one student at a time
    if student["house"] not in houses:  # ?? if the new list(student)'s "house" variable is not present in houses[] 
        houses.append(student["house"]) # then append just that students house to the houses[]

for house in sorted(houses):
    print(house)


# using a set

students = [
    {"name": "Hermione", "house": "Gryffindor" },
    {"name": "Harry", "house": "Gryffindor" },
    {"name": "Ron", "house": "Gryffindor" },
    {"name": "Draco", "house": "Slytherin" },
    {"name": "Padma", "house": "Ravenclaw" } ]

houses = set()  
for student in students:               # for evert dict(student) in the list
    houses.add(student["house"])       # add the student house to the set() houses, duplicattes get deleted by the set 

for house in sorted(houses):
    print(house)




# global variables
# even if a variable is defined outside of a function, it can be read in a function like main()

balance=0

def main():
    print("Balance:", balance)   # balance = 0
    deposit(100)
    withdraw(50)
    print("Balancce:", balance)

def deposit(n):
    global balance  # this line tells python it is not a bug but to edit the global variable
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()

# UnboundLocalError: local variable 'balance' reference before assignment.
# main() could access and just print the balance, reading of global is fine
# but changing and writing to the global does not work, local variable can be changed

# moving the balance=0 into main() also doesnt work, because now it is a local variable to main()
# now withdraw and deposit do not have access to it
# it has to be declared inside a function

# if we pass balance as argument to function, then it will only change a local copy but not the actual variable outside



# using object oriented programming

class Account:
    def __init__(self):
        self._balance = 0    # properties might collide with same name so self._balance

    @property           # property is an instance variable that is protected that allows me to control how it can be read and changed
    def balance(self):  # this is a getter,  it allows syntax like account.balance to be used without _  
        return self._balance        # but prevent code from change balance account.balance=1000 wouldnt work

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main ():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)
 
if __name__ == "__main__":
    main()

# by definition, instance variables are accessible to all the methods in the class because
# we are accessing them through the special parameter 'self'


# using global keyword in a rather small program to give access and manipulate is fine
# using global can become messy and confusing very quickly, on where the data is stored
# better to use class




# Constants
# once set, doesnt allow it to be changed

# always put your constants above the file, instead of hard coding it in the syntax
# so its obvious and easy to change

MEOWS = 3

for _ in range(MEOWS):
    print("meow")

# python doesnt make variables into constants, so CAPITALISE to indicate its a constant
# no key words to make a variable unchangable, mostly honour systems




class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()     # istantantiating a cat function using a constructor, it can be anything
cat.meow()      # meow() is going to access the class constant of 3 ?????
                # it is a constant in a sense, you should not touch it, it is not enforced by the language

# ends at 13h 58m
