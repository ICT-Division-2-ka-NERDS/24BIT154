# point is inside , on or Outside the circle

from math import sqrt

x=int(input('Enter x coordinate :'))
y=int(input('Enter y coordinate :'))

x1=int(input('Enter x coordinate of center:'))
y1=int(input('Enter y coordinate of center:'))

r=int(input('Enter Radius of the Circle :'))

l=sqrt(pow((x-x1),2)-pow((y-y1),2))

if(l==r):
    print('Point is on the Circle')
elif(l>r):
    print('Point is Outside the Circle')
else:
    print('Point is Inside the Circle ')
