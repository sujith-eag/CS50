# starts at 15h 6m

# map

def main():
    yell(["This", "is", "CS50"])    # passing a list

def yell(words):
    uppercase = []
    for word in words:
        uppercase.append(word.upper())  # turning to uppercase
    print(*uppercase)                   # printing the list without , or "" directly

if __name__ == "__main__":
    main()




def main():
    yell("This", "is", "CS50")      # passing 3 arguments, not a list

def yell(*words):                   # * allowing for variable arguments, passing as many things
    uppercase = []
    for word in words:
        uppercase.append(word.upper())
    print(*uppercase)                   # printing the list without , or "" directly

if __name__ == "__main__":
    main()



# map
# is a function that allows you to map or apply some function to every element of some sequence
# docs.python.org/3/library/functions.html#map
# map(function, iterable, ...)

# trying to apply uppercase function to all elements


def main():
    yell("This", "is", "CS50")      

def yell(*words):                    
    uppercase = map(str.upper, words)          # str.upper is passed to map, map will call it and apply the () to all words
    print(*uppercase)                   # it will iterate over all the words, call str.upper on all, makes a new list

if __name__ == "__main__":
    main()



# list comprehensions
# constructing a list without append

def main():
    yell("This", "is", "CS50")      

def yell(*words):                    
    uppercase = [word.upper() for word in words]   # defining a list comprehension 
    print(*uppercase)                              # reading from left to right

if __name__ == "__main__":
    main()




# sorting using list comprehension

students = [
    {"name": "Hermione", "house": "Gryffindor" },
    {"name": "Harry", "house": "Gryffindor" },
    {"name": "Ron", "house": "Gryffindor" },
    {"name": "Draco", "house": "Slytherin" },
    {"name": "Padma", "house": "Ravenclaw" } 
]

gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor" ]
    # gryffindors is, zero or more students name,    (student["name"]) 
    # it is result of itirating over each of the items in students,   (for student in students)
    # only including in the final results the students whose house is gryffindor (if student["house"] == "Gryffindor")

for gryffindor in sorted(gryffindors):   # sorting the gryffindors
    print(gryffindor)





# filter
# filter (function, iterable)
# docs.python.org/3/library/functions.html#filter


students = [
    {"name": "Hermione", "house": "Gryffindor" },
    {"name": "Harry", "house": "Gryffindor" },
    {"name": "Ron", "house": "Gryffindor" },
    {"name": "Draco", "house": "Slytherin" },
    {"name": "Padma", "house": "Ravenclaw" } 
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"       # if s["house"] == "Gryffindor":
                                            #     return True
                                            # else:
                                            #    return False

gryffindors = filter(is_gryffindor, students)  # is_gryffindor is called and applied each element in the sequence

for gryffindor in gryffindors:      #for gryffindor in sorted(gryffindors, key:lambda s: s["name"]):
    print(gryffindor["name"])





students = [
    {"name": "Hermione", "house": "Gryffindor" },
    {"name": "Harry", "house": "Gryffindor" },
    {"name": "Ron", "house": "Gryffindor" },
    {"name": "Draco", "house": "Slytherin" },
    {"name": "Padma", "house": "Ravenclaw" } 
]

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])





# dictionary comprehensions
# to create a dictionary on the fly without creating a empty dict{} beforehand


students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append ({"name": student, "house": "Gryffindor"})

print(gryffindors)

# this creates a list of dictionaries like the one above with name of students



# another way

students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print (gryffindors)

"""
output is 
[{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, 
{'name': 'Ron', 'house': 'Gryffindor'}] 
"""

# making just one dictionary, with key is name
# using dictionary comprehension

students = ["Hermione", "Harry", "Ron"]

gryffindors = { student: "Gryffindor" for student in students}

print (gryffindors)

# output is
# {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}


# ends at 15h 35m
