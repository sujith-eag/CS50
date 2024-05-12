
# more on thinking of implimenting things
# using mario world

# printing the 3 colums
"""
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
"""
# so the will be 3#



"""
def main():
    print_column(3)

def print_column(height):   
    print("#\n" * height, end="")
"""
# same thing of 3#


# 4 in row
"""
def main():
    print_row(4)

def print_row(width):
    print("?" * width)
"""


# a 3 by 3 block
"""
def main():
    print_square(3)
    
def print_square(size):
    for i in range(size):           # for each row in square
        for j in range(size):       # for each brick in row
            print("#", end="")      # print brick, without
        print()                     # print without argument moves to a line 
"""
# no idea whats happening here


# ok finally it came to the point of printing 3 and doing it for 3 time
# still kind of finding this "for _ in range()" difficult to see
"""
def main():
    print_square(3)
    
def print_square(size):
    for i in range(size):                       
        print("#" * size)
main()
"""

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()

# ok this is more confusing, what is doing what??

# end of Lecture-2 at 4h 7m