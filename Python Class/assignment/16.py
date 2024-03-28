#Simple Interest Calculator:Develop a program that calculates simple interest based on the principal amount,interest rate, and time period entered by the user.
p=int(input("Enter Principal: "))
r=int(input("Enter rate of interest: "))
t=int(input("Enter time period: "))
simple_interest=(p*r*t)/100
print("your simple_interest is: ",simple_interest)
a=p+simple_interest
print("your Amount is: ",a)
