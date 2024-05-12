# Exceptions mean Problems in your code

# SyntaxError   -  unterminated string literal   (missed closing ")
# Problem with the typed code

# RuntimeError
# Can happen due to the type of inputs coming while program runs
# Has to plan defencively to think and take care of it before hand what they will type and miss type

x = int ( input( "whats x?"))       # converting to int type avoids error in calculation, like + concatination
print (f"x is {x} ")    # with f-string, format string
print ( "x is", x)      # without f, since its two arguments it will have its space by sep

        # when strings "cat" are entered for int, causes error
# ValueError: invalid literal error for int() with base 10: 'cat'


# Writing code with error handling in mind, writing code defesively to avoid such errors



#Keyword "try" and "except"
# its like "try" to do something in python, and check if something exeptional will happen
# "except" if something goes wrong then i can do something goes wrong

try:
    x = int( input ("what is x? "))
    print (f"x is {x}")
except ValueError:
    print ("x is not an integer")

# Giving an appropriate error message when things go wrong
# exept: can be just left without any specific error which will catch any error but
# its better to know type of error and give proper feedback



# In best practice, you should "try" only those lines which will cause errors
# here calling print isnt going to cause any value error 

try:
    x = int( input ("what is x? "))
except ValueError:
    print ("x is not an integer")
print (f"x is {x}")

# but a str "cat" raises a NameError:name "x" is not defined (in line 6)
# not because of scope within function(its true in java, c but not in python)
# Problem is due to order of operation
# values go from left to right of =
# input() gave str to int() and immediately it created ValueError, it was handled by the "except"
# but x didnt get a value because "cat" coudnt be converted to "int"
# Print is not indented so it will get executed if "try" succeeded or not
# since value didnt get passed print, it caused NameError




# using "else" keyword to fix it
# "try" to do the following
# "except" if it goes wrong something exceptional, this gets executed
# "else" this line, as it was successful and nothing went wrong,
# the "else" clause is associated with "try",   not "except"

try:
    x = int( input ("what is x? "))
except ValueError:
    print ("x is not an integer")
else:
    print (f"x is {x}")




# instead of quitting the program because the input wasnt right
# using "loops" to prompt again till value is right

while True:
    try:
        x = int ( input ("what is x? "))
    except ValueError:
        print("x is not an integer") 
    else:                              # "else" is not associated with "except" but with "try"
        break                          #  exception happens then it loops  (how is it true?) Except is true?
                                       # No "exeption" then skips "except" and executes "else" and breaks when x is int()
print (f"x is {x}")                    # and prints with the x
                                         # if print was below "else" it wouldnt break out of the loop




while True:
    try:
        x = int (input( "what is x? "))
        break                               # if x gets a value, then it breaks, so simple
    except ValueError:                      # exception, then print and loop to input
        print("x is not an integer")

print(f"x is {x}")




# "return x" is used instead of "break" as return does the same but also returns the value also
# defining a function get_int() of our own which gets int


def get_int():
    while True:
        try:
            x = int( input( "what is x? "))
            return x
        except ValueError:
            print("x is not an integer")
get_int(x)
print(f"x is {x}")

# this is interesting, x isnt getting out of get_int




def main():                 # took me some time to figure out why x isnt passed to print,
    get_int()               # because get_int() has to pass value to x by saying x = get_int()        
    print(f"x is {x}")      # then main() will have x

def get_int():
    while True:
        try:
            x = int( input( "what is x? "))
            return x
        except ValueError:
            print("x is not an integer")

main()



# correcting value passing of x

def main():              
    x = get_int()                
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int( input( "what is x? "))     # return int(input("what is x? "))
            return x                            # this line just directly returns without having to initialise a variable x
        except ValueError:                      # just might make it difficult to read
            print("x is not an integer")

main()




# pass
# instead of giving user error messgage,and prompting them to enter x
# reprompting for input x without error can be done with pass
# silently ignoring it like pass

def main():              
    x = get_int()                
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int( input( "what is x? "))
            return x                       
        except ValueError:              # except catches the value error
            pass                        # pass is to just ignores it 

main()






# making the function reusable 
# by not specifying what a "calee" the function thats being called to have a prompt
# but letting the "caller" function thats calling to decide the prompt
# so caller should "pass" what is wants to be prompted to "calee"
# working
# Caller passes the statement, calee recieves the argument and uses it to return the value

def main():              
    x = get_int("what is x? ")        # main is calling "get_int" giving it an argument it wants              
    print(f"x is {x}")                # x is whatever "get_int" returns

def get_int(prompt):                    # "get_int" gets the argument
    while True:
        try:
            x = int( input(prompt))     # gets the input and passes to x
            return x                      # x is passed to main()
        except ValueError:          
            pass                       

main()


# 3rd week ends at 4h 50m