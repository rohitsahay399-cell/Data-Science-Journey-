Password = input("Enter your password: ")

has_digit = False

for ch in Password:
    if ch.isdigit():
        has_digit = True
        break


if has_digit:
     print("valid password format.")
else:
 print("Invalid password format. Password must contain at least one digit.")