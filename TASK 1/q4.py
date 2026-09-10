s=input("Enter string: ")
a = list(s)
n = len(a)
for i in range(n):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
        x=''.join(a)
print("The sorted string is :",x)

