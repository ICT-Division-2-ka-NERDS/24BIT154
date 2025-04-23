def convert():
    s=input('Enter a string with withespaces :')
    set1=set(s)
    l=list(set1)
    s1=sorted(l)
    j='-'.join(l)
    print(j)

convert()    
