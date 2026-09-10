def anagram(s1,s2):
    a=s1.lower().replace(" ", "")
    b=s2.lower().replace(" ", "")
    print(a,b)
    return sorted(a)==sorted(b)
s1=input("Enter first string: ")
s2=input("Enter second string: ")
if anagram(s1,s2):
    print("Strings are Anagrams")
else:
    print("Strings are NOT Anagrams")