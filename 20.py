#RegEx- Regular Expression
import re
NameAge='''
Janice is 22 and Theon is 23 
Gabriel is 33 and Joey is 21
'''
ages=re.findall(r'\d{1,3}', NameAge)
names=re.findall(r'[A-Z][a-z]*', NameAge)

ageDict={}
x=0
for eachname in names:
    ageDict[eachname]= ages[x]
    x+=1
print(ageDict)