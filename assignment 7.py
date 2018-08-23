#DICTIONARIES

#Ques 1.
dict1={}
for i in range(1,5):
    key=input("Enter the key:")
    value=input("Enter the value:")
    dict1[key]=value
print(dict1)

#Ques 2.
dict1={}
dict2={}
for i in range(1,3):
    dict2={}
    name=input("Enter name")
    for j in range(1,3):
        sub=input("Enter subject")
        marks=int(input("Enter marks"))
        dict2[sub]=marks
    dict1[name]=dict2
    print(dict1)
    student=input("Enter the student's name whose marks u want to see")
    print(dict1[student])
