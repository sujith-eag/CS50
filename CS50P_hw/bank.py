# Hello is 0$
# with H is 20$
# anything else is 100$

#get input, strip, lower case
# if (it starts with h, (if its hello, 0$), else it is 20$) else it is 100$

greet = input("Greeting: ").strip().lower()

if (greet.startswith("h")):
    if (greet.startswith("hello")):
        print("0$")
    else:
        print("20$")

else:
    print("100$")



# im thinking too much, over planning
"""
def main():
    greet=input( )
    f, l = greet.split(" ")
    check(f)

def check(n):
    n=="hello"
    print("0$")
"""