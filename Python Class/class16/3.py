#even
a=[x for x in range(1,20) if x%2==0]
print(a)

#odd
b={x for x in range(1,20) if x%2==1}
print(b)

c={x:x**2 for x in range(1,20) if x%2==1}
print(c)