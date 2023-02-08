#match case in python

a=int(input("enter the value of a:"))
match a:
    case 0:
        print("a is zero ")
    case 4:
        print("a is 4")
    case _:
        print("a is:",a )