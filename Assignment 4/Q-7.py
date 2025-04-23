n=int(input('Enter the value of n:'))
r=int(input('Enter the value of r:'))

nfact=1
rfact=1
fact=1

for i in range(1,n+1):
    nfact=nfact*i

for i in range(1,r+1):
    rfact=rfact*i
    
for i in range(1,n-r+1):
    fact=fact*i

nCr=nfact/(rfact*fact)
print('Value of nCr is :',nCr)

nPr=nfact/fact
print('Value of nPr is :',nPr)
    
