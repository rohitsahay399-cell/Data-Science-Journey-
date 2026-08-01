password = input("Enter password: ")

has_lower = False

for ch in password:
    if ch.islower():
        has_lower = True
        break

if has_lower:
    print("Password contains a lowercase letter.")
else:
    print("Password does not contain a lowercase letter.")