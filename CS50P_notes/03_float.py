#docs.python.org/3/library/function.html#round    to round number to a nearest digit
#round(number[, ndigits])     []  square brackets in code means optional
#round means just one number, but if you want more then specify


#if i have to round to a nearest number

x = float ( input ( "whats x? " ) )     # x = input(float)  did a mistake by reversed the functions
y = float ( input ( "whats y? " ) )
z = round ( x + y )
print (z)




x = float ( input ( "whats x? " ) )
y = float ( input ( "whats y? " ) )
z = round ( x + y )
print ( f" {z:,} " )

# creating a f-string argument and then applying {z:,} makes the number have comma
# oh i need "" for {} if i have to pass f string, format string
# looking at documentation is way to know these formats


#thers isnt an upper bound on how large an int can be but float can get cut off into finite digits

x = float ( input ( "whats x? ") )
y = float ( input("whats y? ") )
z = round(x / y, 2)
print (z)

# on rounding float to nearest few decimals
# 2 in the argument of z allows rounding to nearest 2 decimals



x = float ( input ( "whats x? ") )
y = float ( input("whats y? ") )
z = (x/y)
print= (z)           #there was no z result because i used () ???  idiot there is an = in print, so only no z result



x = float ( input ( "whats x? ") )
y = float ( input("whats y? ") )
z = x/y
print ( f"{z:.2f}" )
#by converting it into an f-strinf, format string i can round the result decimal to 2,  Just one more method
#f string approach
