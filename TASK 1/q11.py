text = input("Enter text: ")

words = len(text.split())
letters = 0
sentences = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    if ch == "." or ch == "!" or ch == "?":
        sentences += 1

L = (letters / words) * 100
S = (sentences / words) * 100

grade = 0.0588 * L - 0.158 * S - 15.8
print("Grade level:", int(grade))