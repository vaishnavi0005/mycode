#membership operators
#write a program that checks if a letter entered by the user is a vowel(a,e,i,o,u) using the in operator. print "vowel" or "Not vowel" accordingly.
a=str(input("Enter string: "))
if a in('a','e','i','o','u'):
    print("vowel")
else:
    print("Not a vowel")