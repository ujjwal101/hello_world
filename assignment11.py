#Ques 1.
import re
i=0
email=input("enter email")
a=re.finditer("^[a-zA-Z0-9][_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com|rediffmail.com)$",email)
for m in a:
    i=m.group()
if email==i:
    print("valid email")
else:
    print("invalid email")


    
#Ques 2.
import re
i=0
num=input("enter number")
a=re.finditer("^[6-9]{1}[0-9]{9}",num)
for m in a:
    i=m.group()
if num==i:
    print("indian number")
else:
    print("not an indian number")
