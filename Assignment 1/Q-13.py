# Bytes to KB, MB, GB

a=int(input('Enter Bytes : '))

b=a/10**3 #1 Kilobyte=10**3 Bytes
print('Kilobytes are :',b)

c=a/10**6 #1 Megabyte=10**6 Bytes
print('Megabytes are :',c)

d=a/10**9 #1 Gigabyte=10**9 Bytes
print('Gigabytes are :',d)
