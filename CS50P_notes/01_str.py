#CS50 Introdunction to programming

#Functions and Arguments intro

name=input("wht is ")         #variable is assigned to store the data    #space has to be added within argument or it'll be continues
print("hello "+ name)         #the "+" concotonates the two strings like a text, its just one argument
print("hello", name)          #the "," creates two arguments,
#the default parameters of print function adds a space between arguments sep=' ' and a new line at the end="\n"
print("hello", name, sep="", end="\n\n\n")     #this has no space and 3extra lines

    

print("hello,'friend'")      # to use actual "" quotation marks inside, the outside and inside can be different to work
print('hello, "friend"')     
print("hello, \"frined\"")   #escaping "\" represents an escape caracter, as its only used with multiple characters



# Parameters and Types of parameters 
# Whats passed first gets printed first are possitional parameters but there are named parameters
# f-srting or format string to run format the string in a different way, New feature

name=input("whats the name? ")          #forgot where the input function goes
print(f"hello, {name}")                 #by putting {} for the variable and f before "" to say its a f-string, format string




#checking the functionalities built into strings

name=input("whats your name? ")
print(f"hello, {name}")         #typed the {name} outside quotation but the purpose was to keep it inside


#to adjust the miss typed spacing in a string and capitalization we can use methods
name=name.strip()              #to remove spaces on left and right
name=name.capitalize()         #to capitalize first letter
name=name.title()              #to create title format
name=name.title().strip()      
#these are called methods


name = input("whats your name? ").title().strip()                  #everything is in one line
print(f"hello, {name}"+ "sss", name, sep='   ', end="\n")          #forgot how to add string and to mark string with ""


#the right side of = is going to get done first and result put to left side in name= whaterer is there
#sometime missing = where is and isnt

#method is a function that is built in to a function which we can use, can check documentation for more
#split methods in strings which splits string to many sub strings
#each part can be assigned a variable so only one can be called


name=input("please type in your name, ").strip().title()
first, last = name.split(" ")                             # (" ") argument says divide the name at single space " "
print(f"hey, {first}", "How are you", end="\n", sep=",")   

#lots of mistakes in running due to minor errors, one word name, 3 word name, putting() for end
#still no way of fixing 3 to 2 or 2 to 3 words in a name error, it expects as many variable i give



name=input("please type in your name, ").strip().title()
first, last = name.split(" ")
print(f"hey, {first}", emot=input("How are you?  "), end="\n", sep=",")
#print(f"oh ", {emot})          #couldnt get the second input and print command  to work 



name=input("please type in your name, ").strip().title()
first, last = name.split(" ")
print("hey,", first, emote = input("how are you? ") )         #had put everything out of Print bracketc corrected
#print(f"oh ", {emote})        #seems input or variable defined inside a print isnt available            



name=input("please type in your name, ").strip().title()
first, last = name.split(" ")
print("hey,", first, emote = input("how are you? ") )          #maybe putting emote separately might have worked

