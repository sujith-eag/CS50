# regular expressions  regexes
# to define patterns and compare them against data to validate and clean them


# "re" is the library for regular expressions
# this library allows define, check for patterns, check and replace
# docs.python.org/3/library/re.html

# " re.search(pattern, string, flags=0) "      #the most versatile function

# the patterns in the re.search can take a lot of special symbols to define its action
"""
.    any character except a newline

*    0 or more repititions
+    1 or more repititions
?    0 or 1 repetition

{m}  m repetitions
{m,n} m-n repetitions

^  matches the start of the string
$  matches the end of the string or just before the newline at the end of the string
so ^ is beginnig and $ is the end
"""





# checking with regular expressions to find limitations
# New way of checking simultaneously if two characters are in the input

email = input("whats your email? ").strip()
if "@" in email and "." in email:        # if "@" in email:
    print("valid")
else:
    print("invalid")

# easy to check and miss with this



email = input ( "what is your email? " ).strip()
username, domain= email.split("@")

if username and "." in domain:   # two boolian expression checking data in username, "." in domain 
    print("valid")               # if there then it will be true so valid
else:                   
    print("invalid")



# to check if it ends with .edu
# "if" "and" using .endswith for domain

email = input ( "what is your email? " ).strip()
username, domain= email.split("@")

if username and domain.endswith("edu"):    
    print("valid")            
else:                   
    print("invalid")

# it will take a lot to properly validate this even if it is simple




# "re" is the library for regular expressions
# this library allows define, check for patterns, check and replace
# docs.python.org/3/library/re.html


# " re.search(pattern, string, flags=0) "      #the most versatile function
# pattern is the patterns you want to search for
# strings are specific search in string
# flags is like passing arguments to modify the behaviour of the function



# first step in re library

import re

email = input ( "what is your email? " ).strip()

if re.search("@", email):
    print("valid")
else:
    print("invalid")



"""
.    any character except a newline  (to check if there is any character or alphabet)

*    0 or more repititions
+    1 or more repititions   (atleast one or more of a character)
?    0 or 1 repetition

{m}  m repetitions
{m,n} m-n repetitions (m through n repetition)

^  matches the start of the string
$  matches the end of the string or just before the newline at the end of the string
"""

#  ".*@.*" . indicates any character,
# .*@ is saying anything to left similarly also at right
# name@ will be valid because * menas even if there are 0 repetition its true

import re

email = input ( "what is your email? " ).strip()

if re.search(".*@.*", email):
    print("valid")
else:
    print("invalid")



# using + instead of * to validate repetition of characters

import re

email = input ( "what is your email? " ).strip()

if re.search(".+@.+", email):
    print("valid")
else:
    print("invalid")

# it could have been "..*@..*"
# the first . means any character, .@ means 0 or more character
# anyway + exists


# (".+@.+", email)  suppose i want to check .edu also
# (".+@.+.edu", email)  here the second . in .edu will be considered as any character so ?edu will also be valid
# (".+@.+\.edu", email )  using \ an escape character makes python understand its a actual .edu
# \ says what follows is not a special symbol but a literal symbol, it escapes the symbol
#  to make sure python doesnt treat it as a escape sequense, single new line
# (r".+@.+\.edu", email)  the r in the beginning says this is a raw string, r string, 
# to take it literally, no interpretation, 
# using r string for all regular expression is a good habit

import re

email = input ( "what is your email? " ).strip()

if re.search(r".+@.+\.edu", email):
    print("valid")
else:
    print("invalid")

# @@@@ will also be valid
# my email edress is name@.edu. is also vaid

# validating is very important


import re

email = input ( "what is your email? " ).strip()

if re.search(r"^.+@.+\.edu$", email):
    print("valid")
else:
    print("invalid")

# now ^ and $ are specifying that just ^.+@.+\.edu$ this is for this expression

# [] allows for a set of character in the expression
#  example [abcde] these are allowed
# [^] says anything exept this is allowed
# example [^@]  here @ is not allowed

#   r"^.+@.+\.edu$"  here . means any character, replacing that with [^@]
#   r"^[^@]+@[^@]+\.edu$"  this allows avoiding @ at right and left of @


import re

email = input ( "what is your email? " ).strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("valid")
else:
    print("invalid")

# this expression is very accomodating of every character except @


# we can allow what is allow which might be like [abcde...], not practical
# we can do a range
# [0-9a-zA-Z_] no comma, space or separators or that also gets included
# these are all allowed, because there is no ^
# replacing [^@] with this, this will be more restrictive

import re

email = input ( "what is your email? " ).strip()

if re.search(r"^[0-9a-zA-Z_]+@[0-9a-zA-Z_]+\.edu$", email):
    print("valid")
else:
    print("invalid")


# this is the world of Regular Expressions

# [0-9a-zA-Z_] has a shortcut \w   represents a word caracter (alphanumaric character and _)

import re

email = input ( "what is your email? " ).strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("valid")
else:
    print("invalid")


# there are more shortcuts

"""
\d  any decimal digit
\D  not a decimal digit
\s  whitespace characters
\S  not a white space character
\w  word character.. as well as numbers and underscore
\W  not a word character
"""
"""
A|B  either A or B
(...) a group
(?:..) non-capturing version

example   r"^\w+@\w+\.edu$" can be r"^\w+@\w+\.(edu|net|gov|org|com)$"  making it a list
  if space also has to be included (\w|\s)  including word characters and white space
  r"^(\w|\s)+@\w+\.edu$"
"""


# even though \w is used it wont accept capital because of .edu which is specified
# it can be handled by forcing all data to be in lower email.lower()  or .lower() at input

# we can handle this with the last of the arguments in re.search(pattern, string, flags=0)
# flags expression that can be used are
"""
re.IGNORECASE    it ignores the case
re.MULTILINE     matching multiple lines
re.DOTALL         any character plus new line 
"""


# to make capital acceptable

import re

email = input ( "what is your email? " ).strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")


# to make . acceptable by grouping
# specifying some sub group as optional using ? 
# which means it can be there or not there
# so adding (\w+\.)? says . can be there or might not be  
# without () it might mean only . is optional, now cs50. is also optional
# (r"^\w+@(\w+\.)?w+\.edu$", email, re.IGNORECASE)


# the actual browser expression
# ^[a-zA-Z0-9.!#$%&'*+\/=?_`{|}~-]+@[a-zA-z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

# better find a library that does it


# few more expressions
"""
re.match(pattern, string, flag=0)   it matches from the start of the string witout ^ symbol
re.fillmatch(pattern, string, flag=0)   matches at start and end witout ^ or $
"""


# ends at 9h 46m
