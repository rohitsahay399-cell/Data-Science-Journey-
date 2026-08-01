Phone =input("Enter your phone number: ")
if Phone.isdigit() and len(Phone) == 10:
    print("Valid phone number format.")
else:
    print("Invalid phone number format. ")