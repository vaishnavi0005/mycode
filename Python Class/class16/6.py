a=[1,2,3]
b=[1,4,6]
c=[]
for x in a:
    for y in b:
        if (x+y)%2==0:
            c.append((x,y))
print(c)

c={(x,y) for x in a for y in b if(x+y)%2==0}
print(c)


