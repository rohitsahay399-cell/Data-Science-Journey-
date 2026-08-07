password = input("Enter password: ")

if len(password) >= 8:
    print("Valid password.")
else:
    print("Password must be at least 8 characters long.")