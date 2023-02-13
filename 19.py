#exception handling
a=int(input("enter the value of a:"))
try:
    for i in range(1,11):
        print(f"{a}x{i}={a*i}")
except:
    print("error as ")
    
print("👍")