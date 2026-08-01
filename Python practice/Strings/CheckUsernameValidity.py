username = input("Enter your username: ")
if username.isalnum() and len(username) >= 5:
 print("Valid username format.")
else:
 print("Invalid username format. Username must be alphanumeric and at least 5 characters long.")