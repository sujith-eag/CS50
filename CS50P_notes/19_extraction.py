# starting at 10h 5m

# We have validated the data according to a certain pattern 
# cleaned up the input and changed it up
# now extracting the user data and cleaning it


# using re.sub() and re.search()  to clearup data


# trying to get username from the url
# variable.replace()  has two parameters, what you want to replace and what u want to replace it with
# the basic front of url is being replaced with "" nothing

url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "")
print (f"Username: {username}")

# doesnt work if it is http, there is some sentence befor this, or additional ? or links
# using variable.removeprefix()  it has one argument , what to be removed
# but didnt do much, these are basic string functions

url = input("URL: ").strip()
username = url.removeprefix("https://twitter.com/", "")
print (f"Username: {username}")




# regular expressions allow you to express the patterns and goals specifically and capture
# re.sub(pattern, repl, string, count=0, flag=0)
# substitute
# (pattern you want to look for, replace that with, where you want to do it(variable))
# its basically find and replace and giving back the value
# typing in (r" ") making it raw string, literal string in regular expression

import re

url = input("URL: ").strip()

username = re.sub(r"^https://twitter\.com/", "", url)    # having \. to escape this
print(f"Username: {username}")

# just a ^ because we want to match from the beginning, we want the username at the end, so no $
# having \. to escape this in twitter\.com because . means any character 
# so without \ even twitter!com twitter?com will be valid
# any data like special symbols like . $ need to be escaped like \. \$



# if it has http or https
username = re.sub(r"^(https|http)://twitter\.com/", "", url)  
# saying http or https
# or using ? to say s is optional
username = re.sub(r"^https?://twitter\.com/", "", url)

# if there is www. or not so making it optional
# by grouping it, with () and also \ for .
username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url)

# maybe there will not be a protocall,  optionals can be nested (?)?
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

#it can also be (www\.|) means www\ or nothing is accepted
# but (www\.)? is more readable






# using re.search now to do the same now, saying T or F, here is username or not
# (.+) is used to capture the data

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))   # if it is group (1) that is (www.), (.+) is group(2)

# if google.com is there it wont run, only if matches contain twitter.com
# only then its True, and data is returned
 

# using Walrus operator

if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(2))   
# if it is group (1) that is (www.), (.+) is group(2)


# using () capturing or (?:) non capturing groups to reduce confusion in groups
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))


# saying what is acceptable in data at (.+) by using whats accepted [a-z0-9_] in . place we are ignoring case
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))


# other re functions

# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)

# this is kind of new language used in JS, ruby etc to clean up data

# ends at 10h 38m

