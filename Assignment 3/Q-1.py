#Counting No. of Vowels
a=input('Enter a string :')
count=0                     #initializing count variable
for ele in a:
    if(ele in'AaEeIiOoUu'):
        count=count+1            #checking if the vowel is present
print('No. of Vowels are :',count)    



