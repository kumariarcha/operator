# sub1=input("enter the marks of physics")
# sub2=input("enter the marks of chemistry")
# sub3=input("enter the marks of biology")
# sub4=input("enter the marks of mathematics")
# sub5=input("enter the marks of computer")
# percentage=(sub1+sub2+sub3+sub4+sub5)/5
# print(percentage)
# if percentage>=90:
#     print("Grade A")
# elif percentage>=80:
#     print("grade B")
# elif percentage>=70:
#     print("grade C")
# elif percentage>=60:
#     print("grade D")
# elif percentage>=40:
#     print("grade E")
# else:
#     print("grade F")



sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")