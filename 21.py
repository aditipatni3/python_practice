#finding a word in string using RegEx
import re
if re.search("inform", "we need to inform you about the latest information"):
    print("we have inform")
    
    
    
#this has infrom in information
# if re.search("inform", "we need to you about the latest information"):
#     print("we have inform")
    
    
#to find the list of all matches
allinform=re.findall("inform", "we need to inform his with the latest information")
for i in allinform:
    print(i)
    

#GETTING THE STARTING AND ENDING INDEX OF A PARTICULAR STRING:
str="we need to inform him with the latest information"
for i in re.finditer("inform", str):
    loctup=i.span()
    print(loctup)
    
#MATCH WORDS WITH A PARTICULAR PATTERN
strr="sat, hat, mat, pat"
allstrr=re.findall("[mshp]at", strr)
for i in allstrr:
    print(i)
    
#MATCH SERIES OF RANGE OF CHARACTER
strs="sat, hat, mat, pat, cat"
allstrr=re.findall("[c-m]at", strs)
for i in allstrr:
    print(i)
    
#using carat^ symbol
strs="sat, hat, mat, pat, cat"
allstrr=re.findall("[^c-m]at", strs)
for i in allstrr:
    print(i)
    
#REPLACE A STRING
food="hat, rat, mat, fat"
regex= re.compile("[r]at")
food=regex.sub("food", food)
print(food)