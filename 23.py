#verifying a phone number using regex
import re
phn="313-414-5656"
if re.search("\w{3}-\w{3}-\w{4}", phn):
    print("it is a phone number")
else:
    print("the number isn't a phone a number")
    
    
phn="313-4145-5656"
if re.search(r"\b\w{3}-\w{3}-\w{4}\b", phn): #using boundary functions
    print("it is a phone number")
else:
    print("the number isn't a phone number")
    
    
    
phn="3134-414-5656"
if re.search(r"\b\w{3}-\w{3}-\w{4}\b", phn):
    print("it is a phone number")
else:
    print("the number isn't a phone number")
    
    
