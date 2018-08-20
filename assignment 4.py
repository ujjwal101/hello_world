#Ques 1.
List=['10','15','20','25','30','35']
print(List[::-1])

#Ques 2.
a='I Love My Car'
count1=0
count2=0
for  i in a:
    if(i.isupper()):
        count1=count1+1
    else:
        count2=count2+1
print('The Uppercase in string are=')
print(count1)

#Ques 3.
a=input('Enter String:')
b=a.split()
print(','.join(b))

#Ques 4.
a='naman'
b=(a[::-1])
if a==b:
    print('string is Palindromic')
else:
    print('String is Not Palindromic')

#Ques 5.
import copy as cp
list1=[1,2,3,[4,5,6]]
list2=cp.deepcopy(list1)
list1[3][1]='Hello'
print(list1)
print(list2)
