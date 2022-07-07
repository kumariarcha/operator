Expected_day=int(input("enter the Expected day:-"))
Expected_month=int(input("enter the Expected month:-"))
Expected_year=int(input("enter the Expected year:-"))
returened_day=int(input("enter the returened day:-"))
returened_month=int(input("enter the returened month:-"))
returened_year=int(input("enter the returened year:-"))
if returened_day==Expected_day:
    if returened_month==Expected_month:
        if returened_year==Expected_year:
            print("no fine")
        else:
            print("ur fine is",15*(returened_day-Expected_day))
    else:
        print("ur fine is ",500*(returened_month-Expected_month))
else:
    print("ur fine is",1000*(returened_year-Expected_year))

