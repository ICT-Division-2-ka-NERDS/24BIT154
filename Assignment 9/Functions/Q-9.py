def count_alpha_digit():
    a=0
    d=0
    s=input('Enter alphanumeric string : ')
    for ele in s:
        
        if(s.isalpha()):
            a+=1

        else:
            d+=1

    return{'alphabets':a,'Digits':d}

b=count_alpha_digit()
print(b)

        
