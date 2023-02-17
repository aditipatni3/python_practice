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