#strings
name="Harry"
print("my name is", name)



#printing any index
print(name[0])
# print(name[5]) throws an error because 5th index doesn't exist.


#for multi line strings
apple="""lorem snb
ds
dw
affg"""
print(apple)


#looping through the string
for character in apple:
    print(character)
    
    

#length of string
print(len(apple))
print(len(name))

hello="world"
hellolen=len(hello)
print(hellolen)



#string slicing
names=("harry, subham, aditi, rohan")
print(names[0:5]) #including 0 but not 5
print(names[:9])
print(names[3:12])
print(names[:])


#negative slicing
print(names[0:-5])  #this means len(names)-5=15===names[0:15]
#in case you try to print names[-1:-3], it won't print, because printing 14 to 12 doesn't make any sense.
nm="harry"
print(nm[-4:-2])


#upper case conversion
print(nm.upper())
print(nm)               #this means string nm isn't changed, as strings are immutable.

str1="AbCdefGhijkLMNOPqrsTuvwxYZ"
print(str1.upper())
print(str1.lower())



#rstrip() used t remove trailing characters
str="hello world!!!!!!!"
print(str.rstrip("!"))



#replace() used to replace one from another
print(str.replace("world", "aditi"))



#split() between spaces and creates a list
a="hi i am your friend. Hello"
print(a.split(" "))



#to capitalize first lettter of the string we use "capitalize()"
print(a.capitalize())



#center() to centralize a string
print(a.center(50))
print(len(a))
print(len(a.center(50)))




#count() to count how many times  a given alue appears in the string.
print(a.count("i"))



#endswith() is used to return a bool value if the string ends or not with the mentioned value
print(a.endswith("!!!"))
print(a.endswith("Hello"))
print(a.endswith("ur", 3, 11))
print(a.endswith("ur", 3, 12))#taking an extra index returns true as 12th isn't counted



#find() is used to search first occurence of a value and returns its index else returns -1
print(a.find("am"))
print(a.find("denise"))
print(a.find("ur"))


#index() similar to find() but instead of returning -1 when string not found, it throws error
# print(a.index("den"))


#isalnum() returns true if the string is made up of A-Z, a-z, 0-9
a="hi i am your friend. Hello"
print(a.isalnum())
c="asbhbviJWNI121344ini"
print(c.isalnum())


#isalpha() returns true only if A-Z and a-z
print(c.isalpha())
d="ajbabiNIBBLIjbsbd"
print(d.isalpha())


#islower() and isupper() used to check if all letters are lower or upper respectively
e="bbeivb"
f="JNNIWVE"
print(e.islower())
print(e.isupper())
print(f.islower())
print(f.isupper())

#isspace() returns true if whitespace is present
print(a.isspace()) #returned false
g="        "
print(g.isspace()) #returned true


#istitle() returns true only oif first letter of each word in the string is capitalized
h="Hello This Is Title"
print(h.istitle())
print(f.istitle()) #returns false if any otherr letter is caps tooo
