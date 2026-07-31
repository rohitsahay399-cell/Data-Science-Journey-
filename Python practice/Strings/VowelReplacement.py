text = input("enter the word: ")

for vowel in "aeiouAEIOU":
    text = text.replace(vowel,"*")
print("updated word:" , text)