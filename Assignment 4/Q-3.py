# counting no of Digits and alphabets in a string

a=0
d=0
str1=input('enter a string to count alphabets and digits in it :')

for ele in str1:
    
        if(ele.isalpha()):
            a=a+1

        elif(ele.isdigit()):
            d=d+1


print('No. of Alphabets :',a)
print('No. of Digits :',d)

            
