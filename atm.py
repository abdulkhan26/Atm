import getpass
users={
    "abdul":1111,
    "mannan":2222,
    "khan":3333}

balances = {name: [0] for name in users}
def credit(balance,amount):
    #cred_amount=int(input("enter the amount to be credited\n"))
    if amount>0 :
        new_bal=balance[-1]
        new_bal+=amount
        balance.append(new_bal)
    return print(f" Balance is {balance[-1]}")

def debit(balance,amount):
    #deb_amount=int(input("enter the amount to be debited\n"))
    if amount>balance[-1] and amount>0:
        print("Insufficient balance")
    elif amount>0:
        new_bal=balance[-1]-amount
        balance.append(new_bal)
        print(f"Balance is: {balance[-1]}")
     

def authorization(users):
    while True:
        name=input("Please enter the name or press 9 to Exit\n\n")
        if name=="9":
            print("Thank you")
            exit()
        if name in users:
            pin=int(getpass.getpass("enter the 4 digit pin\n\n"))
            if users[name]==pin:
                print("verified\n\n")
                balance=balances[name]
                while True:
                    value=int(input("please enter your choice \n 1.Check balance \n 2.Debit\n 3.Credit \n 4.Switch User\n 5.Exit \n\n"))
                    if not options(value,balance):
                        break
            else:
                print("invalid pin\n\n")

        else:
            print("invalid user name\n\n")


def options(value,balance):
        match value:
            case 1:
                print(f"Your balance is: {balance[-1]}")
            case 2:
                amount=int(input("enter the amount to be debited\n\n"))
                debit(balance,amount)
            case 3:
                amount=int(input("enter the amount to be credited\n\n"))
                credit(balance,amount)
            case 4:
                print("logging out\n\n")
                return False
                
            case 5:
                print("thank you\n")
                return False
            case _:
                print("Invalid choice.Enter again.\n")
        return True

        
print("welcome to AMK bank\n\n")
authorization(users)

