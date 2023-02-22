#exception handling
a=(input("enter the value of a:"))
try:
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)}*i)")
except:
    print("error ")
    
print("💕")