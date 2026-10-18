#4. Mini Project (W1): Simple ATM Simulator 🏧
'''Project Features
1.User login using a PIN
2.Check account balance
3.Deposit money
4.Withdraw money
5.Use separate functions for each operation
6.Exit the program'''

# Simple ATM Simulator

PIN = "1234"
balance = 5000.0


def login():
    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")

        if entered_pin == PIN:
            print("\nLogin Successful!")
            return True

        attempts -= 1
        print("Incorrect PIN!")

        if attempts > 0:
            print("Attempts remaining:", attempts)

    print("Too many incorrect attempts. Access denied.")
    return False


def check_balance():
    print(f"\nYour current balance is: Rs. {balance:.2f}")


def deposit():
    global balance

    amount = float(input("Enter amount to deposit: Rs. "))

    if amount <= 0:
        print("Please enter a valid amount.")
    else:
        balance += amount
        print(f"Rs. {amount:.2f} deposited successfully.")
        check_balance()


def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: Rs. "))

    if amount <= 0:
        print("Please enter a valid amount.")

    elif amount > balance:
        print("Insufficient balance!")

    else:
        balance -= amount
        print(f"Rs. {amount:.2f} withdrawn successfully.")
        check_balance()


def atm_menu():
    while True:
        print("\n===== SIMPLE ATM SIMULATOR =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice! Please try again.")


# Main Program
print("Welcome to the ATM Simulator")

if login():
    atm_menu()