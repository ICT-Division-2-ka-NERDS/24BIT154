#Initializing and using sort method   

lst1=[5,7,13,11,21]
lst2=[2,4,22,82]
lst1[2]=lst2
print('Nested list :',lst1)
l=[]
for i in lst1:
    if(type(i)==list):
        l.extend(i)
    else:
        l.append(i)
print('Flatterned list :',l)
l.sort()
print('List Sorted in Ascending Order :',l)
