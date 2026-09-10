def luhn():

     card = input("Enter card number: ")
     t = 0
     d = False
     for i in range(len(card) - 1, -1, -1):
        digit = int(card[i])
    
        if d:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
            
        t += d
        d = not d  

     if t % 10 == 0:
        print("Valid")
     else:
        print("Invalid")
print(luhn())



