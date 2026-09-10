x=input("Enter the string: ")
a=sorted(x)
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
print(a)