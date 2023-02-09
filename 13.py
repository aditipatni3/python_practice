#list-collection of items 

colors=["red", "yellow", "blue", "green", "black", "pink", "orange", "brown"]
print(colors)
print(len(colors))

print(colors[0])
print(colors[2:7])
print(colors[1:7:2])#jumpindex

#to check if an item is present in the list
if "yellow" in colors:
    print("yes")
else:
    print("no")
    
    
    
if "violet" in colors:
    print("yes")
else:
    print("no")
    
    
#list comprehension
colorsWith_o=[color for color in colors if "o" in color ]
print(colorsWith_o)


lst=[i for i in range(5)]
print(lst)


#                            LIST METHODS
l=[1, 2, 3, 4, 5, 6, 7, 8]
print(l)

#to add one more element at the end of list l
l.append(9)
print(l)

#to sort list in ascending order
l.sort()
print(l)

#to sort in descenong order
l.sort(reverse=True)
print(l)

#to find what is at index[1] for eg
print(l.index(1))

#to count how many times an item is present in list
print(l.count(7))

#to copy a list to another list
m=l.copy()
print(m)
m[0]=0
print(m)

#to insert an element at a given index
l.insert(3, "green")
print(l)

#to join two lists
m=[1000, 1100, 1200, 1300, 1400, 1500]
l.extend(m)
print(l)

#to make no changes to oiginal list you can concatenate 
k=l+m
print(k)