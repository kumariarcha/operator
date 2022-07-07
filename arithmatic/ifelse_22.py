service_year=int(input("enter the empoly year:-"))
salary=int(input("enter the empoly service salary:-"))
if service_year>5:
    bonus=salary/5
    print(bonus,"u got bonus")
else:
    print("u will not get bonus because u did not did more then 5 year")