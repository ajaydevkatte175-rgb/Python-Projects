import re

email_condition = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

email = input('enter your email address: ')

if re.search(email_condition ,email):
    print("Valid email address.email validated successfully.")
else:
    print("Invalid email: Email should be at least 6 characters long, start with an alphabet, contain exactly one '@' symbol, have a . in the correct position, and should not contain spaces, uppercase letters, or special characters other than '_', '.', and '@'.'")


