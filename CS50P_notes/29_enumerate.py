# starts at 15h 35m

# enumerate
# enumerate(iterable, start=0)

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print (i + 1, students[i])


# using enumerate

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print (i + 1, student)



# generators
# ability to generate memory

def main():
    n= int(input("what's n? "))
    for i in range(n):
        print("image" * i)

if __name__ == "__main__":
    main()





def main():
    n= int(input("what's n? "))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    return "image" * n
 
if __name__ == "__main__":
    main()





def main():
    n= int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("image" * i)
    return flock
 
if __name__ == "__main__":
    main()





# generators
# docs.python.org/3/howto/functional.html#generators

# yield
# most of the values returned by functions are by yield
# when there is more memory and has to be returned at once, it can be problem with memory


def main():
    n= int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        return "image" * i   # when value is returned in a for loop, it will exit the loop
                              # without returning any value  
if __name__ == "__main__":
    main()




# using one value at a time, and the for loop will keep working

def main():
    n= int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "image" * i
                    
if __name__ == "__main__":
    main()




# iterators
# yield returning an iterator that allows the code and for loop to iterate over these generated value one at a time


# The end of CS50
