s=input("Enter string: ")
n=int(input("Enter n: "))

if len(s)%n!=0:
    print("cannot divide to equal parts")
else:
    a=[]
    for i in range(0,len(s),n):
        a.append(s[i:i+n])

    c=1
    for b in a:
        if b!=a[0]:
            c=0
            break

    if (c==1):
        print("Output:", a)
    else:
        print("Sequences are not the same")