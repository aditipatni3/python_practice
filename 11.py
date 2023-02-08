#printing tables by using break and continue;
#break means loop ko chor k nikal jao
#continue means iteration lo chor k nikal jao

#using for with break to print table of 5 till 10

for i in range(1,15):
    if(i==11):
        break
    print("5 * ", i, "=", 5*i)
    
#using while 
k=1
while(k<=15):
    if(k==11):
        break
    print("5 * ", k, "=", 5*k)
    k=k+1
    
    
#using continue

for i in range(1,15):
    if(i==11):
        continue
    print("5 * ", i, "=", 5*i)
    
    
#using continue with while    
# k=1
# while(k<=15):
#     if(k==11):
#         continue
#     print("5 * ", k, "=", 5*k)
#     k=k+1