a=int(input("enter your age: "))
if a<18:
    print("you are not eligible")
    print("you cannot vote")
elif a>18 and a<60:
    print("you are eligible")
    print("please come for interview")
else: 
    print("you can retire")
    print("Not eligible")