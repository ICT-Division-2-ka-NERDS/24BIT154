#Swapping Two values

a=int(input('Enter the First Value :'))
b=int(input('Enter the Second Value :'))
print('First Value is :',a,'Second Value is :',b,sep=' ')

temp=a
a=b
b=temp
print('After Swapping :-')
print('First value is :',a,'Second Value is :',b)
