#create a program that asks the user for the username and password. Check if both the username and password match predfined values. print "Login succesful" or "Login failed" accordingly
x=str(input("Enter your username: "))
y=str(input("Enter your password: "))
if x==y:
    print("Login successful")
if x!=y:
    print("Login faild")
