a=['red','blue','green','grey','white']
#for with break
for x in a:
    if x=='green':
        break
    print(x)
i=0
while i<len(a):
    i+=1
    if a[i]=='green':
        continue
    print(a[i])
