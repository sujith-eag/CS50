# strats at 14h 39m

# unpacking   (*list)
# taking the value from a list, unpacking the values and assigning it to variables

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")    # the single * in list coins unpacks it itself and passes it to variables
            # ususal convention  print(total(coins[0], coins[1], coins[2]), "Knuts")

# * cant be used with set



# using dictionary
# another version of this, not just possitional argument of 1 2 3
# but with named parameters

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print( total (galleons=100, sickles=50, knuts=25))




def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles":50, "knuts":25}

print( total (coins["galleons"], coins["sickles"], coins("knuts")), "knuts")




def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles":50, "knuts":25}

print( total (**coins), "knuts")    # similar to   print( total (galleons=100, sickles=50, knuts=25))

# ** is used to unpack dictionary
# coins = {"galleons": 100, "sickles":50, "knuts":25}
# it unpacks this dict into three keys and values seperated by = 
# galleons = 100  ,  sickles = 50 ,  knuts = 25

# if galleons.. are given defult value of 0, less than 2 can also work




#   *args   **kwargs
# *args visual representation when a function takes a variable number of arguments, not specific number
# a variable number of possitional arguments
# **kwargs - key word arguments
# if i want certain key word arguments to be called with name or key word argument 

def f(*args, **kwargs):         # f is taking some possitional and some named arguments
    print("Positional:", args)

f (100, 50, 25)      # if i change it to f (100, 50, 25, 5)  or (100)  
                    # it will also show output with any number of args


def f(*args, **kwargs):
    print("Named:", args)

f(galleons=100, sickle=50, knuts=25)        # the output will come out as a dict {}

# supports variable number of possitional or named arguments


# The default code might be,   so it can be easily used
#   print(*objects, sep='', end="\n", )
#        for objects in objects:
# this shows that print has a variable number of arguments


# ends at 15h 6m
