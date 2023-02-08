#for loop

name="Aditi"
for letter in name:
    print(letter, end=",")
    
    
    
#iterating through a list
colors=["red", "yellow", "blue", "green"]
for color in colors:
    print("\n",color)
    for i in color:
        print(i)
        
        
for char in colors:
    for c in char:
        print(c)
        
        
        
#range() in for loops:
for a in range(20):
    print(a)
    
    
for b in range(2,10):
    print(b)
    
for d in range(1,10,2):  #step functions can b used to prnt multiplication table
    print(d)