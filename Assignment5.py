#Ques 1.Year=int(input("Enter a year to check if its leap year"))if(Year%4==0):    if(Year%100==0):        if(Year%400==0):            print("LEAP YEAR")        else:            print("NOT LEAP YEAR")    else:        print("LEAP YEAR")else:    print("NOT LEAP YEAR")#Ques 2.Length=int(input("Enter Length"))Breadth=int(input("Enter Breadth"))if(Length==Breadth):    print("IT'S A SQUARE")else:    print("IT'S A RECTANGLE")    #Ques 3.x=int(input("Enter age of first person"))y=int(input("Enter age of second person"))z=int(input("Enter age of third person"))if(x>=y and x>=z):    print("First person is the oldest")elif(y>=x and y>=z):    print("Second person is the oldest")else:    print("Third person is the oldest")if(x<=y and x<=z):    print("First person is the youngest")elif(y<=x and y<=z):    print("Second person is the youngest")else:    print("Third person is the youngest")#Ques 4.Age=int(input("Enter Age"))Sex=input("Enter Sex")m=input("Enter Marital Status")if(Sex=='F'):    print("Work in Urban Areas")else:    if(Age>=20 and Age<=40):        print("Can work ANYWHERE")    elif(Age>=40 and Age<=60):        print("Work in URBAN AREAS")    else:        print("Error")#Ques 5.q=int(input("Enter Quantity"))c=100*qif(c>1000):    c=c-(c*0.1)    print("Total cost is =",c)else:    print("Total cost is =",c)#LOOPS#Ques 1.li=[]for i in range(10):    a=int(input("Enter a number"))    li.append(a)print(li)#Ques 2.#while True: #   print("*")#Ques 3.a=[]b=[]num=int(input("enter number of elements"))for i in range(num):    c=int(input("enter number"))    a.append(c)for j in a:    v=j*j    b.append(v)print(b)#Ques 4.li1=[]li2=[]li3=[]li4=[]a=int(input("Enter total number of inputs"))for i in range(a):    b=input("Enter elements of list")    li1.append(b)for i in li1:    if(i.isdigit()):        li2.append(i)    elif(i.isalpha()):        li3.append(i)    else:        li4.append(i)print(li2)print(li3)print(li4)#Ques 5p=[]for i in range(1,101):    if(i>1):        flag=False        for j in range(2,i):            if(i%j==0):                flag=True        if not flag:            p.append(i)print(p)#Ques 6.for i in range(5):    for j in range(i):        print("*",end='')    print()#Ques 7.li8=[]n=int(input("Enter number of elements of list"))for i in range(n):    a=int(input("Enter element"))    li8.append(a)num=int(input("Enter the number you want to delete from list"))x=li8.count(num)for i in range(x):    y=li8.index(num)    del(li8[y])print(li8)