input_year=int(input("enter a year:-"))
if input_year%4==0:
    if input_year%100==0:
        if input_year%400==0:
            print("leap year hai")
        else:
            print("not leap year h")
    else:
        print("leap year h")
else:
    print("not leap year h")





    

        