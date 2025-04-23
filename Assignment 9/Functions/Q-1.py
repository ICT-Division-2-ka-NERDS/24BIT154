#counting upper and lower case letters

def count_upper_lower():
    u=0
    l=0

    s=input('Enter a string :')
    for i in s:
        if(i.isupper()):
            u+=1
        else:
            l+=1

    return {'Lower':l,'Upper':u}

result=count_upper_lower()
print(result)
    
    
