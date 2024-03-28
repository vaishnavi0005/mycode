a=['red','blue','green','grey','white']
#for with break
for x in a:
    if x=='green':
        break
    print(x)
    for y in a:
        if y=='blue':
            continue
        print(y)