
s=input("Enter a string")
def frequency(s):
    words=s.split()

    
    dict1={}
    for word in words:
        word=word.lower()
        dict1[word]=dict1.get(word,0)+1

    sort=dict(sorted(dict1.items))
    return sort
 

result=frequency(s)
print(result)
