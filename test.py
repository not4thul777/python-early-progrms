

def show_balance(balance):
    print("---------------------")
    print(f"your balance is ${balance:.2f}")
    print("---------------------")
def deposit():
    print("---------------------")
    amount=float(input("enter an amount to be deposit:"))
    if amount<0:
        print("thats not a valid amount")
        return 0
        print("---------------------")
    else:
        return amount
def withdraw(balance):
    amount=float(input("enter the amount to be withdrawn:"))
    if amount>balance:
        print("---------------------")
        print("insufficient balance")
        print("---------------------")
        return 0
    elif amount<=0:
        print("---------------------")
        print("enter a valid amount to withdraw")
        print("---------------------")
        return 0
    else:
        return amount
def main():
    balance=0
    is_running = True
    while is_running:
        print("---------------------")
        print("   BANKING PROGRAM  ")
        print("---------------------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("---------------------")

        choice=input("Enter your choice (1-4): ")
        if choice=='1':
            show_balance(balance) 
        elif choice=='2':
            balance += deposit()
        elif choice=='3':
            balance -= withdraw(balance)
        elif choice=='4':
            is_running= False
        else:
            print("that is not a valid choice") 
    print("---------------------")
    print("THANK YOU HAVE A NICE DAY")
    print("---------------------")

if __name__=='__main__':
    main()