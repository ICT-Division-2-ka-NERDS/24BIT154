# counting number of boys and girls

t1=('ravi','raju','rishi')
t2=('b1','b2','b3','b4')
l1=['hiya','siya',t1,'riya','diya',t2]

g=0
b=0

for ele in l1:
    if(isinstance(ele,tuple)):
        b=len(t1)+len(t2)

    else:
        g=g+1

print('Number of girls :',g)
print('Number of boys :',b)
