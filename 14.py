#kaun banega crorepati
question=["How many months are there in a year?", "which number comes after 15", "how many vowels are there in english alphabet", "Which sense organ do you use to smell?", "which animal has a long neck?"]
answer=[12, 16,5, "nose", "giraffe"]
options=[12, 11, 13, 15, 14, 16, 13, 20, 3, 4, 5, 6, "nose", "eyes", "tongue", "ears","giraffe", "mice", "elephant", "lion"]
money=0
print(question[0])
print(options[0:4])
guess=int(input("enter your choice"))
match guess:
    case 12:
        print("your answer is correct")
        money=money+10
        print("you won rupees", money)
    case 11:
        print("wrong")
    case 13:
        print("wrong")
    case 15:
        print("wrong")
            
            
print(question[1])
print(options[4:8])
guess=int(input("enter your choice"))
if guess==answer[1]:
    print("your answer is correct")
    money=money+10
    print("you won rupees", money)
else:
    print("wrong")
    
    
print(question[2])
print(options[8:12])
guess=int(input("enter your choice"))
if guess==answer[2]:
    print("your answer is correct")
    money=money+10
    print("you won rupees", money)
else:
    print("wrong")
    
    
    
print(question[3])
print(options[12:16])
guess=input("enter your choice")
if guess==answer[3]:
    print("your answer is correct")
    money=money+10
    print("you won rupees", money)
else:
    print("wrong")
    
    
print(question[4])
print(options[16:20])
guess=input("enter your choice")
if guess==answer[4]:
    print("your answer is correct")
    money=money+10
    print("you won rupees", money)
else:
    print("wrong")