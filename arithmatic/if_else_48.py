            
################48#################
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a>b and a<c:
    print(a,"is the median.")
elif b<c and b>a:
    print(b," is the median.")
elif c<b and c>a:
    print(c," is the median")
else:
    print("Invalid")





