# Write a python program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added toif the bill 
# unit=int(input("enter the units:-"))              
# if unit>=50:
#     bill=unit*0.50
#     print(bill, "bill")
# elif unit>=100:
#     bill=unit*0.75
#     print(bill,"bill")
# elif unit> 100 and unit<250:
#     bill=unit*1.20
#     print(bill)
# elif unit>250:
#     bill=unit*1.50
#     print(bill)
# else:
#     print("nothing")

# carecter=input("enter the alphabet:=")
# if carecter in ("aeiou"):
#     print("vowel")
# elif carecter in ("AEIOU"):
#     print("vowel")
# else:
#     print("consonant")

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# if a>b and a>c:
#     print(a,"maximum")
# elif b>c and b>a:
#     print(b,"maximum")
# elif c>a and c>b:
#     print(c,"maximum")
# else:
#     print("not maximum")

user=int(input("enter the number"))
if user>0:
    print("positive")
elif user<0:
    print("negative")
elif user>=0:
    print("zero")
else:
    print("error")







    