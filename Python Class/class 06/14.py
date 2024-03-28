a=int(input("enter your age: "))
if a>10:
    print("A")
elif a<10:
    print('B')
    if a>30:
        print("c")
    elif a>25:
        print('d')  
        if a>30:
            print('f')
        elif a>15:
    else:
        print("e")
else:
    print("f")