balance = 0
def check_balance():
    print(f"Your balance is {balance}")
def withdraw_cash():
    global balance
    amount = int(input("Enter the amount you want to withdraw: "))
    if amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        print(f"{amount} withdrawn successfully")
def deposit_cash():
    global balance
    amount = int(input("Enter the amount you want to deposit: "))
    balance = balance + amount
    print(f"{amount} deposited successfully")
while True:
    print("1. Check balance")
    print("2. Withdraw cash")
    print("3. Deposit cash")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        check_balance()
    elif choice == 2:
        withdraw_cash()
    elif choice == 3:
        deposit_cash()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
print("Thank you for using our ATM")