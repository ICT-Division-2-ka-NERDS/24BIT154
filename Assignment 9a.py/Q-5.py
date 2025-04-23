#filetering out names with more than 8 letters

l1=['siya','sumit Tandon','krishna','rohan mehta']

f=filter(lambda x:len(x)>8,l1)
print(tuple(f))
