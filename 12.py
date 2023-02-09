#functions

def gmean(a,b):
    gm=(a*b)/(a+b)
    print(gm)
    
gmean(3,4)
gmean(5,6)

def isgreater(c,d):
    if(c>d):
        print(c," is grreater ")
    else:
        print(d,"is greater or the numbers are equal")
        
isgreater(3,4)
isgreater(5,3)
isgreater(6,6)

#function arguments

#1. Required arguments 
def islesser(a,b=9):
    
    if(a<b):
        print(a," is lesser ")
    else:
        print(b,"is lesser or the numbers are equal")
        
islesser(3)
islesser(10,4)
#ialesser(b=4) can't be calculated because we need one value for a