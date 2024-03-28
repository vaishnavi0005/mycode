mylist=[1,3,7,2,4,16,21,27]
a=set()
for b in mylist:
    if b%2==1:
        a.add(b)
print(a)


mylist=[1,3,7,2,4,16,21,27]
b={x for x in mylist if x%2==1}
print(b)
        

