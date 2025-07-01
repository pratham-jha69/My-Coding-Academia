import random

def spin_row():
    symbols = ["🍒", "🍋", "🍉", "⭐", "🔔"]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("-------------------")
    print(" | ".join(row))
    print("-------------------")



def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet * 2
        elif row[0]=="🍋":
            return bet * 3
        elif row[0]=="🍉":
            return bet * 4
        elif row[0]=="⭐":
            return bet * 5
        elif row[0]=="🔔":
            return bet * 10
    return 0


def main():
    
    
    balance = 100



    print("----------------------------")
    print("Welcome to the Slot Machine!")
    print("----------------------------")


    while balance > 0:

        print(f"Current balance: {balance}")

        bet=input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid bet amount. Please enter a number.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient balance for this bet.")
            continue

        if bet <= 0:
            print("Bet amount must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning....")
        
        
        print_row(row)
        
        
        payout = get_payout(row,int(bet))
        if payout > 0:
            print(f"You won: {payout}")
        else:
            print("Better luck next time!")

        balance += payout
        print(f"Your new balance is: {balance}")

        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
