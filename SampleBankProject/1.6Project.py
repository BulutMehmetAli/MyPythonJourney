customerInformations = {}
balanceInformations = {}

def createAccount():
    try:
        identityNumber = int(input("Please enter your identity number: "))
        length = len(str(identityNumber))
        
        if length != 11:
            print("Identity number must be exactly 11 digits long. Please enter again.")
            createAccount()
            return
        
        print("Your identity number is valid.")
    except ValueError:
        print("Invalid input! Please enter a numeric identity number.")
        createAccount()
        return  # Added to exit the loop

    name = input("Enter your name: ")
    lastName = input("Enter your last name: ")
    password = input("Enter your password: ")  # Password can be stored as a string

    try:
        investmentMoney = int(input("Please enter investment amount (Minimum $1000, multiples of 10): "))
        if (investmentMoney < 1000 or investmentMoney % 10 != 0):
            raise ValueError("You have to invest a minimum of $1000 and it must be a multiple of 10.")
    except ValueError as e:
        print(f"Error: {e}")
        createAccount()  # To allow re-entry
        return
    
    # Save data
    customerInformations[identityNumber] = {
        "Name": name,
        "LastName": lastName,
        "Password": password
    }
    balanceInformations[identityNumber] = investmentMoney

    choose = input("If you want to enter your account, please enter 'Y' or 'N' to exit: ")
    if choose.upper() == 'Y':
        menu(identityNumber)
    else:
        print("Thank you for choosing Mali Bank! Goodbye.")
        exit()

def menu(identityNumber):
    print("************* Account Menu *************")
    print("1- Balance Inquiry")
    print("2- Deposit Money")
    print("3- Withdraw Money")
    print("4- Exit")

    while True:
        try:
            chooseOption = int(input("Enter your choice: "))
            if chooseOption == 1:
                balanceInquiry(identityNumber)
            elif chooseOption == 2:
                depositMoney(identityNumber)
            elif chooseOption == 3:
                withdrawMoney(identityNumber)
            elif chooseOption == 4:
                print("Thank you for using Mali Bank! Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def balanceInquiry(identityNumber):  # Balance inquiry
    if identityNumber in balanceInformations:
        balance = balanceInformations[identityNumber]
        print(f"Your current balance is: ${balance}")
    else:
        print("Account not found.")


def depositMoney(identityNumber):  # Deposit money
    try:
        amountInvest = int(input("Enter your investment:"))
        if amountInvest % 10 != 0:
            raise ValueError("Amount must be a multiple of 10")
        elif amountInvest < 0:
            raise ValueError("Amount must be greater than 0")
        else:
            if identityNumber in balanceInformations:
                balanceInformations[identityNumber] += amountInvest
                print("Your new balance: ", balanceInformations[identityNumber])
            else:
                print("Account not found")
    except ValueError as e:
        print(f"Error: {e}")


def withdrawMoney(identityNumber):  # Withdraw money
    try:
        amountwithdraw = int(input("Enter your withdrawal amount:"))
        if amountwithdraw % 10 != 0:
            raise ValueError("Amount must be a multiple of 10")
        elif amountwithdraw <= 0:
            raise ValueError("Amount must be greater than 0")
        else:
            if identityNumber in balanceInformations:
                balanceInformations[identityNumber] -= amountwithdraw
                print("Your new balance: ", balanceInformations[identityNumber])
            else:
                print("Account not found")
    except ValueError as e:
        print(f"Error: {e}")


def checkAccount():
    try:
        verifyIdentityNumber = int(input("Enter your identity number: "))
        # Check if the identity number exists in the dictionary
        if verifyIdentityNumber in customerInformations:
            customer = customerInformations[verifyIdentityNumber]
            print("Account found!")
            print(f"Name: {customer['Name']}")
            print(f"Last Name: {customer['LastName']}")
        else:
            print("Account not found. Please check the identity number.")
    except ValueError:
        print("Invalid input! Please enter a numeric identity number.")



loginAttempts = 3
while loginAttempts > 0:
    choose = int(input("Welcome to our bank automation system. Please enter 1 to gain access or enter 2 to exit:"))
    if choose == 1:
        a = input("Do you have an account? (Y/N): ")
        if a == 'Y':
            checkAccount()
        elif a == 'N':
            createAccount()
        else:
            print("Invalid input.")
    elif choose == 2:
        print("Exiting the system. We wish you a good day...")
        break
    else:
        loginAttempts -= 1
        print(f"Incorrect value entered. You have {loginAttempts} attempts left.")
        if loginAttempts == 0:
            print("You have run out of login attempts. We wish you a good day...")
            break