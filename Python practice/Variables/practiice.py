name = input("Enter your name:")
reverse= ""

for char in name:
   reverse = (char + reverse) 


print(reverse)

if reverse == name:
    print("Palindrome")
else:
    print("Not palindrome")