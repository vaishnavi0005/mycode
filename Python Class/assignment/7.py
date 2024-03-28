#stringt validation: create a program that a checks if a user-entered email address contains the "@"symbol. print"valid email" if it does, and "invalid email" if it doesn't
a=(input("enter email"))
if ("@"in a):
    print("valid email")
else:
    print("invalid email")
