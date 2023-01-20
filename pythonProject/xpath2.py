
print("welcome my bank")
restart=('Y')
chances=3
balance=900
while chances>=0:
    pin=int(input("please enter your 4 digit pin:"))
    if pin==(1234):
        print("you entered your pin correctly\n")
        while restart not in ('n','NO','no','N'):
            print("please press 1 for balance\n")
            print("please press 2 for withdrawal\n")
            print("please press 3 for pay\n")
            print("please press 4 for exit\n")
            option=int(input("what would you like to choose"))
            if option==1:
                print("your balanceis ",balance,'\n')
                restart=input("would you like  to go back")
                if restart in ('n','NO','no','N'):
                    print("thank you for banking with me")
                    break
            elif option==2:
                option2=('y')
                withdrawl=float(input("how much money you want"))
                if withdrawl in [10,20,40,60,80,100]:
                    balance=balance-withdrawl
                    print('\nyour balance is now',balance)
                    restart=input("what would you like to do")
                    if restart in ('n','NO','no','N'):
                        print("thank you for banking with me")
                        break
                elif withdrawl != [10,20,40,60,80,100]:
                    print('Invalid amount,please retry')
                    restart=('y')
                elif withdrawl==1:
                    withdrawl=float(input("please enter the desiired amount"))
            elif option==3:
                pay_in=float(input('how much you like to pay in\n'))
                balance=balance+pay_in
                print("your balance is now",balance)
                restart=input("what you like to go back")
                if restart in ('n','NO','no','N'):
                    print("thank you  for baking with me")
                    break
            elif option==4:
                print('please wait while your card is returned..\n')
                print("thank you for baking me")
                break
            else:
                print('please enter a correct number.\n')
                restart=('Y')
    elif pin !=('1234'):
        print('incorrect password')
        chances=chances-1
        if chances==0:
            print("\n No more tries contact support with shubham")
            break