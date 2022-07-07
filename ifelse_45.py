day=int(input("enter the day:="))
month=int(input("enter the month:="))
year=int(input("enter the year:="))
if (year%4==0 or year%100==0 or year%400):
        next_day=day+1
        next_month=month
        next_year=year
        print(next_day)
elif(month==2 and day==28):
        next_day=1
        next_month=month+1
        next_year=year
        print(next_month)
elif((day==30) and (month==4 or month==6 or month==9 or month==11)):
        next_day=1
        next_month=month
        next_year=year+1
        print(next_year)
else:
        next_day=day+1
        next_month=month
        next_year=year
print(next_day,"-",next_month,"-",next_year)
