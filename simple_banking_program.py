# Python Banking Programm
def show_balance(balance):
    print("********************")
    print(f"Your balance is ${balance:.3f}")
    print("********************")


def deposit():
    amount = float(input("Enter an amount to deposit : "))

    if amount < 0:
        print("********************")
        print("That's not a valid amount")
        print("********************")
        return 0
    else :
        return amount

def withdraw(balance):
    amount = float(input("Enter a  amount to withdraw : "))

    if amount > balance:
        print("********************")
        print("Insuuficient Balance")
        print("********************")
        return 0
    elif amount < 0:
        print("********************")
        print("Amount must be greater than 0")    
        print("********************")
        return 0
    else : 
        return amount    


def main():
     balance = 0
     is_running = True
     
     while is_running:
        print("********************")
        print("   Banking Program   ")
        print("********************")
        print("1. Show Balance ")

        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Exit ")
        print("********************")    
        choice = input("Enter a your choice(1-4): ")
    
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance =+ deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("********************")
            print("That is not a valid choice")  
            print("********************")
     
     print("********************")
     print("Thank you!!  Have a nice day!")          
     print("********************")         
     


if __name__ == '__main__':
    main()

