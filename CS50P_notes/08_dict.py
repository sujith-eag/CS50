# Dictionary at 3h 32m

# Associates a value with another value,  like words and meanings in a dictionary
# having multiple lists [] isnt practical

# new syntax, {} for dictionary   # {} was used in f strings, format strings

"""
students = { }   
# empty dictionary
"""


"""
students = {Harry:Gryffindor, Hermione: gryffindor, Draco:Slytherin }
    # forgot that the names are strings, not formated properly
"""


# better formating,  keys : values, : is the separator
# list[] have numbers to index into them, but dict{} allows the actual words to be used as indecies to get their values
# to get draco values, we can use draco as the key
"""
students = {
    "Harry" : "Gryffindor", 
    "Hermione" : "gryffindor", 
    "Draco" : "Slytherin" }

print(students["Hermione"])
print(students["Draco"])
"""



"""
students = {
    "Harry" : "Gryffindor", 
    "Hermione" : "gryffindor", 
    "Draco" : "Slytherin" }

for student in students:
    print(student)
"""
# by default the dic{} only the keys are read so only names are displayed


"""
students = {
    "Harry" : "Gryffindor", 
    "Hermione" : "gryffindor", 
    "Draco" : "Slytherin" }

for student in students:
    print(student, students[student], sep=", ")
"""
# students[student] is using the name as key to get the associated value



# list of dict{}
# keyword "None" with capital N, which represents absense of value, without " "
# all dict{} are given same key words but differnt values, by design
# keys are standardised to find things easily

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus":"Otter" },
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag" }, 
    {"name": "Ron", "house": "Gryffindor", "patronus": "Terrier" }, 
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# using print(students["name"]) will give a str, but it must be int
# "for" will get first value which is dict{} 0, to student
# print(student["name"]) will get the value of key word "name" 

# kind of confusing

# Ends at 3h 50m