import random
l=[]
for n in range(20):
    l.append(random.randint(1,100))
print(l)
no=int(input('Enter a number present in the list :'))
if(no==n):
    i=l.index(no)
    print(i)



    
