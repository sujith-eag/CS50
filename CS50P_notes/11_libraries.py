#Libraries    Starting at 4h 52m

# libraries(modules) are files of code others or you have written to be used in the program
# abilities to share codes

# python comes with "random" libraries, modules in random.py
# docs.python.org/3/library/random.html

# "import" is the key word to import the content and functions from a library(module)

#random.choice(seq)
# from "random" module, a function called "choice", parameter in () is sequense which means a list like


import random
coin = random.choice( ["heads", "Tails"] )        # giving a list[] with two strings as two elements # picks any one
print(coin)

# "import" gets all the functions to the program, but it has to be typed as "random.choice()" 
# because it has to be associated with the scope of the module 


# "from" is a key word that allows importing function from a module but more specific than "import"

from random import choice
coin = choice ([ "heads", "Tails"])
print (coin)





# random.randint(a,b)   read as rand int to get a random integer
# it gets the values between a and b, inclusive of a and b,
# ex random.randint(1,10) wil give no from 1 and ending at 10

import random
number = random.randint(1,10)
print(number)



# random.shuffle(x) ,   shuffles a group of items
# document says random.shuffle(x) doesnt return a value but shuffles the whole list
# so assigning a value is not necesary (thought it would not work but it worked)

import random
cards = [ "king", "jack", "queen", "joker"]
random.shuffle(cards)                     #new = random.shuffle(cards)     also worked              
for card in cards:
    print(card)





# "statistics" module
# docs.python.org/3/library/statistics.html

import statistics
print (statistics.mean( [100, 90] ))




# "command-line arguments" is a feature
# allows providing arguments or input to the program while executing the program
# the words typed after the file while executing gets passed on as arguments without having to be prompted


#sys,   deals with program itself
# docs.python.org/3/library/sys.html

# "sys.argv"  is a variable that exists in sys, called arg v, argument vector
# argument vector means list of all the words a human typed in at their prompt before hitting enter
# argv is a list[], 
# at [0} the first element is name of the file,  so returns name of file
# the second element at [1] is going to be the typed data

import sys
print ("hello, my name is", sys.argv[1])

# if nothing is typed at prompt it gives an "IndexError", meaning the list ran out of values
# as there is no value at [1]
# it can be handled with an "exception"

import sys
try:
    print ("hello, my name is", sys.argv[1])
except IndexError:
    print (" too few arguments")


# just avoiding the error with if, elif, else
# using len() function to check the length of the list to check and correct it

import sys
if len(sys.argv) <2:              
    print("too few arguments")
elif len(sys.argv) >2:
    print("too many arguments")  
else:
    print( " hello, my name is", sys.argv[1])

# now it takes only one word but if full name has to be printed without without much,
# then it can be "sujith kumar" at prompt that gets taken as one word



# just for design separting the checking and printing part,

import sys
if len(sys.argv) <2:              
    print("too few arguments")
elif len(sys.argv) >2:
    print("too many arguments")  

print( " hello, my name is", sys.argv[1])

# this introduces a IndexError because even though it was checked and error was shown
# the print will anway going to happen, without a value causing error


# in such cases its better to exit the program all together
# using "sys.exit" it can print the given string and also exit at that line
# if program gets till print, it means there is a proper argument

import sys
if len(sys.argv) <2:              
    sys.exit("too few arguments")
elif len(sys.argv) >2:
    sys.exit("too many arguments")  

print( " hello, my name is", sys.argv[1])



# taking many names at once so ther are no too many arguments

import sys
if len(sys.argv) <2:              
    sys.exit("too few arguments")

for name in sys.argv: 
    print( " hello, my name is", name)

# if 3 names are given, it will print out 4 times because 0 has name of the file


# ther is a way to get only few "slice" of argv, taking a subset of a data structure or a list
# Specifying where we will start and end of the list
# sys.argv[1 : ]  1 means starting at second element [1], and blank means going to the end

import sys
if len(sys.argv) <2:              
    sys.exit("too few arguments")

for name in sys.argv[ 1: ]: 
    print( " hello, my name is", name)

# [] at end of list can not just be used to go to a specific element like [1], [0], [2],
# but use [ : ] to specify the start and end of the list to be taken [0 : ] [2:4]  blank means beginning or end
# taking the slices
# [1 : -1]  removes the last one, counting one less from the end


# ending at 5h 35m
