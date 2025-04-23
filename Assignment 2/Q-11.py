# To check if points are on the same line or not

x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))
x3=int(input("Enter x3:"))
y3=int(input("Enter y3:"))

s1=(y2-y1)/(x2-x1)   # slope of the line
s2=(y3-y2)/(x3-x2)   # slope of the line
s3=(y1-y3)/(x1-x3)   # slope of the line

if(s1==s2==s3):
    print('Points lie on the same line')
else:
    print('Points donot Lie on the same line')
