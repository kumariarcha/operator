num1=int(input("enter the first num:="))
num2=int(input("enter the second num:="))
num3=int(input("enter the third num:="))
if num1>num2 and num1>num3:
    print("num1 is maximum")
elif num2>num3 and num3<num2:
    print("num2 is maximum")
elif num3>num1 and num3>num2:
    print("num3 is maximum")
else:
    print("nothing")


