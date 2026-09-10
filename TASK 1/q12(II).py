n = int(input("Input N: "))

for i in range(1,n+1):
    if i==n:
        print("* " * (2*n-1))
    else:
        left = "* " * (i-1) + "*"
        spaces = " " * (2*(n-i)-1)
        right = "*" + " *" * (i-1)
        print(left + spaces + right)

for i in range(n-1,0,-1):
    left = "* " * (i-1) + "*"
    spaces = " " * (2*(n-i)-1)
    right = "*" + " *" * (i-1)
    print(left + spaces + right)