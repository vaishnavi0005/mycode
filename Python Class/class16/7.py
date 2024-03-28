a={1,2,6,6,2,1,4,9,7,7,6,5}
b={x for x in a if x%2==0}
print(b)

c={x:x**3 for x in a if x%2==0}
print(c)