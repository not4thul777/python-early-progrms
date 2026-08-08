def show_balance(balance):
    print("---------------------")
    print(f"Your balance is ${balance:.2f}")
    print("---------------------")


def deposit():
    print("---------------------")
    amount = float(input("Enter an amount to deposit: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        print("---------------------")
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))

    if amount > balance:
        print("---------------------")
        print("Insufficient balance")
        print("---------------------")
        return 0

    elif amount <= 0:
        print("---------------------")
        print("Enter a valid amount to withdraw")
        print("---------------------")
        return 0

    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("---------------------")
        print("    BANKING PROGRAM")
        print("---------------------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("---------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance += deposit()

        elif choice == "3":
            balance -= withdraw(balance)

        elif choice == "4":
            is_running = False

        else:
            print("That is not a valid choice")

    print("---------------------")
    print("THANK YOU! HAVE A NICE DAY")
    print("---------------------")


if __name__ == "__main__":
    main()
