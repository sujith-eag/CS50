#unit tests

# writing code to test the code we have written
 
# "assert" is keyword which asserts something is true
#  if its not true, there will be an "AssertionError"

"""
from calculator import square    # import square from calculator, this doesnt work??

def main():
    test_square()

def test_square():
    assert square(2) == 4    # the square was supposed to be imported from another function 
    assert square(3) == 9    # insted of    if square(2) != 4:
                             #                   print("2 squared was not 4")    better to use assert 

if __name__ == "__main__":
    main()
"""


"""
from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:    
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
"""
# there is more code than using "if", but "assert" is used and error is handled
# more code to test two lines of code




# "pytest" is the tool which can be used to test the code
# there are more built into python
# pytest will handel the try, except and printing which are standard procedure
# pytest can be installed by "pip install pytest"
# docs.pytest.org
"""
from calculator import square

def test_square():
    assert square(2)==4
    assert square(-2)==4
    assert square(3)==9
    assert square(0)==0
"""
# some issue because im not able to import from calculator as it is not being shown 

# the program is run in command line as
# "pytest filename.py"
# anyway mine didnt work

# breaking the logic into various fuctions allows for easy testing and debugging
# with logic all over the program itll be difficult to find or fix
# each function should have well defined input and well defined output

# the test square can be divided into few more categories like possitive and negative





# testing one more with string
"""
def main():
    name = input (" whats your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

if __name__ == "__main__":
    main()
"""
    
# testing program

"""from hello import hello

def test_hello():
    hello("David") == "hello, David"
"""
 # this will fail because testing program is testing the output handed by the hello program
 # but hello is not returning anything,
 # its effects are just "side effcts", printing on the screen, nothing is returned so nothing to test

 # its best practice to reduce "side effects"

 # so insted of
 # print( " hello,", to)
 # return f"hello, {to}"   then print in main()




# "package"
# package is python module, multiple module


# ending at 7h 