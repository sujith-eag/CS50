# starts at 13h 58m

# python is a dynamically typed language, there is no need to say u are using a int, float, set .. it figures it out
# it is not strongly typed language where program has to be told what we are using

# type hints
# docs.python.org/3/library/typing.html

# mypy
# is a program that allows checking if your code adheres to the type hints you have given
# pip install mypy
# mypy.readthedocs.io


def meow (n: int):      # : int is a type hint, it says that n should be an int, doesnt do anything
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))  # type hints can be passed to variables also
meow(number)

# when i run mypy 26_mypy.py   (not python)
# it gives error, "incompatible string, expected int"


def meow (n: int) ->str:   # ->None type hint saying that this function doesnt return anything
    for _ in range(n):   # fixed by    return "meow\n" * n
        print("meow")       # because of operator overloading * can multiply strings with int

number: int = int(input("Number: "))
meows: str = meow(number)       # input is passed to meow() and print happens
print(meows)                # since no value is returned, it prints None

# mypy can detect it if run in mypy



# Docstrings
# document strings 
# peps.python.org/pep-0257      python enhancement proposal
# standerdises how to document your functions and other aspects of your code
# """ """ in a function to document, it uses restructured text convention to make docstrings

def meow (n: int) ->str:
    """
    Meows n times.
    :param n: Number of times to meow
    :type n: int 
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str    
    """
    return "meow\n" * n
number: int = int(input("Number: "))
meows: str = meow(number)      
print(meows)




# argparse
# when allowing users to pass in command line arguments
# input is meow.py -n 3

import sys

if len(sys.argv) == 1:   # name of file goes in sys.argv so it will be 1
    print ("meow")       
elif len(sys.argv)==3 and sys.argv[1] == "-n":   # checking if they gave 3 arguments name, -n and 3
    n = int(sys.argv[2])             # sys.argv[1] == "-n"  checking if second argument was -n
    for _ in range(n):     # n = int(sys.argv[2])  converting 3rd argument, 3 into int
        print("meow")
else:                   
    print("usage: meows.py")


# argparse    
# a library that allows cass in configuration at commandline   argument parser
# docs.python.org/3/library/argparse.html
# handles the parsing and analysis of command line arguments

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")    # a constructor for a calss for argparser
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()      # parse args by default looks at sys.argv for me and stores all in args

for _ in range(int(args.n)):    # .n is syntax for accessing properties inside an object
    print("meow")

# without a -n it wont run

# almost all programming environments gives usage information when -h --help is typed
# adding Parameter (description="Meow like a cat") and other things
# making it work even without argument, by
# making default=1 and setting type=1 so no need of maual int conversion

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()  

for _ in range(args.n):
    print("meow")

# ends at 14h 39m
