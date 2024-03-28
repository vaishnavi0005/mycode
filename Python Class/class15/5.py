a=[1,2,6,3,7,11,13]
b={}
for x in a:
    if x%2==1:
        b[x]=x**3
print(b)

#by using comprehensions
a=[1,2,6,3,7,11,13]
b={x:x**3 for x in a if x%2==1}
print(b)