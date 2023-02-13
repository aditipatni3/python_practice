#FOR LOOP WITH ELSE
# for loop execute hoga phir else aayega
for i in range(5):
    print(i)
else:
    print("❤️")

print("\n")

#FOR LOOP WITH ELSE AND BREAK STATEMENT
#Break k karan loop ends and else doesn't execute
for i in range(7):
    print(i)
    if(i==4):
        break
    
else:
    print("❤️")
print("\n")
    
#FOR LOOP WIT ELSE AND CONTINUE STATEMENT
for i in range(7):
    print(i)
    if(i==4):
        continue
    
else:
    print("❤️")
    
#WHILE LOOP WITH ELSE
i=0
while i<7:
    print(i)
    i=i+1
else:
    print("😊")


#while loop with break
i=0
while i<7:
    print(i)
    i=i+1
    if(i==4):
        break
else:
    print("😊")