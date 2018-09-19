word = input("Give me a word: ")
long = int(word.__len__())
letters = []
pal = False

for c in word:
    if c != ' ':
        letters.append(c)

rev = (letters[::-1])

if letters == rev:
    print("Palindrome")
else:
    print("No Palindrome")