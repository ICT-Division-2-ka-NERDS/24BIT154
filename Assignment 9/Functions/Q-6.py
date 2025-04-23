lst=[]
def fun():
    x=int(input('Enter the  integer value of x :'))
    for t in range(1,x+1):
        s=(t,t**2,t**3)
        lst.append(s)

    print(lst)

fun()    
