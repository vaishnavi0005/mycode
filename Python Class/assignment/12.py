#calculate factorial: write a program that calcutates the factorial of a user input positive integer.
n=int(input("enter number: "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)

