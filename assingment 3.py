#Ques 1.
NexaCars=['Ignis','Baleno','Ciaz','S-cross']
print(NexaCars)

#Ques 2.
NewEntry=['google','apple','facebook','microsoft','tesla']
Add=NewEntry + NexaCars
print(Add)

#Ques 3.
Num=[1,0,1,5,2,6,2,5,3,0,3]
print(Num.count(0))

#Ques 4.
Numbers=[30,26,25,20,15,10,3]
Numbers.sort()
print(Numbers)

#Ques 5.
A=[3,10,15,20]
B=[25,26,30]
C=A+B
C.sort()
print(C)

#Ques 6.
Numbers=[3,10,15,20,25,26,30]
count1=0
count2=0
for i in Numbers:
    if not i % 2:
        count1=count1+1
    else:
        count2=count2+1
print("Even Numbers=",count1)
print("Odd Numbers=",count2)


#TUPLE QUES

#Ques 1.
A=("10,15,20")
B=reversed(A)
print(tuple(B))

#Ques 2.
A=[3,10,15,20,25,26,30]
print('Maximum is=',max(A))
print('Minimum is=',min(A))


#STRING QUES

#Ques 1.
string="ujjwal agnihotri"
print(string.upper())

#Ques 2.
str="ujjwal9292"
print(str.isnumeric())

#Ques 3.
string='Hello World'
print(string.replace('World','Ujjwal Agnihotri'))
