print("wel come to state bank of india")
language=(input("\n1 english \n2 hindi\nenter the your language number :="))
if language=="1":
    transaction=["n1.balance enqary/ n2.withdarw money/ n3.deposit/ n4transfer money/ n5.quit"]
    atm_pin=1234
    pin=input("enter your 4 digit pin to number")
    pin==atm_pin
    amount=20000
    if atm_pin==1234:
            print("n1. choose your transcation :-")
            print("n2 for balance enquiry enter 1:-")
            print("n3. for withdraw money enter 2:-")
            print("n4.for deposit money enter 3:-")
            print("n5.for transfer money enter 4:-")
            print("n6. for quit enter 5 ")
            trans=input("transaction:-")
            if trans=="1":
                swipe=input("do you want enquiry your money?:-")
                if swipe=="yes":
                    print(amount," is your money ,thanks for using state bank of india")
                else:
                    print("nothing")
            elif trans=="2":
                amount1=int(input("enter yoour amount to proceed   "))
                if amount1>=0 and amount1<=20000:
                    print("collect your cash", amount-amount1,"is left in your account. Thanks for using SBI")
                else:
                    print("enter valid amount to proceed")
            elif trans=="3":
                amount2=int(input("enter the amount to deposit=    "))
                if amount2>=1:
                    print("your diposit is done sucsessfully! Now you have", amount+amount2, "Thanks for using SBI Bank")
                else:
                    print("enter valid amount to deposit")
            elif trans=="4":
                transfer_money=int(input("enter your amount to transfer      "))
                if transfer_money>=0:
                    print("your money has been tranfered!", amount-transfer_money,"is left in your account. thanks for using SBI Bank")
                else:
                    print("enter valid amount")
            elif trans=="5":
                quit=input("press to quit")
                if quit=="yes":
                    print("quit")
                else:
                    print("choose any transaction please")
            else:
                print("your password is not valid,try again")
    else:
        print("your pass word is wrong")
else:
    print("sorry we dont have that language")
    print("thinks for using sbi bank")
        
