#Ques 1.
N=2;
from itertools import islice
with open("1.txt") as f:
    h = list(islice(f, N))
print(h)

#Ques 2.
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("1.txt"))


#Ques 3.
with open("1.txt") as f:
    with open("new.txt", "w") as f1:
        for line in f:
            f1.write(line)

            
#Ques 4.
with open('1.txt') as f:
    with open('4.txt') as f1:
        for line1,line2 in zip(f,f1):
            print(line1+line2)

            
#Ques 5.
num = ['30', '10', '20', '15','18','12','29','26','25','3']

with open('new.txt', 'w') as filehandle:  
    for listitem in num:
        filehandle.write('%s\n' % listitem)

f=open("new.txt")
num=[]
for l in f:
    num.append(int(l))
num.sort()
f.close
with open('new.txt', 'w') as filehandle:  
    for listitem in num:
        filehandle.write('%s\n' % listitem)
