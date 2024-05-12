"""
def main():
    ans = input ("What is the answer to the great question of life?  ")
    is_it(ans)

def is_it (data):
    if data == ("forty_two"):
        print ("yes")
    elif data == ("forty two"):
        print ("yes")
    elif data == ("42"):
        print ("yes")
    else: print ("no")

main()
"""

# second attempt
"""
def main():
    while True:
        ans = input ("What is the answer to the great question of life?  ")
        if ans == ("forty_two") :
            print ("yes")
        elif ans == ("forty two"):
            print ("yes")
        elif ans == ("42"):
            print ("yes")
            break
    else: print ("no")

main()
"""
# its prompting second time after the answer but
#for some reason the second method isnt giving a no





# get the input, Clean the input
# if input is equal yes, otherwise no

ans = input("What is the answer to the great question of life?  ")
ans = ans.lower().strip()

if (ans == "42" or ans == "forty two" or ans == "forty_two"):
    print("yes")
else:
    print("no")
