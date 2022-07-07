a=int(input("enter first number:-"))
b=int(input("enter the second number:-"))
c=int(input("enter the third number:- "))
if a<b:
     if b<c:
        print(b,"is middile")
if b<a:
    if a<c:
        print(a,"is in middle") 
if c<b:
    if b<a:
        print(b,"is in middle")               
if b<c:
    if c<a:
        print(c,"is in middle")
if c<a:
    if a<b:
        print(a,"is in middle")
if b<c:
    if c<a:
        print(c,"is in middle")    
if a<c:
    if c<b:
        print(c,"is in middle")  
else:
    # print("nothing")   
    pass         

