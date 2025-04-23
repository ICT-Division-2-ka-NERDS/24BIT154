import random

s1={random.randint(15,45) for i in range(12)}
print(s1)
count=0

for i in s1:
    if(i<30):
        count=count+1

    elif(i>35):
        s1.remove(i)

print(s1)
print('numbers less than 30 :',count)
