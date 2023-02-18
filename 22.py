import re
#backslash problem solved using regex
randomString="here is \\backslash"
print(randomString)
#output is "here is \backslash"

#to solve it:
print(re.search(r"\\backslash", randomString))


#REPLACING NEW LINE CHARACTER WITH JUST A SPACE
str='''
hey
keep the flag
of India
always
high
in the sky'''
print(str)

regex=re.compile("\n")
str=regex.sub(" ", str)
print(str)