alpha={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

def ispangram():
    s=input('Enter a string :')
    a=s.lower()
    b=set(a)

    if(alpha<=b):
        print('string is a pangram ')

    else:
         print('string is  not a pangram ')

ispangram()         
