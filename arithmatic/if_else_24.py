a=int(input("enter the first age:-"))
b=int(input("enter the second age:-"))
c=int(input("enter the third age:-"))
if a>b and a>c :
    print(a, "oldest")
elif b>a and b>c:
    print(b,"among")
elif c>a and c>a:
    print(c,"yengest")
else:
    print("nothing")