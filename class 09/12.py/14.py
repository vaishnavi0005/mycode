import datetime
#user input
day=int(input("Enter day(1-31): "))
month=int(input("Enter month(1-12): "))
year=int(input("Enter year: "))
#convert user input to a date
date=datetime.datetime(year,month,day)
#use weekday function to get week count
week=date.weekday()
#weekday
weekdays=["mon","tue","wed","thu","fri","sat","sun"]
print(weekdays[week])
print(week)
