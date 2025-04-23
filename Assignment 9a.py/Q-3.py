import random

l1=[random.randint(-15,15)for i in range(10)]

m=list(map(lambda x:x**2,l1))
l2=m
print(l1,l2,sep='\n')
