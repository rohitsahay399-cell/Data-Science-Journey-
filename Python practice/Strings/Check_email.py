email = input("Enter your email: ")

if email.count("@") == 1 and email.endswith(".com"):
    print("Valid email format.")
else:
    print("Invalid email format.")