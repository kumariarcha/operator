num1=int(input("enter the first num:-"))
num2=int(input("enter the second num:-"))
num3=int(input("enter the third num:-"))
if num1>num2 and num2<num1:
    print("greastest num",num1)
elif num2>num3 and num1<num2:
    print("greastest num",num2)
elif num3>num1 and num2<num3:
    print("greastest num",num3)
else:
    print("nothing")