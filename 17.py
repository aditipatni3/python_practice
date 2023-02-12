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


