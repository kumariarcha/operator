year=int(input("enter the year:-"))
month=int(input("enter the month:-"))
day=int(input("enter the day:-"))
if year%4==0:
    print(year)
elif month==3:
    print(month)
elif day==7:
    print(day)
else:
    print("enter the yy$ mm $dd")
