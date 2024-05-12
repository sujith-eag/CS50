# Comma separaded values, CSV
# A common convention To store multiple pieces of information that are related in a same file

# the data is separated by comma, the comma represent a collumn

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# open file, move it to a variable, take out each line, strip, split into parts and store in variable
# print each parts separately
# here all data from file is passed into a list called "row"

# here it is put between two variables, name and house

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")



# Sorting it out
# just adding it to first file that got the data

with open("students.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


# if we want to do it after splitting
# the split data is appended to the students[] list
# then sorted and read and printed with for _ in _
# more complicated

students = [ ]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)



students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}        # student = {"name":name, "house":house}
        student ["name"] = name                     # same thing with one line of code
        student ["house"] = house
        students.append(student)          # each student is passsed to student dictionary 

for stu in students:
    print (f"{stu['name']} is in {stu['house']}")   # '' single quote because it already has " "

# making a student {} dictionary and giving key "name" and "house"



# sorting the dictionary

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}  
        students.append(student)    

def get_name(student):                  #new function to return name from student{}
    return student ["name"]             # this isnt necessary function

for stu in sorted(students, key=get_name):    # sorted() has as argumrnt get_name function() which becomes key 
    print (f"{stu['name']} is in {stu['house']}")   # get_name doesnt have () here because the sorted function calls for it

# python allows for passing function as argument for other functions
# this might be complicated but allows full freedom to sort and print
# def get_name can be changed by get_house



# Lambda function  - an annonymus function
# if we are not using a function again, but just once, then lambda function can be used

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}  
        students.append(student)    

for stu in sorted(students, key=lambda student:student["name"] ):     
    print (f"{stu['name']} is in {stu['house']}")

# lambda is given a parameter "student" is called on every one of dictionary in that list,
#  given a student, it indexes into that dictionary get their name
# lambda student:student["name"]     does defining the function all in one line
    # no def, no (), no function name
# which i didnt understand still
# as many lambda functions can be used






# when file has three and some 2 words in csv files, it causes more errors 
# using a library to read and write CSV files
# python has a module called "CSV"
# docs.python.org/3/library/csv.html

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)               # file is iterated by the reader, loading as list of columns
    for name, home in reader:               # name and home details are separated by reader
        students.append({ "name" : name, "home": home}) 

for stu in sorted(students, key=lambda student:student["name"] ):     
    print (f"{stu['name']} is in {stu['home']}")

# csv module comes with a function called reader to read the csv file 
# it figures out the commas, corner cases, quotes and deal with it

# ok this is bit too confusing now
    #
        #
            #     


# a reader returns lists
# when csv has headers specifying headers for the data under it,
# DictReader can be used
# file is iterated by the DictReader, loading as Dictionary of columns
# even without if the order is mixed, it always calls name

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)              
    for name, home in reader:              
        students.append({ "name" : row["name"], "home": row["home"]})   # since it returns rows, "name": row["name"] 

for stu in sorted(students, key=lambda student:student["name"] ):     
    print (f"{stu['name']} is in {stu['home']}")







# csv.write

import csv

name = input ("what's your name? ")
home = input ("where is your home? ")

with open("students.csv", "a") as file:
    w = csv.writer(file)
    w.writerow( [name, home] )    # the argument would be the line i want to write into the list



# csv DictWriter

import csv

name = input ("what's your name? ")
home = input ("where is your home? ")

with open("students.csv", "a") as file:
    w = csv.DictWriter(file, fieldnames=["name", "home"])
    w.writerow( { "name": name, "home": home} )





# images, PIL library
# image library  -  pillow.readerdocs.io

# creating animated gif
# ok i dont have PIL, ill just copy code
"""
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:      #argv is a list, so to take a slice [1: ]
    image = Image.open(argv)
    images.append(image)

images[0].save( 
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
"""

# file I/O ends at 8h 32m