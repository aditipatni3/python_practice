#dictionaries

dic1={"name":"aditi", "age":21, "Indian":True}
# print(dic1)
# print(dic1.items())
# print(dic1.keys())   #to print keys
# print(dic1.values()) #to print values

# print(dic1["name"])

# #to check if key exists
# print(dic1.get('eligible'))
# print(dic1.get('Indian'))

print(dic1.items())
#iteration 
for key, value in dic1.items():
    print(f"the value corresponding to the key {key} is {value}")  #f-string
    
#dictionary methods

#update
dic1.update({"age":22})
print(dic1)

dic1.update({"dob":3})
print(dic1)

dic2={"hello":"world", "my":"name"}
dic1.update(dic2)
print(dic1)

#clear()
dic2.clear()
print(dic2)


#to print empty dic
dic={}
print(dic)

#to pop
dic1.pop("hello")
print(dic1)

dic1.popitem()  # removes the last key value pair
print(dic1)

#del
del dic1['age']
print(dic1) #if something mentioned with dic-  it oly deletes the mentioned key value pair

del dic1
print(dic1)  #it deletes the entire dic