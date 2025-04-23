#string in the list is palindrome or not

l1 = ['madam','Python',"malayalam",12321]

f=filter(lambda x:str(x)==str(x)[::-1],l1)
print(list(f))



