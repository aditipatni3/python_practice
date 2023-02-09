import time
t=time.strftime('%H:%M:%S')
print(t)
hour=int(time.strftime('%H'))
print(hour)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)

if(hour>=0 and hour<12 ):
    print("good morning aditi!!")
elif(hour>=12 and hour<16):
    print("good afternoon aditi!!")
elif(hour>=16 and hour<0):
    print("goood night aditii!!")