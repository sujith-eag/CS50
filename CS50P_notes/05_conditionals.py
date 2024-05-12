#Conditions which allow to take forks in your own road

"""
mathematicals symbols
>   greter than
>=  greater than or equal to
<   less than
<=  less than or equal to
==  Check if it is equal, comparing on left and right
!=  Not equal to
"""



#Boolian expression, an Yes or No

x = int(input( "what is x? "))
y = int(input( "what is y? "))

if x<y:
    print("x is less than y")
if x>y:
    print("x is greater than y")
if x==y:
    print("x is equal to y")

# the : and Indentation tells that the below line should be executed only if the above is true
# whether the firsr one is true or false, it will execute all the lines asking three questions



x = int(input( "what is x? "))
y = int(input( "what is y? "))

if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
elif x==y:
    print("x is equal to y")

#elif which is else if is done to avoid unnecessary execution repetetion
#if x<y isnt true, else if is executed, otherwise stopped




x = int(input( "what is x? "))
y = int(input( "what is y? "))

if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else:
    print("x is equal to y")

# there is no point of checking the third question, its the last option so direct execution
# else can be used in the last one
# else isnt condition, just saying execution



x=int(input("what is x? "))
y=int(input("what is y? "))

if x>y or x<y:                              # "or" condition is used to reduce two to one line
    print("x is not equal to y")
else: print("x is equal to y")         

if x!=y:                                    # we can just use != or ==, insted of using x>y or x<y
    print("x is not equal to y")
else: print("x is equal to y")

if x==y:
    print("x is equal to y")                # here we are just using one condition with one check
else: print("x is not equal to y")

# indentation is a compolsary in python unlike other languages so everything has to be indented properly
# dont forget : before indentation





score = int(input("Score: "))

if score >=90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >=70:
    print("Grade: C")
else:
    print("Grade: F")

# when "if" is used in place of "elif", it will output everything even if first one was true
# ther is also "and" which i didnt use like "if 90 <= score and score <= 100"





#Parity,  to see if given number is even or odd

x=int(input("what is x? "))

if x % 2 == 0:                
    print("x is even")
else:
    print("x is odd")

# "%" is dividing x by the number and getting the reminder, even number/2 is zero





# str, int, float, bool
# the forth data type is bool for boolian which returns True or False (with capital T and F)

def main():
    x=int(input("what is x? "))
    if is_even(x):                  # is_even called and value of x is passed
        print("Even")               # is_even() is defined to return a boolian value of T or F
    else:                           # it is not nesessary that it has to be a number, T or F is enough conditionl to print
        print("Odd")

def is_even(n):
    if n % 2 == 0:                  # there has to be : for further indentation
        return True
    else:
        return False

main()

# functions like .strip() .capitalize() .title() is part of str,
# if our function returns a str, then these can be used




# Pythonic way of doing which can only be done in python is natural way of statng

def main():
    x=int(input("what is x? "))
    if is_even(x):          
        print("Even")             
    else:                   
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False    # One line is equal to the four                                            
                                            #if n % 2 == 0:               
                                            #    return True
                                            #else:
                                            #    return False
main()

# if n % 2 == 0 return True else False
# this doesnt work because "if" needs indentation so cant be in a line
# return doesnt need : or indentation so it can go first




def main():
    x=int(input("what is x? "))
    if is_even(x):          
        print("Even")             
    else:                   
        print("Odd")

def is_even(n):
    return n % 2 == 0      # n % 2 == 0 is by itself a boolian expression which returns T or F
main()                     # So ther actually no need of returning extra T or F as in "True if n % 2 == 0 else False"







name = ("what is your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")                                     
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")

#if isnt a function so doesnt need (), maybe it can have
# or is used to reduce 3 into 1



# "match" (similar to switch in other languages)
# using "match" and its cases to compare

name = input("what is your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:                        
        print("Who?")
# "_" underscore is used to cover any undefined cases



# "|" a vertical bar is used kind of "or"

name = input("what is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":      
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:                           
        print("Who?")



# End of Conditionals and Operators