stud1={'name':'A','rollno':4,'Emarks':45}
stud2={'name':'B','rollno':5,'Emarks':60}
stud3={'name':'C','rollno':6,'Emarks':70}
myschool={'stud1':stud1,'stud2':stud2,'stud3':stud3}
print(myschool)
stud1['hmarks']=75
stud1['mmark']=60
stud2['rollno']=15
stud2['Emarks']=80
stud3.pop("Emarks")
print(myschool)