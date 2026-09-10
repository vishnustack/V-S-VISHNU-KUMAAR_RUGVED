n=int(input("No of terms: "))
n1,n2=0,1
c=0
if n==1:
   print("Fibonacci sequence: ")
   print(n1)
else:
   print("Fibonacci sequence:")
   while c<n:
       print(n1)
       s=n1+n2
       n1=n2
       n2=s
       c+=1