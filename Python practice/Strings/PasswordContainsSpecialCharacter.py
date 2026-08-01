password = input("Enter your password: ")
has_special = False

for ch in password:
    if not ch.isalnum():
        has_special = True
        break

if has_special:
    print("Password contains a special character. ")
else:
    print("Password does not contain a special character.")