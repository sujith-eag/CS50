# File I/O
# Read information from and retriving data


# new things
# listname.append()   to add data
# sorted(listname)    returns a sorted version of that list
# open()    is a function that opens a file so data can be read and written
         # docs.python.org/3/library/functions.html#open

# using "with" "as" for opening, writing and closing



# using list[] to collect data

names = []
for _ in range(3):
    name = input("whats your name? ")
    names.append(name)

# list names is defined, when run input is asked for 3 times
# names.append(name)  is moving the names to names[]

names = []
for _ in range(3):
    names.append(input("whats your name? "))

# instead of having a varable name and moving it to append
# the input can directly become the value with append



names = []
for _ in range(3):
    names.append(input("whats your name? "))

for name in sorted(names):
    print(f"hello, {name}")

# three prompts, data is appended to the list and sorted
# the sorted data is printed
# but all the data will be lost once it is rerun




# To save the data
# open() requires the name of the file and how we want to open it,
# returns a file handle

name = input("whats your name? ")
file = open("names.txt", "w")
file.write(name)
file.close()

# "open" gets the file, the file name is given, if it doesnt exist it will create one
# the "w" arguments says we want to write the data,  so file = ("filename.extension", "w")
# file.write(name) is called to write name inputs
# file.close() closes the file
# "w" write is dangerous
# the problem is, write rewrites the data every time the data is enterd
# data must be "appended" to store incrimentally


# using append "a", instead of a

name = input("whats your name? ")
file = open("names.txt", "a")
file.write(name)
file.close()

# it is appending without any gaps because "write" does not have a default new line like "print"


name = input("whats your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# a seperate new line can be written but using f-string also works
# the data got attached to last one and then new space, so need a fix here


# closing the file is also important
# it can be done with a key word
# "with" and "as"
# "with" specifies that in this context i want you to automatically  open and close a file

name = input("whats your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# you type "with", call the "function" in question 
# and write "as" and specify the name of variable that has to be assigned the return value of open
# previously variable "file" was separately initialised but now its in "as" (similar to for _ in range())
# if there is nothing indented below this line, then as soon as its done executing the file will close





# Reading them back
# "r" to read the data

with open("names.txt", "r") as file:
    lin = file.readlines()

for name in lin:
    print("hello,", name.rstrip())    # print("hello", name, end="")

# lin is variable, file.readlines() is the function for reading
# the data came eith extra line as we had line in data and new one was added by print also
# we can handle print or the data
# rstrip() allows stripping the implimentation detail in the data
# or we can do end=""

with open("names.txt", "r") as file:
    for name in file:
        print("hello,", name.rstrip())



# sorting the reading
# in the previous program the lines are read individually so sorting cannot be done
# all the data has to be read first and then sort and print
# "r" need not be specified because its the implicit default when openning a file

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for data in sorted(names):
    print(f"hello, {data}")

# names is an empty list, file is opened as file, each line in file is rsrtipped and appended to names
# data is sorted, each line is printed


# if we dont have to collect all the data
# directly sorting the file and reading by stripping space

with open("names.txt") as file:
    for line in sorted(file):
        print("hello", line.rstrip())


# if we want to do reverse name sort
# sorted(iterable, /,*, key=None, reverse=False)
# iterable are things that can be iterated over, resrse is by default false

with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print("hello", line.rstrip())



names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for data in sorted(names, reverse=True):
    print(f"hello, {data}")
    