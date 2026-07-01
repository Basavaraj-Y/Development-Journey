#simple ATM simulator
balance = 1000          #initial balance

while True:
    print("\n-----ATM Menu-----")
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        print(f"Your current balance is  {balance} rs.")

    elif choice == 2:
        amount = float(input("Enter the amount to Deposite:"))
        balance += amount
        print("Amount Deposited successfully.")
        print(f"Your current balance is {balance} rs.")

    elif choice == 3:
        amount = float(input("Enter the amount to withdraw:"))
        balance -= amount
        print("Amount Withdrawn Successfully.")
        print(f"Your current balance is {balance} rs.")

    elif choice == 4:
        print("Thank you for using ATM,Have a good day.")
        break
    
    else:
        print("Invalid choice, please enter a valid choice.")