# "Loops" starts at 2h 46m



# "while" loop
# "while" allows asking a question to get T or F and runs untill it is T
# indentation is way of making code a part of a thing 
# Crt + C will cancell program the infinite loop

"""
i=3
while i != 0:
    print("Meow")
"""
# Executing this will send it into infinite loop as i as always != 0
# So a method is needed to change i every loop so its eventually 0
# decremented by 1

"""
i=3
while i != 0:
    print("Meow")
    i=i-1
"""


# it can also be incremental by 1
"""
i=0
while i != 3:        #while i<3:
    print("Meow")
    i=i+1            #i += 1      # "i += 1" is a way to increment by 1
"""



# "for" Loop
# "list" a data type supported by python
# str, int, float, bool, list

# "for" allows you to iterate over a list of items
"""
for i in [0, 1, 2]:
    print ("meow")
"""
# "in" is just a new for stating value in the list
# "i" is initialise with 0 first, then 1 and then 2
# end of numbers in the list it will stop print
# [] are for lists,   again : and indentation



# to remove the manual number entry by using "range()" function
# range() will hand out whatever number of values it is specified
"""
for i in range(3):                      #for _ in range(3):
    print("meow")
"""
# the is simply defined by typing it!

# Pythonic Improvement
# if you just need a variable to just run a loop and wont be used again, not meaningful
# then it can be defined by a single under score "_"


# only a python feature
"""
print ("meow" * 3)              # will be meowmeowmeow

print ("meow\n" * 3)            # using an escap sequence like "\n" gives new lines
                                # but has an extra line
print ("meow\n" *3, end="")     # removing the default "\n" parameter of print function
                                # kind of difficult to read
"""


# making it interactive 
"""
n=int(input("cat should meow? "))
print("meow\n", end="")
"""

#but has to make sure the number is possitive
"""
n=int(input("wahts n? "))
    if n<0:
    continue
"""
# my attempt failed because, defined "n" outside the loop and used "if" instead of "while" "if"
# getting the input should be part of the loop

"""
while True:
    n=int(input("whats n? "))
    if n<0:
        continue
    else:
        break

for _ in range(n):
    print("meow")
"""
# "continue" just runs the loop again till n<0 is T
# "break" will break the recent loop that has begun 



# "else" can be removed and made tighter
# it breaks only if n>0
"""
while True:
    n=int(input("whats n? "))
    if n>0:
        break

for _ in range(n):
    print("meow")
"""
# "_" is a not important variable
# there is "while" "if" "else" "for" some confusion




# defining own function, a meow()
# call a function first and then define it later
"""
def main():
    meow(3)

def meow():
    for _ in range(n):
        print("meow")
main()
"""
# when i had to fix the number of prints i can use "for a _ variable in range(n)" 


# interactive    but  lots of conditions and values moving around
# seems easy when its there but coming up with it is the task
"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("whats n? "))
        if n>0:
            break            # it can just be "return n" insteaf of "break" within the loop
    return n                 # even with break, there has to be a "return n" outside the loop but within the function

def meow(n):                 # forgot to import n into meow() by giving it n, meow(n)
    for _ in range(n):       # 
        print("meow")

main()
"""
# call "main", which calls "get_number" to get a positive input only and pass it to "meow"
# "main" calls "meow" which has the "int" to run it that many times
# "meow" runs for "_" number to the "int range" and stops




# BREAKING THE STEPS INTO SMALLER & SMALLER BASIC STEPS