choice = True
while (choice):
    userChoice = int(
        input("Enter your choice..\n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division \n 0. Exit \n"))

    if (userChoice == 0):
        break  ## Immidiate terminate. program will not execute further
        ###choice = False    ## this condtion will be checked only after completing this iteration

    firstNum = int(input("Please enter first number : "))
    secondNum = int(input("Please enter second number : "))

    if userChoice == 1:
        result = firstNum + secondNum
        print(f"{firstNum} + {secondNum} = {result}")

    elif userChoice == 2:
        result = firstNum - secondNum
        print(f"{firstNum} - {secondNum} = {result}")

    elif userChoice == 3:
        result = firstNum * secondNum
        print(f"{firstNum} * {secondNum} = {result}")

    elif userChoice == 4:
        result = firstNum / secondNum
        print(f"{firstNum} / {secondNum} = {result}")

    else:
        print("Thank you.. Exiting program")
        choice = False
        ####break


## it should return result.. or print result
def calculator(first, second, operation):
    pass





