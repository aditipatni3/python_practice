import re
#backslash problem solved using regex
randomString="here is \\backslash"
print(randomString)
#output is "here is \backslash"

#to solve it:
print(re.search(r"\\backslash", randomString))