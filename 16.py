#sets- unorder collection of data items - do not contain dulicate items- enclosd within { }
cities1={"delhi", "bangalore", "kolkata", "hyderabad","chennai", "coimbatore"}
# print (cities1)
cities2={"delhi", "bangalore", "coimbatore", "gurgaon", "indore", "surat"}
# print(cities2)
# print(len(cities1))
# print(len(cities2))
# print(type(cities1))

#to print a null set
city=set()
print(city)

#union() and update()
 
# print("cityies1=",cities1.union(cities2))
# print("1=",cities1)
# print("2=",cities2)

# cities1.update(cities2)
# print(cities1)

#to add a single item
cities1.add("mumbai")
print(cities1)


#remove()-raises an error if element not present / discard()-no error
# cities1.remove("mumbai")
# print(cities1)

# cities1.remove("indore")-------error
# print(cities1)

# cities1.discard("indore")-----no existence
# print(cities1)


# cities1.discard("delhi")
# print(cities1)



#to delete the entire set
# del(cities1)
# print(cities1)

#to remove last item of the set ---pop()
# item=cities1.pop()
# print(item)
# print(cities1)

#issubset()--all the items of cities 2 present in cities1???
print(cities2.issubset(cities1))

#issuperset()
print(cities2.issuperset(cities1))

