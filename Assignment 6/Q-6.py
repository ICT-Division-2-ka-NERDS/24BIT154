# modifying an element in tuple

t1=(1,22,2,3,4,5,'asus')
print(t1)

a=list(t1)
print(type(a))

a[3]=99
b=tuple(a)

print(b)
