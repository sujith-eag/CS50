#Looking into creating our own functions to use it most of the places by calling on it

# def is define which allows defining your own function,
#by typing def naming the function, parenthesis(), and : the defining begins
#whatever gets indented below it is treated as part of the function


def hello():
    print ("hello")

name = input("whats your name? ")
hello()
print(name)

#functions have(), optional are [], to create new arguments "," can be used
#methods have = and assigning values is also =,    "" and ''are interchangable



def hello(to):
    print("hello,", to)

name = input ("whats your name? ")
hello(name)

#the parameter for hello() is assigned as (to)
#seems it acts as a variable and it gets replaced by anything that is in () of hello
#so hello(name) takes the value of "name" and replaces with the variable "to" in the function we defined



#giving default value to the function like script had sep=' ' and end='\n'
#if no value is provided default can run, if defined it gets replaced

def hello(to="world"):              #defining hello, with parameter to, and default value world, :
    print("hello,", to )            #prints srting hello, with another variable to

hello()                             #calling hello()  prints hello world, asks input
name=input("whats your name? ")     
hello(name)                         #calling again with hello as argument, replaces value of to and gives name




#functions have to be defined at the top a file (this became bit confusing)
#defining function on top will be like writing code in reverse

#its fixed by putting the main part of the code on the top of the file
# in this it is asking for name and calling name function

def main():
    name=input("whats your name? ")     
    hello(name)                            #input is taken, hello is called and input is passed to hello()  

def hello(to="world"):                     #input becomes value of variable "to"
    print("hello,", to)                    #prints hello and input

main()

#main is defined, hello is defined,then main() function is called




# Issue of scope of variable  

def main():
    name=input("whats your name? ")     
    hello()                                #hello is called without argument, ie not passing the input value     

def hello():                         #hello is defined without argument
    print("hello,", name)            #name is directly called from the main function but name only exists in main
                                     #so there will be an error   
main()

#issue of "Scope" which refers to a variable only existing in the context it was defined in
#name was defined in main() so it cannot be used directly in hello()
#when the value is handed to hello() within the main(), it can be used
#its for each function to name its own variable so the "name" variable in main can be passed to "hello" which becomes "to"
 




# the previous hello() funtions had only side effects, printing data on the screen

# input() hands a value, str(), int(), float() functions returns a value that was passed into it
# "return" a key word can be used to return the value back to another function


def main():
    x = int(input("whats x? "))
    print( "value of x squared is,", square(x))    # i should stop lookig at variables like (x) (n) it can change
                                                #but functions are more stable passing values bw them

def square(n):
    return n*n              #the return function passes the value back to main function
    return n**2            # ** is raising power
    return pow(n, 2)       # pow is for raising power

main()

#end of Lecture on Functions and variables at 1h 50min
#this was so good learning and practice

