a = input("Enter a number: ")
n = len(a)

if n < 3:
    print(a, "is not a Hill Number")
else:
    i = 0
    while i < n - 1 and a[i] < a[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        print(a, "is NOT a Hill Number")
    else:
        while i < n - 1 and a[i] > a[i + 1]:
            i += 1

        if i == n - 1:
            print(a, "is a Hill Number")
        else:
            print(a, "is not a Hill Number")