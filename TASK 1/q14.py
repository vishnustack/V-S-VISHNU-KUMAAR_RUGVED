arr = [10, 5, 3, 4, 3, 5, 6]

r=1
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            r=arr[i]
            break
    if (r==0):
        break

if (r==1):
    print("First repeating element:", r)
else:
    print("No repeating element found.")