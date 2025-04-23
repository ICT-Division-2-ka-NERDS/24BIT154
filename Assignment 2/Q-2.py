#Largest and Smallest values of 3 Numbers

a=int(input('Enter the First No. :'))
b=int(input('Enter the value of Second No.'))
c=int(input('Enter the Third No. :' ))

if(a>b and a>c):
    print('a is the largest')
    if(b>c):
        print('c is smallest')

    else:
        print('b is smallest')
        
elif(b>a and b>c):
    print('b is the largest')
    if(a>c):
        print('c is smallest')
    
    else:
        print('a is smallest')
        
elif(c>b and c>a):
    print('c is the largest')
    if(b>a):
        print('a is smallest')
    
    else:
        print('b is smallest')        
        
