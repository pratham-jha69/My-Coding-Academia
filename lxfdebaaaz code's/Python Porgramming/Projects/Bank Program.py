import time
def show_balance(balance):
    print("-----------------------------------")
    print("Showing Balance")

    time.sleep(2)
    print(f"Your current balance is: {balance}")

def deposit():
    print("-----------------------------------")
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        print("Amount deposited successfully!")
    else:
        print("Invalid deposit amount. Please try again.")
    print("-----------------------------------")
    return amount

def withdraw(balance):
    print("-----------------------------------")
    print("Withdrawing Money")
    amount = float(input("Enter the amount to withdraw: "))
    if amount > 0 and amount <= balance:
        print("Amount withdrawn successfully!")
        return amount
    else:
        print("Invalid withdrawal amount or insufficient balance. Please try again.")
        return 0
    print("-----------------------------------")
    


def main():

    balance = 0
    is_running = True

    while is_running:

        print("Welcome to the bank program!")
        print("-----------------------------------")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("-----------------------------------")
        choice = input("Enter your choice (1-4): ")

        match choice:

            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                print("-----------------------------------")
                print("Thank you for using the bank program!")
                print("-----------------------------------")
                is_running = False
            case _:
                print("-----------------------------------")
                print("Invalid choice, please try again.")
                print("-----------------------------------")
        

if __name__ == "__main__":
    main()
    