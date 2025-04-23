#To Check wether area of Rectangle is greater then the perimeter
l=int(input('Enter Length :'))
b=int(input('Enter Breadth :'))
print('Length is :',l,'Breadth is :',b)

a=l*b
p=2*(l+b)

if(a>p):
      print('Area is Greater then Perimeter')
else:
    print('Area is not Greater then Perimeter')
