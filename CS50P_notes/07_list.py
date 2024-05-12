# Starting on "list"        at 3h 20m

# list of values to work with more data

"""
students = ["Hermione", "Harry", "Ron"]             # names are strings so ""
print(students)                                     # prints everything including []
"""



"""
students = ["Hermione", "Harry", "Ron"]
print (students[0])
print (students[1])
print (students[2])
"""
# gives all names in separate line
# the lists in python are 0 indent, zero is the first items place
# to call a specific object in a list, [] and its place number can be given



# using "for" loop to iterate over strings also
# all are printed even without knowing how many are in the list
"""
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)
"""
# the initialisation of "student" variable happened automatically in the loop
# "for" loop will initialise it to each name in sequence
# better to name variable "student" than "_" because we are using it



# "for loop" iterates over things in a list
for i in [0, 1, 2]:
    print ("meow")

# for creates a variable like "i",
# then it assigns "i" the first thing in the list
# then the second and soforth with the underlying code also

for i in range(3):
    print ("meow")
# we introduced range instead of mannual list to give values





# range expects an integer so range(students) wouldnt work
# "len()" is length function which will tell you the length of a list
"""
students = ["Hermione", "Harry", "Ron"]
for i in range (len(students)):
    print(i)
"""
# this will give me 0, 1, 2 because thats what is coming from len(student) when "for" loopes


"""
students = ["Hermione", "Harry", "Ron"]
for i in range (len(students)):
    print(students[i])
"""
# now 0 of list gets printed and other numbers in sequence


"""
students = ["Hermione", "Harry", "Ron"]
for i in range (len(students)):
    print(i+1, students[i])
"""
# print is given one more argument, it will automatically add space to it
# its "i+1" because first number will be 0 otherwise

