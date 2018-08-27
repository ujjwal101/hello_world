#Ques 1.
#the code snippet shows ZeroDivisionError
a=3
if a<4:
    try:
        a=a/(a-3)
    except:
        print("denominator cannot be zero!")
print(a)


#Ques 2.
#the code snippet shows IndexError
l=[1,2,3]
try:
    print(l[3]) 
except:
    print("indexes above 2 aren't acceptable.")

#Ques 3.
#An exception
#error


#Ques 4.
#-5.0
#a/b result in 0


#Ques 5.
#1.IMPORT ERROR
try:
    import copyy
except ImportError as message:
    print('Exception:', message)
#2.VALUE ERROR
try:
    num=int(input("enter a number"))
except ValueError as message:
    print('Exception:', message)
#3.INDEX ERROR
l=[1,2,3]
try:
    print(l[3]) 
except:
    print("indexes above 2 aren't acceptable.")
