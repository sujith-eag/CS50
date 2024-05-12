# Integers

# % is modulo operator which allows taking the reminder after dividing a number
 
x=1  
y=2
z= x + y
print(z) 


#making it interactive with input()

x= input ("whats x? ")
y= input ("whats y? ")
print (z=x+y)             # i keep forgetting " " for strings and that defining a variable inside print doesnt work



x= input ("whats x? ")
y= input ("whats y? ")
z=x+y
print (z)
#the answer will be 22 as + is concatonating both numbers because they are treated as strings
#any input from keyoard is treated as a string
#can be corrected by converting them to integers by using int()


x= input ("whats x? ")
y= input ("whats y? ")
z= int(x) + int(y)
print (z)
#int isnt just a data type but also a funtion which can conver 2 from str type to int type
#tried to put z=int(x)+int(y) in print but removing the z might work


x= input ("whats x? ")
y= input ("whats y? ")
print(int(x) + int(y))
#no point of defining a variable z to use just for print



x= int(input ("whats x? "))
y= int(input ("whats y? "))
print(x+y)
#nesting a function within a function to convert x y itself to integers
#argument moves from inner function becomes input to outer function



print ( int( input("whats x? ")) + int(input("whats y? ")))

#one line but very complicated and clever for its own good
