# seperating the elements of tuple

l1=[(1,'s1',14),(2,'s2',16),(3,'s3',15),(4,'s4',18)]

lname=[]
lroll=[]
lage=[]

for ele in l1:
    lname.append(ele[1])
    lroll.append(ele[0])
    lage.append(ele[2])

print(lname, lroll,lage)    
