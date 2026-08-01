Password = input("Enter your password: ")

has_uppercase = False

for ch in Password:
    if ch.isupper():
        has_uppercase = True
        break

if has_uppercase:
    print("Password contains at least one uppercase letter.")
else:
    print("Invalid password format. Password must contain at least one uppercase letter.")


