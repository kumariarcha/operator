r=int(input("enter the number of room..."))
g=int(input("enter the number of girls"))
bed=int(input("enter the number of bed"))
if g>bed :
    if g-bed:
        a=g-bed
        print("we want more",a,"bed")
elif g<bed:
    if bed-g:
        b=bed-g
        print("we are want more",b,"girls")
else:
    print("All is well")