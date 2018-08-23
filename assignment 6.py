#Ques 1.
import math
def area(r):
    sa=4 * math.pi * r * r
    print("The surface area of sphere is=%.2f" %sa)
r=float(input("Enter radius"))
area(r)

#Ques 2.
def perfect(n):
    sum=0
    for j in range(1,n):
        if n%j==0:
            sum=sum+j
    if sum==n:
            print(n)
for i in range (1,1000):
    perfect(i)
  
#Ques 3.
def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
n=int(input("Enter a number"))
table(n)

#Ques 4.
def cal(n,p):
    if p!=0:
        return (n*cal(n,p-1))
    else:
        return 1
n=int(input("Enter a number"))
p=int(input("Enter the power"))
print(cal(n,p))

