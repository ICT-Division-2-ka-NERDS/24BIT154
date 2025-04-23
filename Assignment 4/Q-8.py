#Finding the factorial

No=int(input('Enter a number to find it\'s factorial: '))
fact=1
for i in range(1,No+1):
    fact=fact*i
print('Factorial of the No. Given is :',fact)    
