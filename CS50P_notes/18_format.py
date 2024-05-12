# starts at 9h 46m
# writing code to Reformating the user data to the format we want


# suppose names are in first last or last, first

name = input("whats your name? ")
if "," in name:
    last, first=name.split(", ")
    print(f"hello, {last} {first}")

print(f"hello, {name}")

# so many mistakes
# put = for print = (), after all this time still mistakes
# having two print functions but both will run anyway when there is ,
# split on ", " made last, first but print also gave last, first
# could have given data to name and used as one print
# was doing ("if name has ", ")  instead of (if "," in name)  
# split (, )  doesnt work because its a string so split (", ")
# more mistakes while doing name = (f"{} {}") by adding , without ""


# corrected clean up code for "first last"  "last, first"

name = input("what's your name? ")
if "," in name:
    last, first= name.split(", ")
    name = (f"{first} {last}")

print(f"Hello, {name}")

# for "first,last"  "first last, jr"
# making the space optional(?) using regular expressions
# but putting it in split(, ?) wont work because split doesnt support re
# have to use the library re


import re
name = input("what's your name? ")
re.search(r"^.+ .+$", name)

# raw string is used for not treating anything as function
# variable has to be passed as " re.search(pattern, string, flags=0) "
# but the () just doesnt group data but captures and returns data
# if thats not necessary then non capturing version can be used  (?:...)


# the data that has to be captured is covered by (),  ^(.+), (.+)$
# data left and right to the ", "
# ", ?" is used in middle to make the space optional so (malan,david) is valid
# suppose there is more space then ", *" is used so any extra space is removed? dont know how this happened
# ie  (malan,    david)

# 3 versions of doing it 

import re
name = input("what's your name? ")
matches = re.search(r"^(.+), ?(.+)$", name)        #  (r"^(.+), *(.+)$", name)
                                        # very important    
if matches:                             # if name has , then "matches" variable is true
    last, first = matches.groups()      # groups of () from re.search are called
    name = f"{first} {last}"            # name is updated

if matches:
    last = matches.group(1)             # or just the first group and second group is called
    first= matches.group(2)             # it is group, not groups here, individual () from matches
    name = f"{first} {last}"            
                                        # if naming 2 more variable isnt nesessary
if matches:                             # directly update name by concatination
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")

# we are using re.search now not just to get True or False
# but also to get back specific values using () to capture specific data

# in re.search and getting back data it is group(1), group(2) but not 0,1
# here 1 is 1 and 2 is 2  as there is something in 0


# new feature in python
#  := wlrus operator 
# it allows to assign value and also ask a boolian question at the same time

matches = re.search(r"^(.+), ?(.+)$", name)        # matches is called and data is capture
if matches:                                        # asking if matches is true in next line
    name = matches.group(2) + " " + matches.group(1)

if matches := re.search(r"^(.+), ?(.+)$", name):    
    name = matches.group(2) + " " + matches.group(1)

# := is called instead of =
# the value is being assigned from left to right and also boolian question is being asked


# ending at 10h 05 min