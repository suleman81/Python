print("Welcome To My ATM")
chance = 3
balance = 100
restart = ('Y')

while chance >= 0:
    pin = int(input("Please Enter your 4-digit Password: "))
    if pin == 1234:
        while restart not in ('N','n'):
            print("Please choose 1 to check your Balance:")
            print("Please choose 2 to make withdraw:")
            print("Please choose 3 to Pay in:")
            print("Please choose 4 to get your card back:")
            option = int(input("Enter your choice: "))
            if option == 1:
                print(f"Your current balance is {balance}$.\n")
                restart = input("Would you like to choose another option: ")
                if restart in ('N','n'):
                    print("Thank you..")
                    break
            elif option == 2:
                option2 = ('Y')
                withdraw = float(input("How much would you like to withdraw? \n - 10$/- 30$/- 50$/- 80$/- 100$"))
                if withdraw in [10,30,50,80,100]:
                    balance = balance - withdraw
                    print(f"Your current balance is {balance}$.")
                    restart = input("Would you like to choose another option: ")
                    if restart in ('N','n'):
                        print("Thank you..")
                        break
                elif withdraw != [10,30,50,80,100]:
                    print("Invalid input Please Re-try\n")
                    restart = ('Y')
                elif withdraw == 1:
                    withdraw = float(input("Please enter desired amount:"))

            elif option == 3:
                pay_in = float(input("How would you like to Pay In: "))
                balance = balance + pay_in
                print(f"Your current balance is {balance}$.")
                restart = input("Would you like to choose another option: ")
                if restart in ('N','n'):
                    print("Thank you..")
                    break
            elif option == 4:
                print("Here is your card\n Thanks for choosing us")
                break
            else:
                print("Pleaseenter correct number")
                restart = ('Y')
    elif pin != 1234:
        print('Incorrect Password')
        chance = chance - 1
        if chance == 0:
            print('\nNo more tries')
            break