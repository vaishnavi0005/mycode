a=['jan','feb','mar','apr']
b=['red','blue','green','yellow']
#using nested loop
for x in a:
    if x=='mar':
        break
        print(x)
        for y in b:
            if y=='green':
                continue
                print(y)
