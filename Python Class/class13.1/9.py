b={'name':'harsh','marks':97}
a=b.copy()
print(a)
#dict method
c=dict(a)
print(c)
#insert a new item in c
c['area']="mumbai"
#updata marks
c["marks"]=100

#delet name
c.pop('name')
print(c)