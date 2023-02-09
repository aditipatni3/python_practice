#recursion

def factorial(n):
    ''' this is a doctring'''
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))
print(factorial.__doc__) #docstring can be printed and hence it is not just a comment.



def fibonacci(n):
    '''adding prev number'''
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
    
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))


