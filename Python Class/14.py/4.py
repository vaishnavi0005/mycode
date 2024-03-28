myschool={
"stud1":{'name':'A','rollno':4,'Emarks':45},
"stud2":{'name':'B','rollno':5,'Emarks':60},
"stud3":{'name':'C','rollno':6,'Emarks':70}}
print(myschool)
#to add new items
myschool['stud1']['hmarks']=70
myschool['stud2']['Emarks']=80
myschool['stud3'].pop('Emarks')
print(myschool)