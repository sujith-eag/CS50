# about importing functions from own libraries and files


def main():
        hello("world")
        goodbye("world")
        
def hello(name):
        print(f"hello, {name}")

def goodbye(name):
        print(f"goodbye, {name}")   # it printed goodbye {"world"} because i left {name} outside "" even when it was f string

main()

# i was supposed to save this in separate file so i can import function but ill keep it here for clarity


# a different program to import function
"""
import sys    #so command line argument can be run

from 4import import hello     # 4import is the file name

if len(sys.argv()) == 2:
    hello(sys.argv[1])
"""
# when function is run in command line with file name and person name
# it prints all hello world, goodbye world and hello name
#happened because when python went to get the function and read the file from top to bottom
# the main() function without any conditional gets called also
# to avoid that __name__ is used





def main():
        hello("world")
        goodbye("world")
        
def hello(name):
        print(f"hello, {name}")

def goodbye(name):
        print(f"goodbye, {name}")

if  __name__ == "__main__":    # __name__ is a function  "__main__" is a string
        main()


# __name__ is a variable whose variable is automatically set to main when the file is run through the command line
# so it becomes "__main__" == "__main__"

# when function gets imported from another file but its not called directly from command line,
# main == main wont satisfy so main() wont be called with another program



"""
import sys

from 4import import goodbye

if len(sys.argv()) == 2:
    goodbye(sys.argv[1])
"""


# week three ended at 6h 9m