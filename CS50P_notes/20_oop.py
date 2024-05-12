# starts at 10h 38m

# Object oriented Programming

# Procedural coding, step by step
# functional programming, passing on functions



# into to "Tuple"
# its an immutable list
# when two things are returned at once it forms a tuple

def main():
    name, house = get_student()
    print(f"{name} of {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()




# the return of name, house seperated by a comma is coming as a tuple list
# it can be passed to a single variable like student 
# then it can be indexed into using [0] [1]

def main():
    student = get_student()
    print (f"{student[0]} from {student[1]}")     # why are you putting = for print??

def get_student():
    name = input("Student: ")
    house = input("House: ")
    return name, house

if __name__=="__main__":
    main()

# tuples do not allow for the values to be changed so 
# when programming defensively, not wanting any data modification we can use tuple



# trying to change the value of the tuple

def main():
    student = get_student()
    if student[0] == "padma":               # suppose the user inputs padma and griffindor
        student[1] = "Ravenclaw"            # we want it to change to "Ravenclaw"
    print (f"{student[0]} from {student[1]}")   # tuple cant be changed like this
                                    # so it will cause TypeError(using wrong type)
def get_student():              # 'tuple' object does not support item assigment
    name = input("Student: ")   # we have to use a list then to edit this
    house = input("House: ")
    return name, house          # return [name, house]   will pass a list, it is mutable
                                # return (name, house) is a tuple

if __name__=="__main__":
    main()




# Using dictionary which uses keys as call option so order doesnt matter
# allows better symantics, name is name and house will be house

def main():
    student = get_student()
    print(f"{student['name']} of {student['house']}")  # careful not to use "" inside "" to name a key
                                                      # "{student["name"]} " will cause error
def get_student():
    student = {}                        # first define a dict as student
    student["name"] = input("Name: ")   # then for a key value get the input
    student["house"] = input("House: ") # harry will be assigned to name , ie  name:harry
    return student                      # return the dict of student

if __name__=="__main__":
    main()


# to not create unnesasary variables, some cleaning
# also having conditionals to change house of padma (possible as it will be dict now)

def main():
    student = get_student()
    if student["name"]=="Padma":
        student["house"]="Ravenclaw"

    print(f"{student['name']} of {student['house']}")
                                                    
def get_student():
    name = input("Name: ")                 #student = {}                        
    house = input("House: ")               #student["name"] = input("Name: ")   
    return {"name": name, "house":house}   #student["house"] = input("House: ") 
                                           #return student                      

if __name__=="__main__":
    main()

