name = "mam"
reversed = ""

for ch in name:
    reversed = ch  + reversed 
print(reversed)

if name == reversed:
    print("The string is palindrome")
else:
    print("The string is not palindrome")