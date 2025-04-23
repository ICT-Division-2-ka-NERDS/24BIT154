# generating pythagoreous triplets with side length <=30
a=1
b=1
c=1
for a in range(1,31):              # a ranges from 1 to 31
    for b in range(a,31):          # b ranges from a to 31    
        for c in range(b,31):      # c ranges from b to 31
            if(a**2+b**2==c**2):
                print('pythagorous triplets ',a,b,c)
    
