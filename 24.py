#finally keyword
def fun():
    try:
        l=[1,5,6,7]
        i=int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error")
        return 0
    finally:
        print("👍")  
        
x=fun()
print(x)



#Raising value error