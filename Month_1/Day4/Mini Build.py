#Refactor ATM project using functions

def show_menu():
    print("----ATM Menu----")
    print("1.Check balance")
    print("2.Deposite")
    print("3.withdraw")
    print("4.Exit")

def check_balance(balance):
    print(f"current balance:{balance}")

def deposite(balance):
    amount = float(input("Enter amount to depodite:"))
    
    if amount > 0:
        balance += amount
        print(f"{amount} deposited successfully.")
    else:
        print("Invalid amount.")

    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw:"))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("insufficient balance.")
    else:
        balance -= amount
        print(f"{amount} withdraw successfully.")

    return balance

balance = 10000

while True:
    show_menu()

    choice = int(input("Enter a choice:"))

    if choice == 1:
        check_balance(balance)

    elif choice == 2:
        balance = deposite(balance)

    elif choice == 3:
        balance = withdraw(balance)

    elif choice == 4:
        print("Thanks for using ATM,Have a good day!...")
        break
    else:
        print("Invalid choice, Try again.")
