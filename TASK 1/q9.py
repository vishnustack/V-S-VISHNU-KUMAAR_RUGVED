def encrypt():
    a= "abcdefghijklmnopqrstuvwxyz"
    text = input("Enter text: ").lower()
    shift = int(input("Enter shift: "))
    result = ""

    for ch in text:
        if ch in a:
            pos = a.find(ch)
            new_pos = (pos + shift) % 26
            result += a[new_pos]
        else:
            result += ch
    print("Encrypted:", result)
print(encrypt())



