
def ispalindrome():
    x=input('Enter a String:')
    y=tuple(x)
    r=reversed(x)
    s=tuple(r)

    if(y==s):
        print('String is a palindrome')

    else:
        print('String is  not a palindrome')


ispalindrome()    
    
