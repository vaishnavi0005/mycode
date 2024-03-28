a=['arya','diksha','priya','mayuri']
b=['cake','apple','maggie','samosa']
c={}
for(x,y)in zip (a,b):
    c[x]=y
print(c)


a=['arya','diksha','priya','mayuri']
b=['cake','apple','maggie','samosa']
c={x:y for (x,y) in zip(a,b)}
print(c)