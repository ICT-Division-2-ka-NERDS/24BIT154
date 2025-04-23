#removing empty tuple from existing tuple

t1=()
t2=(1,22,31,'hiii',41,67)
t3=()
t4=(9,0,5,55,'hello','broo',34)

l1=[t1,t2,t3,t4]

for i in l1:
    if(len(i)==0):
        l1.remove(i)


print('list with no empty tuples :',l1)        
